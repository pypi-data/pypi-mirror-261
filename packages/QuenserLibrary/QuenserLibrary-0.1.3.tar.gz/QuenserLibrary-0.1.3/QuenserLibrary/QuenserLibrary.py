# -*- coding: utf-8 -*-
#QuenserLibrary.py

from robot.api.deco import keyword
from .TineLibrary import TineLibrary
from .asdasd import asdasd


class QuenserLibrary(TineLibrary, asdasd):

     def __init__(self):
        super().__init__()
        TineLibrary.__init__(self)
        asdasd.__init__(self)
    
    # def PrintTEST(self):
    #     """ พิมพ์ข้อความ 'Hello, world!' ลงในคอนโซล แบบไม่ได้แอดคีย์ """
    #     print("Hello, world! เทสภาษาไทย")


    # @keyword("Hello world")
    # def Hello(self):
    #     """ พิมพ์ข้อความ 'Hello, world!' ลงในคอนโซล แบบแอดคีย์ """
    #     print("Hello, world! Test keyword='Hello, world!'")
