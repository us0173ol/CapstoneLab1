from unittest import TestCase
from camelCase import *


class TestFunctions(TestCase):


    def camelCase(self):
        self.assertEqual("hello", camelCase.camel_Case('HELLO'))
        self.assertEqual("MIke was hEre", camelCase.camel_Case('mikeWasHere'))
        self.assertEqual("Unit Testing is fuN", camelCase.camel_Case('unitTestingIsFun'))
