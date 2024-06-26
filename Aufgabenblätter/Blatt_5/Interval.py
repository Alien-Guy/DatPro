class Interval:
    def __init__(self, lowerbound, upperbound): #self = Intervall
        self.lowerbound = lowerbound
        self.upperbound = upperbound
    
    def __repr__(self):
        return f"Interval ({str(self.lowerbound)},{str(self.upperbound)})"
    
    def __str__(self):
        return f"[{self.lowerbound},{self.upperbound}["
    
    def __contains__(self, number):
        if self.lowerbound <= number and self.upperbound > number:
            return True
        else: return False
    
    def set_lowerbound(self, number):
        self.lowerbound = number
    
    def set_upperbound(self, number):
        self.upperbound = number
    
    def clear(self):
        self.lowerbound = None
        self.upperbound = None