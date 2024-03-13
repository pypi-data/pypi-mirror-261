# -*- coding: utf-8 -*-

import time
import os

from robot.libraries.BuiltIn import BuiltIn
from .keywordgroup import KeywordGroup



class _Support(KeywordGroup):

    def __init__(self):

        self._bi = BuiltIn()

    #KEY_WORD#

    def t_quit_app(self):
        """ปิดแอพปัจจุบันและปิดเซสชัน"""
        driver = self._current_application()
        driver.quit()


    #PRIVATE_FUNCTION#
        
    def _current_application(self):
        """คืนค่าอินสแตนซ์ของแอปพลิเคชันปัจจุบัน"""
        return self._bi.get_library_instance('AppiumFlutterLibrary')._current_application()



    