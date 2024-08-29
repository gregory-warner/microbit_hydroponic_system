from microbit import *
from pin_status_display import PinStatusDisplay
from interval_timer import IntervalTimer

class Power:
    off=0
    on=1

class Mode:
    power=0
    settings=1

class MicrobitPinController:
    def __init__(self):
        """
        Initializes a new instance of the MicrobitPinController class. Sets up three pins (pin0, pin1, and pin2) on the microbit board,
        and initializes an interval timer to control the duration between power toggles for a selected pin.
        By default, power is turned on to pin0.
        """
        self.pins = [pin0, pin1, pin2]
        self.timer = IntervalTimer()
        self.initialize_pin(0)

    def initialize_pin(self, pin_index: int) -> None:
        self._pin = self.pins[pin_index]
        self.mode = Mode.power
        self.power_status = Power.on
        self.update_pin(pin_index)

    def enable_settings_mode(self):
        self.mode = Mode.settings
        self.power_status = Power.off
        [pin.write_digital(0) for pin in self.pins]

    def enable_pin_touch_listener(self):
        [pin.write_digital(0) for pin in self.pins]

        if button_a.is_pressed():
            for i, pin in enumerate(self.pins):
                if pin.is_touched():
                    self.update_pin(i)

    def update_pin(self, pin_number: int) -> None:
        self._pin = self.pins[pin_number]
        self.power_status = Power.on
        self.mode = Mode.power
        self.write_pin()

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

    def write_pin(self):
        self._pin.write_digital(self.power_status)
        PinStatusDisplay.display(self.pins.index(self._pin), self.power_status)