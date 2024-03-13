#tests/test_submodule1.py
# -*- coding: utf-8 -*-

import unittest
from XpiumLibraryFlutter.submodule1.module1 import Module11

class TestModule1(unittest.TestCase):
    def test_PrintTEST1(self):
        mod1 = Module11()
        mod1.PrintTEST11()
        # ตรวจสอบว่าผลลัพธ์ตรงกับที่คาดหวัง

if __name__ == '__main__':
    unittest.main()
