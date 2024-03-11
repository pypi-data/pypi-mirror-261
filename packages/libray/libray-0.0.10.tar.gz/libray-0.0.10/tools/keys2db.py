#!/usr/bin/env python3
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

# This script transforms Datfile.dat and keys/*.key keyfiles into a sqlite3 keys.db
# Keys.db is then moved to libray/data/keys.db and packaged with libray in setup.py.
# Libray checks if this file is bundled with it and has logic to identify the correct key.

# TODO: In theory we could add the game-serials (BLUS-0000) and check that first.


import bs4
import csv
import sys
import shutil
import sqlite3
import pathlib
import argparse


import requests


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--database', type=pathlib.Path, default='keys.db', help='Path to keys.db')
    parser.add_argument('-k', '--keys', type=pathlib.Path, default='keys', help='Path to .key keys')
    parser.add_argument('--show-missing', action='store_true', help='Show titles missing keys')
    args = parser.parse_args()

    if args.database.exists():
        args.database.unlink()

    # Check if there's a mapping csv that maps the keynames to title IDs
    mapping = pathlib.Path('keys.csv')

    title_ids = {}

    if mapping.exists():
        with open(mapping, 'r') as infile:
            reader = csv.DictReader(infile, delimiter=',', quotechar='"', )
            for row in reader:
                title_ids[row['md5']] = {
                    'title_id': row['title_id'],
                    'filename': row['filename'],
                    'size': row['size'],
                    'crc32': row['crc32'],
                }

    db = sqlite3.connect(args.database)
    c = db.cursor()

    c.execute('CREATE TABLE games (title_id TEXT, name TEXT, size TEXT, crc32 TEXT, md5 TEXT, sha1 TEXT, key BLOB)')
    db.commit()

    cwd = pathlib.Path(__file__).resolve().parent

    keys_path = cwd / 'keys'

    if not keys_path.exists():
        print('Error: No keys/ folder. Place the .key files in a tools/keys/ folder')
        sys.exit()

    any_dats = [x for x in cwd.glob('*.dat')]

    if not any_dats:
        print('Error: No .dat file. Place the .dat file in the tools/ folder')
        sys.exit()

    datfile = any_dats[0]

    warnings = 0

    with open(datfile, 'r') as infile:

        soup = bs4.BeautifulSoup(infile.read(), features='html5lib')

        for game in soup.find_all('game'):

            name = game.find('description').text.strip()
            attrs = game.find('rom').attrs

            try:

                title_map = title_ids[attrs['md5']]

                assert title_map['size'] == attrs['size']
                assert title_map['crc32'] == attrs['crc']

                title_id = title_map['title_id']

            except (KeyError, AssertionError):
                title_id = None

            # Some of the records are spaces:
            if not title_id:
                title_id = None

            entry = [title_id, name, attrs['size'], attrs['crc'], attrs['md5'], attrs['sha1']]

            try:
                with open(cwd / ('keys/' + name + '.key'), 'rb') as keyfile:
                    entry.append(keyfile.read())
            except FileNotFoundError:
                warnings += 1
                if args.show_missing:
                    print('Warning: missing keyfile for %s [%s]' % (name, attrs['crc']))

                c.execute('INSERT INTO games (title_id, name, size, crc32, md5, sha1) VALUES (?, ?, ?, ?, ?, ?)', entry)
                continue

            c.execute('INSERT INTO games VALUES (?, ?, ?, ?, ?, ?, ?)', entry)

    db.commit()

    db.close()

    data_path = (cwd.parent / 'libray') / 'data/'

    if not data_path.exists():
        data_path.mkdir()

    shutil.copyfile(args.database, ((cwd.parent / 'libray') / 'data/') / args.database.name)

    print('Warning: no keyfiles for %s titles' % str(warnings))





