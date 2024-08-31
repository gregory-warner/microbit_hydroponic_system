from microbit import Image, display

class StatusDisplay:
    status = {
        0: Image.ARROW_S,
        1: Image.ARROW_N
    }

    settings_image = Image(
        "09000:"
        "99000:"
        "00900:"
        "00099:"
        "00099"
    )

    @staticmethod
    def display_pin_status(pin_number: int, power_status: int) -> None:
        display.show([str(pin_number), StatusDisplay.status[power_status]] * 2, delay=800, clear=True)
        
    @staticmethod
    def display_settings():
        display.show(StatusDisplay.settings_image, delay=2500, clear=True)

    def display_reset():
        display.show([
            Image(
                "00000:"
                "00000:"
                "00000:"
                "00000:"
                "99999"
            ),
            Image(
                "00000:"
                "00000:"
                "00000:"
                "99999:"
                "00000"
            ),
            Image(
                "00000:"
                "00000:"
                "99999:"
                "00000:"
                "00000"
            ),
            Image(
                "00000:"
                "99999:"
                "00000:"
                "00000:"
                "00000"
            ),
            Image(
                "99999:"
                "00000:"
                "00000:"
                "00000:"
                "00000"
            ),
        ], delay=200, clear=True)