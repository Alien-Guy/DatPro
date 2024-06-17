#Programm implementiert die Klasse Dictionary manuell in Python-Code.

class Node:
    def __init__(self, key, value):
        self.next = None
        self.key = key
        self.value = value

    def __str__(self):
        return f"Node[{self.key}]={self.value}"


class Dictionary:
    def __init__(self):
        self.head = Node(None, None)

    def __str__(self):
        node = self.head
        s = "."
        while node.next != None:
            node = node.next
            s += "->"+str(node)
        return s

    def __len__(self):
# Standard-Methode, bitte in den Präsenzübungen implementieren
        pass

    def __contains__(self, key):
# Standard-Methode, bitte in den Präsenzübungen implementieren
        pass

# Hängt (key, value) an die ssl an. Überschreibt den Wert value falls es
# den Schlüssel key bereits gibt
    def store(self, key, value):
# Bitte in den Präsenzübungen implementieren
        pass

# Sucht key in der ssl und gibt den value zurück, löst ansonsten KeyError aus
    def retrieve(self, key):
# Bitte in den Präsenzübungen implementieren
        pass

# Fügt (key, value) hinter key_loc ein
    def insert(self, key_loc, key, value):
# Bitte in den Übungen implementieren
        pass

# Sucht nach einem Knoten mit key und löscht diesen dann. Löst einen
# KeyError aus, wenn key nicht in ssl ist
    def delete(self, key):
# Bitte in den Übungen implementieren
        pass

# Iterator über die keys, __iter__
    def __iter__(self):
# Standard-Methode, bitte in den Übugen implementieren
        pass

# Iterator über die keys, __next__
    def __next__(self):
# Standard-Methode, bitte in den Übungen implementieren
        pass



# Hiermit die Dictionary-Methoden testen...
items = [ ("Käthe", 1910), ("Hans", 1950), ("Hans", 1954),
          ("Lea", 1995), ("Kevin", 2000) ]
d = Dictionary()
print("Leeres Directory:")
print(d)
print(f"len(d) = {len(d)}")
print(f'"Lea" in d: {"Lea" in d}')
try:
    print(f'{d.retrieve("Lea") = }')
except KeyError:
    print('d.retrieve("Lea") löst KeyError aus')
try:
    print('d.delete("Lea")')
    d.delete("Lea")
except KeyError:
    print('d.delete("Lea") löst KeyError aus')

for item in items:
    print(f"Speichere {item} in d.")
    d.store(*item)
    print(d)
    print(f"len(d) = {len(d)}")
    print(f'"Lea" in d: {"Lea" in d}')
    try:
        print(f'{d.retrieve("Lea") = }')
    except KeyError:
        print('d.retrieve("Lea") löst KeyError aus')
    try:
        print('d.delete("Lea")')
        d.delete("Lea")
    except KeyError:
        print('d.delete("Lea") löst KeyError aus')

# Jetzt den Iterator über die keys in d testen
print('Iterator über d testen:')
for key in d:
    value = d.retrieve(key)
    print(f"({key}, {value})")
