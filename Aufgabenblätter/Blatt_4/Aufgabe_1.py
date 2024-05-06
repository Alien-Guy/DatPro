from math import sin, cos, atan2, hypot, degrees, radians

def polar_nach_kartesisch(radius, winkel_in_grad):
    winkel = radians(winkel_in_grad)
    x = radius * cos(winkel)
    y = radius * sin(winkel)
    werte_kartesisch = (x, y)
    return werte_kartesisch

def kartesisch_nach_polar (x_wert, y_wert):
    r = hypot(x_wert, y_wert)
    phi_in_grad = degrees(atan2(y_wert, x_wert))
    werte_polar = (r, phi_in_grad)
    return werte_polar

# Test: Kartesisch: (8,3); Polar: (8.54400374531753, 20.556045219583467); Korrekt
# Test: Kartesisch: (-7,13); Polar: (14.7648230602334, 118.30075576600638); Korrekt
# Test: Kartesisch: (43,-92); Polar: (101.55294185792945, -64.94902218355712); Korrekt
# Test: Kartesisch: (-18,-35); Polar: (39.35733730830886, -117.21611155730749); Korrekt
# Somit ist nach 4 Tests mit Vorzeichenwechsel davon auszugehen, dass das Programm grundsätzlich funktioniert.