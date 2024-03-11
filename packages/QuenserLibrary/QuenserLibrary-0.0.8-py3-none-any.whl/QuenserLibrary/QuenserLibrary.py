# -*- coding: utf-8 -*-
#QuenserLibrary.py

from robot.api.deco import keyword

class QuenserLibrary:
    @keyword("Print Test")
    def print_test(self):
        """ พิมพ์ข้อความ 'Hello, world!' ลงในคอนโซล """
        print("Hello, world!")
