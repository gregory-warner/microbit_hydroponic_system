from microbit_pin_controller import *
from microbit import *

ps = MicrobitPinController()


while True:
    if button_a.is_pressed() and button_b.is_pressed():
        ps.toggle_mode()
        continue

    if ps.mode == Mode.settings:
        for pin in ps.pins:
            if pin.is_touched():
                ps.set_pin_on(pin)
                break
    # if ps.mode == Mode.power:

            
    # elif ps.mode == Mode.settings:
        
    #     if ps.is_change_interval_pressed:
    #         ps.update_interval_timer()


    # ps.check_interval_timer()
