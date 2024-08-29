from microbit import *

class StatusDisplay:
    status = {
        0: Image.ARROW_S,
        1: Image.ARROW_N
    }

    settings_image = Image(
            "00900:"
            "09990:"
            "99099:"
            "09990:"
            "00900"
        )

    @staticmethod
    def display_pin_status(pin_number: int, power_status: int) -> None:
        display.show("P{}".format(str(pin_number)))
        display.show(StatusDisplay.status[power_status])
        
    def display_settings():
        display.show(StatusDisplay.settings_image, delay=10000)