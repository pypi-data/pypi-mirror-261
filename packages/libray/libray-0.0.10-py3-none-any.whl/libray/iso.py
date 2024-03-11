# -*- coding: utf8 -*-

# libray - Libre Blu-Ray PS3 ISO Tool
# Copyright © 2018 - 2024 Nichlas Severinsen
#
# This file is part of libray.
#
# libray is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# libray is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with libray.  If not, see <https://www.gnu.org/licenses/>.


import os
import sys
import sqlite3
import pathlib
from threading import Thread
import time
import pkg_resources
from tqdm import tqdm
from Crypto.Cipher import AES


try:
    from libray import core
    from libray import ird
    from libray import sfo
except ImportError:
    import core
    import ird
    import sfo


class ISO:
    """Class for handling PS3 .iso files.

    Attributes:
      size:              Size of .iso in bytes
      number_of_regions: Number of regions in the .iso
      regions:           List with info of every region
      game_id:           PS3 game id
      ird:               IRD object (see ird.py)
      disc_key:          data1 from .ird, encrypted
    """

    NUM_INFO_BYTES = 4

    def read_regions(self, input_iso):
        """List with info dict (start, end, whether it's encrypted) for every region.

        Basically, every other (odd numbered) region is encrypted.
        """

        # The first region is always unencrypted

        encrypted = False

        regions = [{
            'start': core.to_int(input_iso.read(self.NUM_INFO_BYTES)) * core.SECTOR,  # Should always be 0?
            'end': core.to_int(input_iso.read(self.NUM_INFO_BYTES)) * core.SECTOR + core.SECTOR,
            'enc': encrypted
        }]

        # We'll read 4 bytes until we hit a non-size (<=0)

        while True:

            encrypted = not encrypted

            end = core.to_int(input_iso.read(self.NUM_INFO_BYTES)) * core.SECTOR

            if not end:
                break

            regions.append({
                'start': regions[-1]['end'],
                'end': end + core.SECTOR - (core.SECTOR if encrypted else 0),
                'enc': encrypted
            })

        return regions

    def __init__(self, args):
        """ISO constructor using args from argparse."""

        self.size = core.size(args.iso)

        if not self.size:
            core.error('looks like ISO file/mount is empty?')

        with open(args.iso, 'rb') as input_iso:
            # Get number of unencrypted regions
            self.number_of_unencrypted_regions = core.to_int(input_iso.read(self.NUM_INFO_BYTES))

            # Skip unused bytes
            input_iso.seek(input_iso.tell() + self.NUM_INFO_BYTES)

            self.regions = self.read_regions(input_iso)

            # Seek to the start of sector 2, '+ 16' skips a section containing some 'playstation'
            input_iso.seek(core.SECTOR + 16)

            self.game_id = input_iso.read(16).decode('utf8').strip()

            # Find PARAM.SFO

            core.vprint('Searching for PARAM.SFO', args)

            input_iso.seek(0)
            counter = 1
            found_param = False

            while True:

                data = input_iso.read(8)

                if not data:
                    break

                # if data == b'PS3LICDA':
                #  print(data)

                if data[0:4] == b'\x00\x50\x53\x46':
                    found_param = True

                    # input_iso.seek(input_iso.tell() - 8)
                    # param = sfo.SFO(input_iso)
                    # print(param['TITLE'])
                    # print(param['TITLE_ID'])
                    break

                input_iso.seek((core.SECTOR * counter))

                counter += 1

            game_title = ''

            if found_param:
                input_iso.seek(input_iso.tell() - 8)
                try:
                    param = sfo.SFO(input_iso)
                    core.vprint('PARAM.SFO found', args)

                    game_title = core.multiman_title(param['TITLE'])

                    if args.verbose and not args.quiet:
                        param.print_info()

                    # Set output to multiman style
                    if not args.output:
                        args.output = f'{game_title} [{param["TITLE_ID"]}].iso'

                except Exception:
                    core.warning('Failed reading SFO', args)

        self.disc_key = self.get_key_from_args(game_title, args)
        if args.verbose and not args.quiet:
            self.print_info()

    def decrypt(self, args):
        """Decrypt self using args from argparse."""

        core.vprint(f'Decrypting with disc key: {self.disc_key.hex()}', args)

        with open(args.iso, 'rb') as input_iso:

            if not args.output:
                output_name = f'{self.game_id}.iso'
            else:
                output_name = args.output

            core.vprint(f'Decrypted .iso is output to: {output_name}', args)

            with open(output_name, 'wb') as output_iso:

                if not args.quiet:
                    pbar = tqdm(total=(self.size // 2048))

                for region in self.regions:
                    input_iso.seek(region['start'])

                    # Unencrypted region, just copy it
                    if not region['enc']:
                        while input_iso.tell() < region['end']:
                            data = input_iso.read(core.SECTOR)
                            if not data:
                                core.warning('Trying to read past the end of the file', args)
                                break
                            output_iso.write(data)

                            if not args.quiet:
                                pbar.update(1)
                        continue
                    # Encrypted region, decrypt then write
                    else:
                        while input_iso.tell() < region['end']:
                            num = input_iso.tell() // 2048
                            iv = bytearray([0 for i in range(0, 16)])
                            for j in range(0, 16):
                                iv[16 - j - 1] = (num & 0xFF)
                                num >>= 8

                            data = input_iso.read(core.SECTOR)
                            if not data:
                                core.warning('Trying to read past the end of the file', args)
                                break

                            cipher = AES.new(self.disc_key, AES.MODE_CBC, bytes(iv))
                            decrypted = cipher.decrypt(data)

                            output_iso.write(decrypted)

                            if not args.quiet:
                                pbar.update(1)

                if not args.quiet:
                    pbar.close()

                core.vprint('Decryption complete!', args)

    def encrypt(self, args):
        """Encrypt self using args from argparse."""

        core.vprint(f'Re-encrypting with disc key: {self.disc_key.hex()}', args)

        with open(args.iso, 'rb') as input_iso:

            if not args.output:
                output_name = f'{self.game_id}_e.iso'
            else:
                output_name = args.output

            core.vprint(f'Re-encrypted .iso is output to: {output_name}', args)

            with open(output_name, 'wb') as output_iso:

                if not args.quiet:
                    pbar = tqdm(total=(self.size // 2048))

                for region in self.regions:
                    input_iso.seek(region['start'])

                    # Unencrypted region, just copy it
                    if not region['enc']:
                        while input_iso.tell() < region['end']:
                            data = input_iso.read(core.SECTOR)
                            if not data:
                                core.warning('Trying to read past the end of the file', args)
                                break
                            output_iso.write(data)

                            if not args.quiet:
                                pbar.update(1)
                        continue
                    # Decrypted region, re-encrypt it
                    else:
                        while input_iso.tell() < region['end']:
                            num = input_iso.tell() // 2048
                            iv = bytearray([0 for i in range(0, 16)])
                            for j in range(0, 16):
                                iv[16 - j - 1] = (num & 0xFF)
                                num >>= 8

                            data = input_iso.read(core.SECTOR)
                            if not data:
                                core.warning('Trying to read past the end of the file', args)
                                break

                            cipher = AES.new(self.disc_key, AES.MODE_CBC, bytes(iv))
                            encrypted = cipher.encrypt(data)

                            output_iso.write(encrypted)

                            if not args.quiet:
                                pbar.update(1)

                if not args.quiet:
                    pbar.close()

                core.vprint('Re-encryption complete!', args)

    def get_key_from_args(self, game_title, args):
        # key provided with -d / --decryption-key
        if args.decryption_key:
            return core.to_bytes(args.decryption_key)

        def get_key_from_ird(i):
            self.ird = ird.IRD(i)
            if self.ird.region_count != len(self.regions):
                core.error(
                    f'Corrupt ISO or error in IRD. Expected {self.ird.region_count} regions, found {len(self.regions)} regions')

            if self.regions[-1]['start'] > self.size:
                core.error(
                    f'Corrupt ISO or error in IRD. Expected filesize larger than {self.regions[-1]["start"]/1024**3:.2f} GiB, actual size is {self.size/1024**3:.2f} GiB')
            cipher = AES.new(core.ISO_SECRET, AES.MODE_CBC, core.ISO_IV)
            return cipher.encrypt(self.ird.data1)

        # .ird file given with -k / --ird
        if args.ird:
            return get_key_from_ird(args.ird)

        # No key or .ird specified. Let's first check if keys.db is packaged with this release
        core.vprint('Checking for bundled redump keys', args)

        try:
            db = sqlite3.connect(pkg_resources.resource_filename(__name__, 'data/keys.db'))
        except FileNotFoundError:
            db = sqlite3.connect((pathlib.Path(__file__).resolve() / 'data/') / 'keys.db')
        c = db.cursor()

        # UPDATE: 2024 - New database now has game/title ids. See if we have that.

        core.vprint('Searching using TITLE_ID', args)
        keys = c.execute('SELECT name, key FROM games WHERE title_id = ?', [self.game_id.replace('-','')]).fetchall()
        if len(keys) == 1:
            core.vprint(f'Found potential redump key: "{keys[0][0]}"', args)
            return keys[0][1]

        # Then check if there's only one game with this exact size
        core.vprint('Trying to find redump key based on size', args)
        keys = c.execute('SELECT name, key FROM games WHERE size = ?', [str(self.size)]).fetchall()
        if len(keys) == 1:
            core.vprint(f'Found potential redump key: "{keys[0][0]}"', args)
            return keys[0][1]

        # If not, see if we can filter it out based on name and size
        core.vprint('Trying to find redump key based on size, game title, and country', args)
        if not game_title:
            raise ValueError

        keys = c.execute('SELECT name, key FROM games WHERE lower(name) LIKE ? AND size = ?', [
                         '%' + '%'.join(game_title.lower().split(' ')) + '%' + core.serial_country(self.game_id).lower() + '%', str(self.size)]).fetchall()
        if keys:
            core.vprint(f'Found potential redump key: "{keys[0][0]}"', args)
            return keys[0][1]

        # since checksums can take a while to calculate, bail here unless the
        # user has specifically indicated they want to try the CRC32 fallback
        if not args.checksum:
            core.error('could not find disc key')

        # Okay, searching has failed us, but maaaybe the checksum works?
        core.vprint('Trying to find redump key based on CRC32', args)
        crc32 = None
        crc32_continue = [True]
        if args.checksum_timeout > 0:
            def timeout(allow_execution):
                time.sleep(float(args.checksum_timeout))
                if crc32 is None:
                    core.vprint(f'could not calculate CRC32 before {args.checksum_timeout}-second timeout', args)
                    allow_execution[0] = False
            crc_thread = Thread(target=timeout, args=(crc32_continue,), daemon=True)
            crc_thread.start()

        crc32 = core.crc32(args.iso, crc32_continue)
        if crc32 is None:
            raise TimeoutError

        keys = c.execute('SELECT name, key FROM games WHERE crc32=?', [crc32.lower()]).fetchall()
        if len(keys) == 1:
            core.vprint(f'Found potential redump key: "{keys[0][0]}" (CRC32={crc32.lower()})', args)
            return keys[0][1]

        # Fallback to downloading an IRD from the internet (currently disabled)
        # try:
        #   core.warning('No IRD file specified, finding required file', args)
        #   args.ird = core.ird_by_game_id(self.game_id) # Download ird
        #   return get_key_from_ird(args.ird)
        # except:
        #   core.vprint('Could not download IRD file', args)

        raise ValueError

    def print_info(self):
        # TODO: This could probably have been a __str__? Who cares?
        """Print some info about the ISO."""
        print(f'Game ID: {self.game_id}')
        print(f'Key: {self.disc_key.hex()}')
        print(f'Info from ISO:')
        print(f'Unencrypted regions: {self.number_of_unencrypted_regions}')
        for i, region in enumerate(self.regions):
            print(i, region, region['start'] // core.SECTOR, region['end'] // core.SECTOR)
