import random
import unittest
from gradescope_utils.autograder_utils.decorators import weight, tags, number, visibility
import problem3

class TestIntegration(unittest.TestCase):
    def setUp(self):
        pass

    @weight(2)
    @number('3.1')
    def test1(self):
        '''Test [(130, 80), (250, 120)]'''
        case_input = [(130, 80), (250, 120)]
        case_output = 110
        assert problem3.max_rest_time(case_input) == case_output


    @weight(2)
    @number('3.2')
    def test2(self):
        '''Test [(100, 60), (150, 90), (200, 120), (250, 150)]'''
        case_input = [(100, 60), (150, 90), (200, 120), (250, 150)]
        case_output = 85
        assert problem3.max_rest_time(case_input) == case_output

    @weight(1)
    @number('3.3')
    def test3(self):
        '''Test [(25, 100)]'''
        case_input = [(25, 100)]
        case_output = 0
        assert problem3.max_rest_time(case_input) == case_output

    @weight(1)
    @number('3.4')
    def test4(self):
        '''Test [(100, 100), (200, 200)]'''
        case_input = [(100, 100), (200, 200)]
        case_output = 75
        assert problem3.max_rest_time(case_input) == case_output

    @weight(2)
    @number('3.5')
    def test5(self):
        '''Test [(100, 100), (100, 200), (200, 200)]'''
        case_input = [(100, 100), (100, 200), (200, 200)]
        case_output = 50
        assert problem3.max_rest_time(case_input) == case_output

    @weight(2)
    @number('3.6')
    def test6(self):
        '''Long test (n = 1000)'''
        random.seed(1)
        case_input = []
        for i in range(1000):
            base = random.randrange(2000)
            offset = random.randrange(-500, 500)
            offset2 = random.randrange(-500, 500)
            case_input.append((base + offset + 3000, (base * 4 + offset2)))
        case_output = 2392
        assert problem3.max_rest_time(case_input) == case_output