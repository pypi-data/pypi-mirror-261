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

# This file contains tests to validate the key-retrieval logic for the
# ISO class.
# This script is not included in the release of libray.


import argparse
import unittest
import unittest.mock as mock
from Crypto.Cipher import AES

from libray import core, iso

class TestISO(unittest.TestCase):

    @mock.patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace())
    def test_explicit_decryption_key(self, mock_args):
        mock_args.iso = 'fake.iso'
        mock_args.decryption_key = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        decryptkey_bytes = core.to_bytes(mock_args.decryption_key)
        fake_iso = iso.ISO.__new__(iso.ISO)
        returned_key = fake_iso.get_key_from_args('AAA', mock_args)
        self.assertEqual(decryptkey_bytes, returned_key)

    @mock.patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace())
    def test_explicit_valid_ird(self, mock_args):
        mock_args.iso = 'fake.iso'
        mock_args.ird = 'aaa.ird'
        mock_args.decryption_key = False
        mock_args.verbose = True

        ird = mock.Mock()
        ird.region_count = 3
        ird.data1 = b'01010101010101010101010101010101'
        cipher = AES.new(core.ISO_SECRET, AES.MODE_CBC, core.ISO_IV)
        decryptkey_bytes = cipher.encrypt(ird.data1)

        fake_iso = iso.ISO.__new__(iso.ISO)
        fake_iso.size = 2048
        fake_iso.regions = [
            {'start': 0, 'end': 512, 'enc': False},
            {'start': 512, 'end': 1024, 'enc': True},
            {'start': 1024, 'end': 2048, 'enc': False}
        ]

        with mock.patch('iso.ird.IRD', return_value=ird) as mock_ird:
            returned_key = fake_iso.get_key_from_args('AAA', mock_args)
            mock_ird.assert_called_once_with('aaa.ird')
            self.assertEqual(decryptkey_bytes, returned_key)

    @mock.patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace())
    def test_ird_with_region_count_mismatch(self, mock_args):
        mock_args.iso = 'fake.iso'
        mock_args.ird = 'aaa.ird'
        mock_args.decryption_key = False
        mock_args.verbose = True

        ird = mock.Mock()
        ird.region_count = 3
        ird.data1 = b'01010101010101010101010101010101'

        fake_iso = iso.ISO.__new__(iso.ISO)
        fake_iso.size = 512
        fake_iso.regions = [
            {'start': 0, 'end': 512, 'enc': False},
        ]

        with mock.patch('iso.ird.IRD', return_value=ird) as mock_ird:
            with self.assertRaises(SystemExit):
                fake_iso.get_key_from_args('AAA', mock_args)

    @mock.patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace())
    def test_ird_with_invalid_start(self, mock_args):
        mock_args.iso = 'fake.iso'
        mock_args.ird = 'aaa.ird'
        mock_args.decryption_key = False
        mock_args.verbose = True

        ird = mock.Mock()
        ird.region_count = 3
        ird.data1 = b'01010101010101010101010101010101'

        fake_iso = iso.ISO.__new__(iso.ISO)
        fake_iso.size = 512 * 1024 * 1024
        fake_iso.regions = [
            {'start': 0, 'end': 3000000, 'enc': False},
            {'start': 3000000, 'end': 2000000000, 'enc': True},
            {'start': 2000000000, 'end': 2000001000, 'enc': False}
        ]

        with mock.patch('iso.ird.IRD', return_value=ird) as mock_ird:
            with self.assertRaises(SystemExit):
                fake_iso.get_key_from_args('AAA', mock_args)

    @mock.patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace())
    def test_keys_db_size_match(self, mock_args):
        mock_args.iso = 'fake.iso'
        mock_args.ird = ''
        mock_args.decryption_key = False
        mock_args.verbose = True

        fake_iso = iso.ISO.__new__(iso.ISO)
        fake_iso.size = 512 * 1024 * 1024
        fake_iso.game_id = 'TCUS-12345'

        with mock.patch('iso.sqlite3') as mocksql:
            decryption_key = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
            decryptkey_bytes = core.to_bytes(decryption_key)
            mocksql.connect().cursor().execute().fetchall.return_value = [['AAA', decryptkey_bytes]]
            returned_key = fake_iso.get_key_from_args('AAA', mock_args)
            self.assertEqual(decryptkey_bytes, returned_key)

    @mock.patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace())
    def test_keys_db_size_multiple_match_name_lookup(self, mock_args):
        mock_args.iso = 'fake.iso'
        mock_args.ird = ''
        mock_args.decryption_key = False
        mock_args.verbose = True

        fake_iso = iso.ISO.__new__(iso.ISO)
        fake_iso.size = 512 * 1024 * 1024
        fake_iso.game_id = 'TCUS-12345'

        with mock.patch('iso.sqlite3') as mocksql:
            decryption_key = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
            decryptkey_bytes = core.to_bytes(decryption_key)
            mocksql.connect().cursor().execute().fetchall.side_effect = [[], [['AAA', decryptkey_bytes]]]
            returned_key = fake_iso.get_key_from_args('AAA', mock_args)
            self.assertEqual(decryptkey_bytes, returned_key)

    @mock.patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace())
    def test_keys_db_size_multiple_match_no_game_id(self, mock_args):
        mock_args.iso = 'fake.iso'
        mock_args.ird = ''
        mock_args.decryption_key = False
        mock_args.verbose = True

        fake_iso = iso.ISO.__new__(iso.ISO)
        fake_iso.size = 512 * 1024 * 1024
        fake_iso.game_id = 'TCUS-12345'

        with mock.patch('iso.sqlite3') as mocksql:
            decryption_key = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
            decryptkey_bytes = core.to_bytes(decryption_key)
            mocksql.connect().cursor().execute().fetchall.return_value = [['AAA', decryptkey_bytes],['BBB', decryptkey_bytes]]
            with self.assertRaises(ValueError):
                fake_iso.get_key_from_args(None, mock_args)

    @mock.patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace())
    def test_keys_db_no_match_no_checksum(self, mock_args):
        mock_args.iso = 'fake.iso'
        mock_args.ird = ''
        mock_args.decryption_key = False
        mock_args.checksum = False
        mock_args.verbose = True

        fake_iso = iso.ISO.__new__(iso.ISO)
        fake_iso.size = 512 * 1024 * 1024
        fake_iso.game_id = 'TCUS-12345'

        with mock.patch('iso.sqlite3') as mocksql:
            mocksql.connect().cursor().execute().fetchall.return_value = []
            with self.assertRaises(SystemExit):
                fake_iso.get_key_from_args('AAA', mock_args)

    @mock.patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace())
    def test_keys_db_no_match_checksum_fallback(self, mock_args):
        mock_args.iso = 'fake.iso'
        mock_args.ird = ''
        mock_args.decryption_key = False
        mock_args.checksum = True
        mock_args.checksum_timeout = 15
        mock_args.verbose = True

        fake_iso = iso.ISO.__new__(iso.ISO)
        fake_iso.size = 512 * 1024 * 1024
        fake_iso.game_id = 'TCUS-12345'

        with mock.patch('iso.sqlite3') as mocksql:
            decryption_key = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
            decryptkey_bytes = core.to_bytes(decryption_key)
            fakeresults = ([], [], [['AAA', decryptkey_bytes]])
            mocksql.connect().cursor().execute().fetchall.side_effect = fakeresults
            with mock.patch('iso.core.crc32', return_value='01010101'):
                returned_key = fake_iso.get_key_from_args('AAA', mock_args)
                self.assertEqual(decryptkey_bytes, returned_key)

    @mock.patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace())
    def test_keys_db_no_match_checksum_timeout(self, mock_args):
        mock_args.iso = 'fake.iso'
        mock_args.ird = ''
        mock_args.decryption_key = False
        mock_args.checksum = True
        mock_args.checksum_timeout = 15
        mock_args.verbose = True

        fake_iso = iso.ISO.__new__(iso.ISO)
        fake_iso.size = 512 * 1024 * 1024
        fake_iso.game_id = 'TCUS-12345'

        with mock.patch('iso.sqlite3') as mocksql:
            mocksql.connect().cursor().execute().fetchall.return_value = []
            with mock.patch('iso.core.crc32', return_value=None):
                with self.assertRaises(TimeoutError):
                    fake_iso.get_key_from_args('AAA', mock_args)


