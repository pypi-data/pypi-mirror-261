#tests/test_submodule2.py
# -*- coding: utf-8 -*-

import unittest
from XpiumLibraryFlutter.submodule1.module2 import Module12

class TestModule2(unittest.TestCase):
    def test_PrintTEST2(self):
        mod1 = Module12()
        mod1.PrintTEST12()
        # ตรวจสอบว่าผลลัพธ์ตรงกับที่คาดหวัง

if __name__ == '__main__':
    unittest.main()
