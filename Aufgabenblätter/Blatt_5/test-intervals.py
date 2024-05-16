from Interval import Interval
from Intervals import Intervals

intervals = Intervals()
intervals.add( Interval(1, 4) )
intervals.add( Interval(4, 5) )
print(f"Intervals = {intervals}")
for position in range(10):
    print(f"{position} in intervals: {position in intervals}")
print()

intervals.clear()
intervals.add( Interval(1, 4) )
intervals.add( Interval(2, 3) )
print(f"Intervals = {intervals}")
for position in range(10):
    print(f"{position} in intervals: {position in intervals}")
print()

intervals.clear()
intervals.add( Interval(1, 3) )
intervals.add( Interval(2, 6) )
intervals.add( Interval(8, 10) )
intervals.add( Interval(15, 18) )
print(f"Intervals = {intervals}")
# test iterator:
for interval in intervals:
    print(f"intervals contains the following interval: {interval}")
for position in range(20):
    print(f"{position} in intervals: {position in intervals}")
print()


intervals.clear()
intervals.add( Interval(1, 2) )
intervals.add( Interval(3, 4) )
intervals.add( Interval(5, 6) )
intervals.add( Interval(7, 8) )
print(f"Intervals = {intervals}")
for position in range(10):
    print(f"{position} in intervals: {position in intervals}")
print()
