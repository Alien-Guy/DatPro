#Aufgabenblatt 5
#Autor: Jonas Niermann; Matr.-Nr.: 7418131

#Erstellt eine Klasse Intervals, die mehrere, rechtsoffene Intervalle aufnehmen kann.
#Intervalle müssen von rechts nach links angegeben werden.
#Erben von der Klasse Interval wäre nicht hilfreich, da beide Klassen unterschiedliche Datentypen verwenden.

class Intervals:
    def __init__(self):
        self.list_of_intervals = []
    
    def __str__(self):
        for i in range(len(self.list_of_intervals)):
            return f"[{self.list_of_intervals[i][0]}, {self.list_of_intervals[i][1]}["
    
    def __contains__(self, number):
        for i in range(len(self.list_of_intervals)):
            if self.list_of_intervals[i][0] <= number and self.list_of_intervals[i][0] > number:
                return True
            break
        return False
    
    def add (self, eingabe):
        """Das Intervall darf nur aus 2 Zahlen bestehen, es muss als Tupel mit Klammern übergeben werden und von links nach rechts aufsteigend geordnet sein."""
        if type(eingabe) == tuple and len(eingabe) == 2 and eingabe[0] < eingabe[1]:
            self.list_of_intervals.append(eingabe)
    
    def clear(self):
        self.list_of_intervals = []

    def __iter__(self):
        self.counter = 0
    
    def __next__(self):
        if self.counter < len(self.list_of_intervals): self.counter += 1