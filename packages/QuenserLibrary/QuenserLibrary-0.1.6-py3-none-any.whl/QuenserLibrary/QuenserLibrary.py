# -*- coding: utf-8 -*-
#QuenserLibrary.py

from robot.api.deco import keyword
from .TineLibrary import TineLibrary
from .asdasd import asdasd
from robot.libraries.BuiltIn import BuiltIn


class QuenserLibrary(TineLibrary, asdasd):

    def __init__(self):
        self._bi = BuiltIn()

    def t_quit_app(self):
        """ปิดแอพปัจจุบันและปิดเซสชัน"""
        driver = self._current_application()
        driver.quit()

    def _current_application(self):
        """คืนค่าอินสแตนซ์ของแอปพลิเคชันปัจจุบัน"""
        return self._bi.get_library_instance('AppiumFlutterLibrary')._current_application()

    
    def PrintTEST(self):
        """ พิมพ์ข้อความ 'Hello, world!' ลงในคอนโซล แบบไม่ได้แอดคีย์ """
        print("Hello, world! เทสภาษาไทยfdsafadsfsadfdsafdsa")


    @keyword("Hello world")
    def Hello(self):
        """ พิมพ์ข้อความ 'Hello, world!' ลงในคอนโซล แบบแอดคีย์ """
        print("Hello, world! Test keyword='Hello, world!'")
