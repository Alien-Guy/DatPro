from Interval import Interval

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
        self.intervals.append(self.interval)
        self.interval = Interval(None, None)

    def transition_to_state(self, new_state, position):
        if self.state == 1:
            self.interval.set_lowerbound(position)
        else:
            self.interval.set_upperbound(position)
            self.commit_interval()
        self.state = new_state

    def input(self, coord):
        if self.state == 1:
            if coord[1] == 0.0:
                self.transition_to_state(0, coord[0])
        else:
            if coord[1] != 0.0:
                self.transition_to_state(1, coord[0])

    def get_intervals(self):
       return self.intervals       