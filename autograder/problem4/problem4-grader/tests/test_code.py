import unittest
from gradescope_utils.autograder_utils.decorators import weight, tags, number, visibility
from problem4 import calculate


class TestIntegration(unittest.TestCase):
    def setUp(self):
        pass

    @weight(1)
    @number('4.1')
    def test1(self):
        '''Test 1: Sample 1 (Part 1)'''

        case_input = "1 + 4 + 7 + 2 + 492"
        case_output = 506
        assert (calculate(case_input)) == case_output

    @weight(1)
    @number('4.2')
    def test2(self):
        '''Test 2: Hidden (Part 1 only)'''

        case_input = "24 + 8 + 7 + 1 + 3 + 8 + 9 + 47 + 32"
        case_output = 139
        assert (calculate(case_input)) == case_output

    @weight(1)
    @number('4.3')
    def test3(self):
        '''Test 3: Sample 2 (Part 2)'''

        case_input = "1 - 2 / 7 + 2 + 492"
        case_output = -1
        assert (calculate(case_input)) == case_output

    @weight(1)
    @number('4.4')
    def test4(self):
        '''Test 4: 2 - 2 / 2 - 3 + 4'''
        case_input = "2 - 7 / 2 - 3 + 4"
        case_output = -10
        assert (calculate(case_input)) == case_output

    @weight(1)
    @number('4.5')
    def test5(self):
        '''Test 5: Hidden (Part 2 only)'''
        case_input = "10 - 3 + 2 + 2 / 1"
        case_output = 3
        assert (calculate(case_input)) == case_output


    @weight(1)
    @number('4.6')
    def test6(self):
        '''Test 6: Sample 3 (Part 3)'''

        case_input = "10 - 2 / 7 * 2 + 1"
        case_output = 3
        assert (calculate(case_input)) == case_output

    @weight(1)
    @number('4.7')
    def test7(self):
        '''Test 7: Hidden (Part 3 only)'''

        case_input = "1 + 1 + 3 + 4 + 9 * 4 / 3 * 2"
        case_output = 36
        assert (calculate(case_input)) == case_output

    @weight(1)
    @number('4.8')
    def test8(self):
        '''Test 8: Sample 4 (Part 4)'''

        case_input = "6 - (8 / 2) * 2 + 2"
        case_output = 8
        assert (calculate(case_input)) == case_output

    @weight(1)
    @number('4.9')
    def test9(self):
        '''Test 9: 1 + 1 + (3 + (2 + 4)) + (9 * 4 / 3) * 2 + (3 * 1/2)'''

        case_input = "1 + 1 + (3 + (2 + 4)) + (9 * 4 / 3) * 2 + (3 * 1/2)"
        case_output = 40
        assert (calculate(case_input)) == case_output

    @weight(1)
    @number('4.10')
    def test10(self):
        '''Test 10: Hidden'''

        case_input = "200 - (4 - 2 * 3) + (9 * ((3/2) * (15/3)))"
        case_output = 149
        assert (calculate(case_input)) == case_output