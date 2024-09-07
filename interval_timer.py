from microbit import running_time

millis_in_second = 1000
seconds_in_minute = 60
minute_in_hour = 60

class IntervalTimer:
    def __init__(self):
        self.start_time = None
        # intervals in hours
        self.intervals = [1, 2, 4, 8, 16, 24]
        self.current_interval_index = 0
        self.interval = self._hours_to_millis(self.intervals[self.current_interval_index])

    def _hours_to_millis(self, hour) -> int:
        return hour * minute_in_hour * seconds_in_minute * millis_in_second
    
    def _millis_to_hours(self, millis) -> int:
        return millis // (millis_in_second * seconds_in_minute * minute_in_hour)

    def reset(self):
        self.start_time = running_time()

    def elapsed(self) -> int:
        return running_time() - self.start_time
    
    def stop(self) -> None:
        self.start_time = None
    
    def is_timer_expired(self) -> bool:
        return self.start_time is not None and self.interval - self.elapsed() <= 0

    def change_interval(self) -> int:
        self.current_interval_index = (self.current_interval_index + 1) % len(self.intervals)
        self.interval = self._hours_to_millis(self.intervals[self.current_interval_index])
        return self._millis_to_hours(self.interval)