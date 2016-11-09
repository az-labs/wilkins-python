#!/usr/bin/python

import unittest
import subprocess
import sys


class TestWilkins(unittest.TestCase):

    def test_cliusage(self):
        expected_result = '{'
        expected_result += '"synonyms": ["bla", "rest"], '
        expected_result += '"type": "Verb", '
        expected_result += '"residual": ["1 (stay%2:30:00::)", '
        expected_result += '"6 (rest%2:30:00::)"]}'
        output = subprocess.check_output(['./wilkins.py', '--word', 'remain',
                                          '--output', 'json'])
        self.assertEqual(output.strip(), expected_result)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestWilkins)
    ret_val = unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful()
    sys.exit(not ret_val)
