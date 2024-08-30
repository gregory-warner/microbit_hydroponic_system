from microbit_pin_controller import MicrobitPinController, Mode
from microbit import *

class MicrobitListener:
    def __init__(self, controller: MicrobitPinController):
        self.controller = controller
    
    def on_button_press(self):
        if button_a.is_pressed() and button_b.is_pressed():
            self.controller.toggle_mode()
            return
        
        if self.controller.mode == Mode.SETTINGS and button_b.is_pressed():
            self.controller.update_interval_timer()
        

    def on_pin_touch(self):
        if self.controller.mode == Mode.SETTINGS:
            for pin in self.controller.pins:
                if pin.is_touched():
                    self.controller.set_pin_on(pin)
                    break
            
    
