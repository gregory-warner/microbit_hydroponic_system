from microbit import *
from pin_status_display import PinStatusDisplay
from interval_timer import IntervalTimer

class Power:
    off=0
    on=1

class Mode:
    power=0
    settings=1

class PinPowerSupply:
    def __init__(self):
        """
        Initializes a new instance of the PinPowerSupply class. Sets up three pins (pin0, pin1, and pin2) on the microbit board,
        and initializes an interval timer to control the duration between power toggles for a selected pin.
        By default, power is turned on to pin0.
        """
        self.pins = [pin0, pin1, pin2]
        self.timer = IntervalTimer()
        self.initialize_pin()

    def initialize_pin(self):
        pin_number = 0
        self._pin = self.pins[pin_number]
        self.mode = Mode.power
        self.power_status = Power.on
        self.update_pin(pin_number)

    def enable_settings_mode(self):
        self.mode = Mode.settings
        self.power_status = Power.off
        self.write_pin()
        display.scroll("Settings")

    def enable_pin_touch_handler(self):
        both_buttons_pressed = button_a.is_pressed() and button_b.is_pressed()

        if both_buttons_pressed and self.pins[0].is_touched():
            self.update_pin(0)
        elif both_buttons_pressed and self.pins[1].is_touched():
            self.update_pin(1)
        elif both_buttons_pressed and self.pins[2].is_touched():
            self.update_pin(2)

    def update_pin(self, pin_number: int) -> None:
        self.set_pin(pin_number)
        self.power_status = Power.on
        self.write_pin()
        self.disable_settings_mode()

    def disable_settings_mode(self):
        self.power_status = Power.on
        self.mode = Mode.power
        
    def set_pin(self, pin_number) -> None:
        self._pin = self.pins[pin_number]

    def check_interval_timer(self):
        """
        Checks the interval timer and toggles the power status if the timer interval is complete
        """
        if self.timer.get_remaining_time() <= 0:
            self.toggle_pin_power()
            self.timer.reset()

    def toggle_pin_power(self):
        current_power = self._pin.read_digital()
        self.power_status = not current_power
        self.write_pin()

    # def read_pin(self, pin=None):
    #     if pin is None:
    #         pin = self._pin
    #     display.show(pin.read_digital(), delay=3000)

    def write_pin(self):
        self._pin.write_digital(self.power_status)
        PinStatusDisplay.display_pin_status(self.pins.index(self._pin), self.power_status)