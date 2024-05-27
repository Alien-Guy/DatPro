from interval import Interval

class BlankIntervals:
    def __init__(self):
        self.state = 1
        self.interval = Interval(None, None)
        self.intervals = []

    def __str__(self):
        s = f"State: {self.state}, interval: {self.interval},"
        if len(self.intervals) > 0:
            s+= " intervals: "
            for interval in self.intervals:
                s += f"{interval} "
        else:
            s += " (None)"
        return s

    def commit_interval(self):
        pass

    def transition_to_state(self, new_state, position):
        pass

    def input(self, coord):
        pass

    def get_intervals(self):
        pass
