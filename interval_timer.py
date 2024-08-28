from microbit import running_time, display

millis_in_second = 1000
seconds_in_minute = 60
minute_in_hour = 60

class IntervalTimer:
    def __init__(self):
        self.start_time = running_time()
        # intervals in hours
        self.intervals = [1, 2, 4, 8, 16, 24]
        self.current_interval_index = 0
        self.interval = self.hours_to_millis(self.intervals[self.current_interval_index])

    def hours_to_millis(self, hour) -> int:
        return hour * minute_in_hour * seconds_in_minute * millis_in_second
    
    def millis_to_hours(self, millis) -> int:
        return millis // (millis_in_second * seconds_in_minute * minute_in_hour)

    def reset(self):
        self.start_time = running_time()

    def elapsed(self) -> int:
        return running_time() - self.start_time
    
    def get_remaining_time(self) -> int:
        return self.interval - self.elapsed()
    
    def change_interval(self):
        self.current_interval_index = (self.current_interval_index + 1) % len(self.intervals)
        self.interval = self.hours_to_millis(self.intervals[self.current_interval_index])
        display.scroll("Interval: {} Hour(s)".format(str(self.millis_to_hours(self.interval))))