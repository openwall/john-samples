#!/usr/bin/env python

"""
This script is used for testing the `aix2john` Python module. The `aix2john`
module is designed to process and classify different types of hashed passwords
retrieved from the IBM AIX (Advanced Interactive eXecutive) system, a Unix-based
operating system.

The `TestAix2John` class contains unit tests for the module's methods, including
`get_password_type`, `process_line`, `process_password`, and `process_file`.

Each test method typically involves an assertion, comparing the method's output
with the expected result. Mocking is used extensively for testing methods that
depend on external factors like file I/O or command-line arguments.

Usage:
    To run the unit tests, run `python -m unittest discover`. 
    Not compatible with Python 2.
"""

import unittest
import io
import argparse
from unittest.mock import patch, mock_open
import aix2john


class TestAix2John(unittest.TestCase):
    """Unit test class for the aix2john module."""

    def test_get_password_type(self):
        """Test get_password_type with various password types."""
        self.assertEqual(
            aix2john.get_password_type('*'),
            aix2john.PASSWORD_UNDEFINED)

        self.assertEqual(
            aix2john.get_password_type('YFf0/OmVZz6tQ'), 'des')

        self.assertEqual(
            aix2john.get_password_type('5f4dcc3b5aa765d61d8327deb882cf99'),
            'md5')

        self.assertEqual(
            aix2john.get_password_type(
                '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'),
            'sha256')

        self.assertEqual(
            aix2john.get_password_type('randomstring'),
            aix2john.PASSWORD_UNKNOWN)

    def test_process_line(self):
        """Test process_line with various line formats."""
        self.assertEqual(aix2john.process_line('guest:\n'), ('guest', None))

        self.assertEqual(
            aix2john.process_line('        password = *\n'), (None, '*'))

        self.assertEqual(aix2john.process_line(''), (None, None))

    @patch('builtins.print')
    def test_process_password(self, mock_print):
        """Test process_password with a locked account."""
        aix2john.process_password('guest', '*', False)
        mock_print.assert_not_called()

        aix2john.process_password('guest', '*', True)
        mock_print.assert_called_with(
            'guest:*:Account is locked or no password is set')

    @patch('builtins.open', new_callable=mock_open,
           read_data='guest:\n        password = *\n')
    @patch('builtins.print')
    def test_process_file(self, mock_print, mock_file):
        """Test process_file with a mock file."""
        mock_file.return_value.__iter__.return_value = [
            'guest:\n', '        password = *\n']

        aix2john.process_file(mock_file(), True)
        mock_print.assert_called_with(
            'guest:*:Account is locked or no password is set')

    @patch('builtins.print')
    def test_process_password_diff_password_types(self, mock_print):
        """Test process_password with various password types."""
        aix2john.process_password('paul', 'YFf0/OmVZz6tQ', False)
        mock_print.assert_called_with('paul:YFf0/OmVZz6tQ:des')

        aix2john.process_password(
            'claire', '5f4dcc3b5aa765d61d8327deb882cf99', False)
        mock_print.assert_called_with(
            'claire:5f4dcc3b5aa765d61d8327deb882cf99:md5')

        aix2john.process_password(
            'jonas',
            '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8',
            False)
        mock_print.assert_called_with(
            'jonas:5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8:sha256')

    @patch('builtins.open', new_callable=mock_open,
           read_data='guest:\n        password = *\n')
    @patch('builtins.print')
    def test_process_file_print_all_false(self, mock_print, mock_file):
        """Test process_file with print_all=False."""
        mock_file.return_value.__iter__.return_value = [
            'guest:\n', '        password = *\n']

        aix2john.process_file(mock_file(), False)
        mock_print.assert_not_called()

    @patch('aix2john.argparse.ArgumentParser.parse_args',
           return_value=argparse.Namespace(file=io.StringIO('dummy data\n'),
                                           all=True))
    def test_main_with_IOError(self, mock_args):
        """Test main function error handling when an IOError is raised."""
        with patch('aix2john.process_file', side_effect=IOError("Error message")) as mock_process:
            with patch('logging.error') as mock_log:
                with self.assertRaises(SystemExit):
                    aix2john.main()
        mock_log.assert_called_once()

    @patch('argparse.ArgumentParser.parse_args',
           return_value=argparse.Namespace(file=io.StringIO('dummy data\n'),
                                           all=True))
    def test_main_with_arguments(self, mock_args):
        """Test main function processes command line arguments correctly."""
        with patch('aix2john.process_file') as mock_process:
            aix2john.main()
            mock_process.assert_called_once()

    def test_process_line_no_username_password(self):
        """Test process_line with a line without username or password."""
        self.assertEqual(aix2john.process_line('random text\n'), (None, None))

    def test_process_line_with_password_only(self):
        """Test process_line with a line with only password."""
        self.assertEqual(
            aix2john.process_line('password = YFf0/OmVZz6tQ\n'),
            (None, 'YFf0/OmVZz6tQ'))

    @patch('builtins.open', new_callable=mock_open,
           read_data='a' * 10**6 + ':\n' + 'password = *\n')
    def test_process_file_with_large_username(self, mock_file):
        """Test process_file with an extremely large username."""
        mock_file.return_value.__iter__.return_value = [
            'a' * 10**6 + ':\n', 'password = *\n']
        with self.assertRaises(ValueError):
            aix2john.process_file(mock_file(), True)


if __name__ == '__main__':
    unittest.main()
