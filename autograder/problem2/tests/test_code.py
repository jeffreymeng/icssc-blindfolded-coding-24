import unittest
from gradescope_utils.autograder_utils.decorators import weight, tags, number, visibility
from problem2 import second_longest_contiguous

class TestIntegration(unittest.TestCase):
    def setUp(self):
        pass

    @weight(1.66)
    @number('2.1')
    def test1(self):
        '''Test "abbbcccccc"'''
        case_input = "abbbcccccc"
        case_output = 3
        assert second_longest_contiguous(case_input) == case_output

    @weight(1.66)
    @number('2.2')
    def test2(self):
        '''Test "ddeeddddeeee"'''
        case_input = "ddeeddddeeee"
        case_output = 4
        assert second_longest_contiguous(case_input) == case_output

    @weight(1.66)
    @number('2.3')
    def test3(self):
        '''Test fdaaaaaaaaslkdsagjsssssssssslkdasfdsk'''
        case_input = "fdaaaaaaaaslkdsagjsssssssssslkdasfdsk"
        case_output = 8
        assert second_longest_contiguous(case_input) == case_output

    @weight(1.66)
    @number('2.4')
    def test4(self):
        '''Test wwwwwaasssssdddsssssaawwww'''
        case_input = "wwwwwaasssssdddsssssaawwww"
        case_output = 5
        assert second_longest_contiguous(case_input) == case_output
    
    @weight(1.66)
    @number('2.5')
    def test5(self):
        '''Secret Test 1'''
        case_input = "ab"
        case_output = 1
        assert second_longest_contiguous(case_input) == case_output

    @weight(1.7)
    @number('2.6')
    def test6(self):
        '''Secret Test 2'''
        case_input = "lllllldssssafjjjjjjjjjjjlkdskjjjjjkjjjgdsaallkjdslkjfffdfddssssssafd"
        case_output = 6
        assert second_longest_contiguous(case_input) == case_output

