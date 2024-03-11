# -*- coding: utf-8 -*-
#ScreenshotKeywords.py
import os
from robot.libraries.BuiltIn import BuiltIn

class ScreenshotKeywords:
    def CaptureScreenshot(self, filename=None):
        """จับภาพหน้าจอปัจจุบันและฝังลงใน log.

        ถ้าไม่กำหนด `filename`, ภาพจะถูกฝังเป็น Base64 ลงใน log.html.
        """
        logdir = BuiltIn().get_variable_value('${OUTPUT DIR}')
        path = os.path.join(logdir, filename if filename else "screenshot.png")
        link = os.path.relpath(path, logdir)

        application = self._current_application()
        if filename:
            application.get_screenshot_as_file(path)
            self._html(f'<a href="{link}"><img src="{link}" width="800px"></a>')
        else:
            base64_screenshot = application.get_screenshot_as_base64()
            self._html(f'<img src="data:image/png;base64, {base64_screenshot}" width="800px">')

        return path

    def _current_application(self):
        # เรียกใช้ AppiumFlutterLibrary ที่ได้ทำการ register ไว้กับ BuiltIn library
        # คุณต้องแน่ใจว่าได้นำเข้า AppiumFlutterLibrary และสร้าง instance ในทดสอบของคุณ
        return BuiltIn().get_library_instance('AppiumFlutterLibrary')

    def _html(self, html):
        BuiltIn().log(html, html=True)
