# -*- coding: utf-8 -*-
#QuenserLibrary.py

from robot.api.deco import keyword


class QuenserLibrary1:
    def PrintTEST1(self):
        """ พิมพ์ข้อความ 'Hello, world!' ลงในคอนโซล แบบไม่ได้แอดคีย์ """
        print("Hello, world! เทสภาษาไทย111")

    @keyword("Hello world1")
    def Hello(self):
        """ พิมพ์ข้อความ 'Hello, world!' ลงในคอนโซล แบบแอดคีย์ """
        print("Hello, world! Test keyword='Hello, world!111'")
