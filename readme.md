# Install
- Acquire a micro:bit
- Clone this repository
- Open the repository in Visual Code and install the plugin -> **micro:bit Python**
- View the main.py page
- Press CRTL-SHIFT-P to view plugin options
- Click "micro:bit-python: MicroPython environment on the micro:bit
- Wait for process to complete
- Click "micro:bit-python: Flash sketch on the micro:bit
- Wait for process to complete

# Run
- Plug in the micro:bit
- Press buttons A and B at the same time to enter Settings mode
- Optional: change the duration the pump is off by pressing button B (default set to 4 hours)
- With one hand, touch the GND and a pin, e.g. pin0 (this will set pin 0 as the digital out pin)
- Press buttons A and B to set the pin and enter Power mode

The pump and timer will turn on, and the system is running

# Demo
[micro:bit hydroponic system project demo](https://www.youtube.com/watch?v=rj4i-KYhMBo)


# Documentation

## main.py
This module represents the main entry point of the Microbit Pin Controller application for the Hydroponic System Project.
It uses a while loop to continuously check for button presses and toggles modes or pin power based on those inputs.
The `main()` function serves as the entry point of the program. It initializes an instance of the `MicrobitPinController` class,
and enters an infinite loop where it checks for button presses and performs appropriate actions based on the current mode.

### Configuration
If both buttons A and B are pressed simultaneously, the function toggles between settings and power modes using the `toggle_mode()` method of the `MicrobitPinController` instance.

While in settings mode:
    - Pressing Button A will set the pin to the minimum value detected among all pins using the `set_pin_to_minimum_value()` method.
    - Pressing Button B will update the interval timer for the pump using the `update_interval_timer()` method.

While in power mode:
    - Pressing Button B will toggle the power of the pump using the `toggle_pump_power()` method.

## status_display.py
A class used to represent a status display on the microbit.

### Attributes
----------
`status : dict`
    a dictionary where keys are integer power status codes and values are corresponding Image objects from the microbit library.

`settings_image : Image`
    an image representing the settings icon to be displayed on the microbit.

### Methods
-------
`display_pin_status(pin_number: int, power_status: int) -> None`:
    Displays the Power status for a specific pin number on the microbit using the pin number followed by an arrow up for "on" or arrow down for "off".

`display_settings() -> None`:
    Displays the settings image on the microbit.

`display_start() -> None`:
    Simulates a startup sequence on the microbit LED panel by cycling through a solid line moving upward.

## interval_timer.py
A class used to represent a timer with intervals and power on durations.

### Attributes
----------
`start_time : int or None`
    The time when the timer was started. It is set to None if the timer is stopped.

`intervals : list[int]`
    A list of predefined interval values in minutes.

`current_interval_index : int`
    The index of the current interval value in `intervals`.

`power_on_duration : int`
    The duration for which the pump should stay on in minutes when it's turned on.

`interval : int`
    The current interval value in milliseconds.

### Methods
-------
`_minutes_to_millis(minutes: int) -> int`:
    Converts a time duration from minutes to milliseconds.

`_millis_to_minutes(millis: int) -> int`:
    Converts a time duration from milliseconds to minutes.

`reset() -> None`:
    Resets the timer by setting `start_time` to the current running time.

`elapsed() -> int`:
    Returns the time that has passed since the timer was started in milliseconds.

`stop() -> None`:
    Stops the timer by setting `start_time` to None.

`is_timer_expired() -> bool`:
    Checks if the timer has expired by comparing the elapsed time with the current interval value.

`change_interval() -> int`:
    Changes the current interval value to the next one in `intervals`. Returns the new interval value in minutes.

`update_pump_interval(power_status: int) -> int`:
    Updates the current interval value based on the power status of the pump. Returns the new interval value in minutes.

## microbit_pin_controller.py
A class used to control the pins of the microbit.

### Attributes
----------
`pins : list`
    A list of pins controlled by the microbit.
`_pin : Pin`
    The current pin in operation.
`mode : int`
    The current mode of operation.
`power_status : int`
    The current power status of the pin.
`run_count : int`
    The number of times the pump has turned on.
`timer : IntervalTimer`
    An interval timer object for scheduling tasks.

### Methods
-------
`_get_pin_index() -> int`:
    Returns the index of the current pin in the pins list.

`set_pin_to_minimum_value()`:
    Sets the current pin to the one with the minimum analog value.

`set_pin(pin)`:
    Sets the current pin and displays its index.

`set_pin_power(pin, power_status: int)`:
    Sets the power status of a pin.

`reset_pins() -> None`:
    Resets all pins to the off state.

`toggle_mode() -> None`:
    Toggles between settings and power modes.

`update_interval_timer()`:
    Updates the interval timer and displays the new interval.

`timer_expired_handler() -> None`:
    Handles the event when the timer expires.

`update_pump_interval(power_status: int) -> None`:
    Updates the pump interval based on the power status and displays the new interval.

`toggle_pump_power() -> None`:
    Toggles the power of the pump and updates the display accordingly.