from microbit import *
from status_display import StatusDisplay
from interval_timer import IntervalTimer

class Power:
    OFF = 0
    ON = 1

class Mode:
    SETTINGS = 0
    POWER = 1

class MicrobitPinController:
    def __init__(self):
        self.pins = [pin0, pin1, pin2]
        self._pin = None
        self.mode = Mode.POWER
        self.power_status = Power.OFF
        self.timer = IntervalTimer()

    def _get_pin_index(self) -> int:
        if self._pin is None:
            return -1
        return self.pins.index(self._pin)
    
    def set_pin(self, pin):
        self._pin = pin
        display.show(str(self._get_pin_index()), delay=200, clear=True)

    def set_pin_power(self, pin, power_status: int):
        self.power_status = power_status
        pin.write_digital(power_status)

    def reset_pins(self) -> None:
        self.power_status = Power.OFF
        for pin in self.pins:
            self.set_pin_power(pin, self.power_status)

    def toggle_mode(self) -> None:
        self.mode = not self.mode
        if self.mode == Mode.SETTINGS:
            self.reset_pins()
            StatusDisplay.display_settings()
        elif self.mode == Mode.POWER:
            StatusDisplay.display_start()
            if self._pin is not None:
                self.set_pin_power(self._pin, Power.ON)
                self.timer.reset()

    def update_interval_timer(self):
        display.scroll(str(self.timer.change_interval()))
        self.timer.reset()

    def timer_expired_handler(self) -> None:
        if self.timer.is_timer_expired():
            power = int(not self.power_status)
            self.set_pin_power(self._pin, power)
            StatusDisplay.display_pin_status(self.pins.index(self._pin), power)
            self.timer.reset()

