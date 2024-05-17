from Interval import Interval
from Intervals import Intervals

Liste_von_Intervallen = Intervals()
Liste_von_Intervallen.add(Interval(1,2))
Liste_von_Intervallen.add(Interval(3,4))

print(Liste_von_Intervallen)
for interval in Liste_von_Intervallen:
   print(interval)
print(Liste_von_Intervallen.__contains__(4))