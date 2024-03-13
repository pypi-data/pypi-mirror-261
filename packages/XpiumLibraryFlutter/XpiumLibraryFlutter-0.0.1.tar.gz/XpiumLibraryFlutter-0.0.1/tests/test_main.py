#tests/test_main.py
# -*- coding: utf-8 -*-

import unittest
from XpiumLibraryFlutter.main import MainClass

class TestMain(unittest.TestCase):
    def test_main(self):
        # ทดสอบ main class
        obj = MainClass()
        # ทดสอบเมทอดหรือคุณสมบัติของ obj

if __name__ == '__main__':
    unittest.main()
