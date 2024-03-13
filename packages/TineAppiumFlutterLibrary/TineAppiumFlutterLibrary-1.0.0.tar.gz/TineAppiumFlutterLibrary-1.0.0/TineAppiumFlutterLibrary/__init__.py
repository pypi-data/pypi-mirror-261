# -*- coding: utf-8 -*-

from TineAppiumFlutterLibrary.keywords import *
from TineAppiumFlutterLibrary.version import VERSION


class TineAppiumFlutterLibrary(
    _Support,
    _SupportElement,
    _RunOnFailureKeyWords,
    _LoggingKeywords,
):
    """ENIT_APPIUMFLUTTER SUPPORT APPIUM SERVER"""
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = VERSION
    
    

    def __init__(self):
        """ENIT_APPIUMFLUTTER SUPPORT APPIUM SERVER"""
        for base in TineAppiumFlutterLibrary.__base__:
            base.__init__(self)

