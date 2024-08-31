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
        self.timer = IntervalTimer()
        self._pin = None
        self.pins = [pin0, pin1, pin2]
        self.set_pin_on(self.pins[0])

    def toggle_mode(self) -> None:
        self.mode = not self.mode
        if self.mode == Mode.SETTINGS:
            StatusDisplay.display_settings()

    def set_pin_on(self, pin) -> None:
        if self._pin == pin or pin.read_digital() == Power.ON:
            return
        
        self._pin = pin
        self.mode = Mode.POWER
        self.write_pin(self._pin, Power.ON)

    def update_interval_timer(self):
        self.timer.change_interval()
        self.timer.reset()

    def check_interval_timer(self):
        if self.timer.get_remaining_time() <= 0:
            self.toggle_pin_power()
            self.timer.reset()
        
    def is_timer_expired(self) -> bool:
        return self.timer.get_remaining_time() <= 0
    
    def timer_expired_handler(self) -> None:
        self.toggle_pin_power()
        self.timer.reset()

    def reset_timer(self) -> None:
        self.timer.reset()
        StatusDisplay.display_reset()

    def toggle_pin_power(self):
        self.write_pin(self._pin, not self.power_status)

    def write_pin(self, pin, status: int) -> None:
        self.power_status = status
        pin_index = self.pins.index(pin)
        self.pins[pin_index].write_digital(status)
        StatusDisplay.display_pin_status(pin_index, status)

    def reset_pins(self):
        for pin in self.pins:
            if pin.read_digital() == Power.ON:
                self.write_pin(pin, Power.OFF)