from microbit import *
from microbit_pin_controller import MicrobitPinController, Mode

def main():
    pc = MicrobitPinController()

    while True:
        if button_a.is_pressed() and button_b.is_pressed():
            pc.toggle_mode()
        if pc.mode == Mode.SETTINGS:
            if button_a.is_pressed():
                for pin in pc.pins:
                    if pin.is_touched():
                        pc.set_pin(pin)
                        break
                continue
            if button_b.is_pressed():
                pc.update_interval_timer()
                
        pc.timer_expired_handler()

if __name__ == "__main__":
    main()
