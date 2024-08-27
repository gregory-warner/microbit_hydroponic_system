from pin_power_supply import PinPowerSupply

ps = PinPowerSupply()

while True:
    ps.pin_power_listener()
    ps.check_interval_timer()
