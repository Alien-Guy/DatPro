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
        pass

    def transition_to_state(self, new_state, position):
        if new_state == 0:
            self.interval.set_lowerbound(position)
            self.state = new_state
        else:
            self.interval.set_upperbound(position)
            commit_interval()
        pass

    def input(self, coord):
        if self.state == 1:
            if coord[1] == 0.0:
                transition_to_state(0, coord[0])
            else: pass
        else:
            if coord[1] == 0.0:
                pass
            else: transistion_to_state(1, coord[0])
        pass

    def get_intervals(self):
        self.inhalt = "[ "
        for i in range(len(self.list_of_intervals)):
            self.inhalt += f"[{self.list_of_intervals[i][0]}, {self.list_of_intervals[i][1]}[, "
        self.inhalt += "]"
        return self.inhalt