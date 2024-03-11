# -*- coding: utf-8 -*-
#QuenserLibrary.py

from robot.api.deco import keyword
from .ScreenshotKeywords import ScreenshotKeywords

class QuenserLibrary(ScreenshotKeywords):
    def PrintTEST(self):
        """ พิมพ์ข้อความ 'Hello, world!' ลงในคอนโซล แบบไม่ได้แอดคีย์ """
        print("Hello, world!")

    @keyword("Hello world")
    def Hello(self):
        """ พิมพ์ข้อความ 'Hello, world!' ลงในคอนโซล แบบแอดคีย์ """
        print("Hello, world! Test keyword='Hello, world!'")
