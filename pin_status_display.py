from microbit import *

class PinStatusDisplay:
    pins_display = {
        0: Image(
            "09990:"
            "09090:"
            "09090:"
            "09090:"
            "09990"
        ),
        1: Image(
            "09900:"
            "00900:"
            "00900:"
            "00900:"
            "09990"
        ),
        2: Image(
            "09990:"
            "00090:"
            "09990:"
            "09000:"
            "09990"
        ),
    }

    pins_status = {
        0: Image(
            "00900:"
            "00900:"
            "90909:"
            "09990:"
            "00900"
        ),
        1: Image(
            "00900:"
            "09090:"
            "90909:"
            "00900:"
            "00900"
        ),
    }

    @staticmethod
    def display(pin: int, status: int, delay: int = 800) -> None:
        """
        Displays the Pin number with an arrow up if the status is on and down if the status is off
        """
        display.show([PinStatusDisplay.pins_display[pin], PinStatusDisplay.pins_status[status]] * 2, delay=delay)
        display.clear()