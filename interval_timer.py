from microbit import running_time

class IntervalTimer:
    def __init__(self):
        self.start_time = None
        # intervals in minutes
        self.intervals = [1, 60, 120, 240, 480, 960, 1920]

        # default to 4 hours off
        self.current_interval_index = 3

        # pump will stay on for the duration in minutes
        self.power_on_duration = 30

        self.interval = self.intervals[self.current_interval_index]
        self.interval = self._minutes_to_millis(self.intervals[self.current_interval_index])
    
    def _minutes_to_millis(self, minutes) -> int:
        return minutes * 60 * 1000

    def _millis_to_minutes(self, millis) -> int:
        return millis // (1000 * 60)

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
        self.interval = self._minutes_to_millis(self.intervals[self.current_interval_index])
        return self._millis_to_minutes(self.interval)
    
    def update_pump_interval(self, power_status: int) -> int:
        if power_status == 1:
            self.interval = self._minutes_to_millis(self.power_on_duration)
        else:
            self.interval = self._minutes_to_millis(self.intervals[self.current_interval_index])
        return self._millis_to_minutes(self.interval)