from microbit import *
from status_display import StatusDisplay
from interval_timer import IntervalTimer

class Power:
    off = 0
    on = 1

class Mode:
    power = 0
    settings = 1

class MicrobitPinController:
    def __init__(self):
        self.pins = [pin0, pin1, pin2]
        self.timer = IntervalTimer()
        self._pin = None
        self.set_pin_on(self.pins[0])

        self.is_mode_change_pressed = button_a.is_pressed() and button_b.is_pressed()
        self.is_change_interval_pressed = self.mode == Mode.settings and button_b.is_pressed()

    def toggle_mode(self) -> None:
        self.mode = not self.mode
        if self.mode == Mode.settings:
            StatusDisplay.display_settings()

    def set_pin_on(self, pin) -> None:
        if self._pin == pin or pin.read_digital() == Power.on:
            return

        self._pin = pin
        self.mode = Mode.power
        self.write_pin(self._pin, Power.on)

    def update_interval_timer(self):
        self.timer.change_interval()
        self.timer.reset()

    def check_interval_timer(self):
        if self.timer.get_remaining_time() <= 0:
            self.toggle_pin_power()
            self.timer.reset()

    def toggle_pin_power(self):
        current_power = self._pin.read_digital()
        self.power_status = not current_power
        self.write_pin(self._pin, self.power_status)

    def write_pin(self, pin, status: int) -> None:
        self.power_status = status
        pin_index = self.pins.index(pin)
        self.pins[pin_index].write_digital(status)
        StatusDisplay.display_pin_status(pin_index, status)

    def reset_pins(self):
        for pin in self.pins:
            if pin.read_digital() == Power.on:
                self.write_pin(pin, Power.off)