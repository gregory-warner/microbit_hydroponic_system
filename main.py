from microbit import *
from microbit_pin_controller import MicrobitPinController, Mode

def main():
    pc = MicrobitPinController()

    while True:
        if button_a.is_pressed() and button_b.is_pressed():
            pc.toggle_mode()
        if pc.mode == Mode.SETTINGS:
            if button_a.is_pressed():
                pc.set_pin_to_minimum_value()
                continue
            if button_b.is_pressed():
                pc.update_interval_timer()
        elif pc.run_count > 0:
            pc.timer_expired_handler()
            display.scroll(str(pc.run_count))

if __name__ == "__main__":
    main()
