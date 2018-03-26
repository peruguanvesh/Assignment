import unittest
from unittest.mock import patch

from string_case import StringCase

class StringCaseTest(unittest.TestCase):

    @patch('string_case.StringCase.getString', return_value='anvesh kumar')
    def test_getString_returns_correct_ouput(self, mock_method):
        '''test case for getString

        getString is mocked so that it doesnt take input from console while
        testing
        '''
        instance = StringCase()
        self.assertEqual(instance.getString(), 'anvesh kumar')

    @patch('string_case.StringCase.getString', return_value='anvesh kumar')
    def test_printString_returns_correct_output(self, mock_method):
        '''test case for printString

        printString is evaluated for expected value( which is upper case )
        while getString function is mocked so that it doesnt takes input
        from console while testing
        '''
        instance = StringCase()
        self.assertEqual(instance.printString(), 'ANVESH KUMAR')




