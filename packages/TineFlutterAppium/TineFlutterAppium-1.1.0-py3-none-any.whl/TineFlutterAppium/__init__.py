from TineFlutterAppium.keywords import *


class TineFlutterAppium(
    _Support,
    _SupportElement
):
    """ENIT_APPIUMFLUTTER SUPPORT APPIUM SERVER"""
    

    def __init__(self):
        """ENIT_APPIUMFLUTTER SUPPORT APPIUM SERVER"""
        for base in TineFlutterAppium.__base__:
            base.__init__(self)

