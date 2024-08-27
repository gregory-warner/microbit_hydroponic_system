from microbit import *
from pin_status_display import PinStatusDisplay
from interval_timer import IntervalTimer

class PinPowerSupply:
    pin_status = {
        'on': 1,
        'off': 0
    }

    def __init__(self):
        """
        Initializes a new instance of the PinPowerSupply class. Sets up three pins (pin0, pin1, and pin2) on the microbit board,
        and initializes an interval timer to control the duration between power toggles for a selected pin.
        By default, power is turned on to pin0.
        """
        self.pins = [pin0, pin1, pin2]
        self._pin = self.pins[0]
        self.timer = IntervalTimer()

        self.update_pin_power(self.pins[0], self.pin_status['on'])

    def pin_power_listener(self):
        """
        Monitors for button and touch inputs and updates the power status or interval timer settings.
        If both buttons are pressed while a pin is touched, switch the power to that pin.
        If both buttons are pressed without any pins being touched, change the interval duration of the timer.
        """
        both_buttons_pressed = button_a.is_pressed() and button_b.is_pressed()

        if self.pins[0].is_touched() and both_buttons_pressed:
            self.switch_pin(self.pins[0])
            return
        
        if self.pins[1].is_touched() and both_buttons_pressed:
            self.switch_pin(self.pins[1])
            return
        
        if self.pins[2].is_touched() and both_buttons_pressed:
            self.switch_pin(self.pins[2])
            return
        
        if both_buttons_pressed:
            self.timer.change_interval()

    def check_interval_timer(self):
        """
        Checks the interval timer and toggles the power status if the timer interval is complete
        """
        if self.timer.get_remaining_time() <= 0:
        
            self.update_pin_power(self._pin, 0)
            self.timer.reset()
        
    def switch_pin(self, pin):
        """
        Switches the pin that will be powered on and off. If another pin is currently powered on, turns off that pin before turning on the new one.
        Args:
            pin (microbit.pin): The new pin with power status on
        """
        if self._pin == pin:
            return

        if self._pin is not None:
            self.update_pin_power(self._pin, self.pin_status['off'])

        self.update_pin_power(pin, self.pin_status['on'])
    
    def update_pin_power(self, pin, status):
        """
        Updates the power status of a specified pin and displays the current power status of the pin.
        Args:
            pin (microbit.pin): The pin to update the power status.
            status (int): 0: off or 1: on.
        """
        pin.write_digital(status)
        PinStatusDisplay.display_pin_status(self.pins.index(pin), status)