# -*- coding: utf-8 -*-
#ScreenshotKeywords.py
import os
from robot.libraries.BuiltIn import BuiltIn

class ScreenshotKeywords:
    @keyword("Capture Screenshot")
    def capture_screenshot(self, filename=None):
        """จับภาพหน้าจอปัจจุบันและฝังลงใน log

        ถ้าไม่กำหนด `filename`, ภาพจะถูกฝังเป็น Base64 ลงใน log.html
        """
        # ระบุโฟลเดอร์สำหรับเก็บ screenshots
        logdir = BuiltIn().get_variable_value('${OUTPUT DIR}')
        path = os.path.join(logdir, filename if filename else "screenshot.png")
        link = os.path.relpath(path, logdir)

        # ถ้ากำหนดชื่อไฟล์ ให้บันทึก screenshot ไปยังไฟล์นั้น
        if filename:
            self._current_application().get_screenshot_as_file(path)
            self._html('</td></tr><tr><td colspan="3"><a href="%s">'
                       '<img src="%s" width="800px"></a>' % (link, link))
        else:
            # ไม่กำหนดชื่อไฟล์ ให้ฝังเป็น Base64 ใน log
            base64_screenshot = self._current_application().get_screenshot_as_base64()
            self._html('</td></tr><tr><td colspan="3">'
                       '<img src="data:image/png;base64, %s" width="800px">' % base64_screenshot)

        return path

    def _current_application(self):
        # สร้างเมธอดเพื่อรับ instance ของ current application จากที่อื่น
        # คำสั่งนี้ควรเรียก appium driver หรือ อื่นๆ ที่สามารถจับภาพหน้าจอได้
        # ควรเปลี่ยน 'YourAppiumDriver' เป็นชื่อที่เหมาะสมกับ driver ของคุณ
        return BuiltIn().get_library_instance('YourAppiumDriver')

    def _html(self, html):
        # เพิ่ม HTML ลงใน log ของ Robot Framework
        BuiltIn().log(html, html=True)
