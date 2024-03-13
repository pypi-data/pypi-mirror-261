# -*- coding: utf-8 -*-

import time
import os

from robot.libraries.BuiltIn import BuiltIn
from .keywordgroup import KeywordGroup

class _SupportElement(KeywordGroup):

    def __init__(self):
        self._bi = BuiltIn()

    def t_switch_mode(self,mode):
        """Switch Mode to NATIVE_APP OR FLUTTER.
           When you open app with flutter only
        """
        driver = self._current_application()

        if mode == 'NATIVE_APP':
            driver.switch_to.context('NATIVE_APP')

        if mode == 'FLUTTER':
            driver.switch_to.context('FLUTTER')


    #PRIVATE_FUNCTION#
        
    def _current_application(self):
        """คืนค่าอินสแตนซ์ของแอปพลิเคชันปัจจุบัน"""
        return self._bi.get_library_instance('AppiumFlutterLibrary')._current_application()
        