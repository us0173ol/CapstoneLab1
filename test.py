from unittest import TestCase
from camelCase import *


class TestFunctions(TestCase):


    def test_lowercase(self):
        self.assertEqual("hello", lowercase('HELLO'))
        self.assertEqual("she sells seashells", lowercase('SHE SELLS SEASHELLS'))

    def test_camelCase(self):
        self.assertEqual("helloThere", camel_Case('hello there'))
        self.assertEqual("mikeWasHere", camel_Case('mike was here'))
        self.assertEqual("unitTestingIsFun", camel_Case('unit testing is fun'))
