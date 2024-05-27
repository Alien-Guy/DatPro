from blankintervals import BlankIntervals

inpt = [ (0.1, 1), (0.1, 1), (0.2, 0), (0.3, 0), (0.4, 1),
         (0.5, 1), (0.6, 0), (0.7, 0), (0.8, 0), (0.9, 0),
         (1.0, 1), (1.1, 0), (1.2, 1) ]

blankintervals = BlankIntervals()
print(blankintervals)

for point in inpt:
    blankintervals.input(point)
print(blankintervals)

print("Expect: [0.2, 0.4[ [0.6, 1.0[ [1.1, 1.2[")
intervals = blankintervals.get_intervals()
print("        ", end="")
for interval in intervals:
    print(interval, end="")
print()
