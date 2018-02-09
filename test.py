from unittest import TestCase
from camelCase import *


class TestFunctions(TestCase):


    def camelCase(self):
        self.assertEqual("hello", camel_Case('HELLO'))
        self.assertEqual("MIke was hEre", camel_Case('mikeWasHere'))
        self.assertEqual("Unit Testing is fuN", camel_Case('unitTestingIsFun'))
