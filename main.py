from microbit_pin_controller import *
from microbit_listener import MicrobitListener
from microbit import *

ps = MicrobitPinController()
listener = MicrobitListener(ps)

while True:
    listener.on_button_press()
    listener.on_pin_touch()

    if ps.is_timer_expired():
        ps.timer_expired_handler()
