#!/usr/bin/python

import unittest
import subprocess

class TestWilkins(unittest.TestCase):

    def test_cliusage(self):
        output = subprocess.check_output(['./wilkins.py', '--word', 'remain', '--output', 'json'])
        self.assertEqual(output.strip(), '{"synonyms": ["bla", "rest"], "type": "Verb", "residual": ["1 (stay%2:30:00::)", "6 (rest%2:30:00::)"]}')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestWilkins)
    unittest.TextTestRunner(verbosity=2).run(suite)
