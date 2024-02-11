import unittest
from gradescope_utils.autograder_utils.decorators import weight, tags, number
import subprocess

class TestIntegration(unittest.TestCase):
    def setUp(self):
        pass

    @weight(2.0)
    @number('1.1')
    @tags('integration')
    def test1(self):
        '''Line 1'''
        hello = subprocess.Popen('python3 -u importer.py'.split(),
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                encoding='utf8')
        stdout, _ = hello.communicate()
        stdout = stdout.strip().split('\n')

        self.assertTrue(len(stdout) >= 1)
        self.assertEqual(stdout[0], 'hELLO wORLD11')
        hello.terminate()

    @weight(2.0)
    @number('1.2')
    @tags("integration")
    def test2(self):
        '''Line 2'''
        hello = subprocess.Popen('python3 -u importer.py'.split(),
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                encoding='utf8')
        stdout, _ = hello.communicate()
        stdout = stdout.strip().split('\n')
        self.assertTrue(len(stdout) >= 2)
        self.assertEqual(stdout[1], ':sunglasses:')
        hello.terminate()

    @weight(2.0)
    @number('1.3')
    @tags("integration")
    def test3(self):
        '''Line 3'''
        hello = subprocess.Popen('python3 -u importer.py'.split(),
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                encoding='utf8')
        stdout, _ = hello.communicate()
        stdout = stdout.strip().split('\n')
        self.assertTrue(len(stdout) >= 3)
        self.assertEqual(stdout[2], str(min(420 ** 5, 42 ** 42, 5 ** 420)))
        hello.terminate()

    @weight(2.0)
    @number('1.4')
    @tags("integration")
    def test4(self):
        '''Line 4'''
        hello = subprocess.Popen('python3 -u importer.py'.split(),
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                encoding='utf8')
        stdout, _ = hello.communicate()
        stdout = stdout.strip().split('\n')
        self.assertTrue(len(stdout) >= 4)
        self.assertEqual(stdout[3], str((8 * 70 + 1965)/5))
        hello.terminate()

    @weight(2.0)
    @number('1.5')
    @tags("integration")
    def test5(self):
        '''Line 5'''
        hello = subprocess.Popen('python3 -u importer.py'.split(),
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                encoding='utf8')
        stdout, _ = hello.communicate()
        stdout = stdout.strip().split('\n')
        self.assertTrue(len(stdout) >= 5)
        self.assertEqual(stdout[4], 'type the wrods "I\'m a big kid now!" then move on :)')
        hello.terminate()
