#Aufgabenblatt 9
#Autor: Jonas Niermann; Matr.-Nr.: 7418131

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
        node = self.head
        length = 0
        while node.next != None:
            node = node.next
            length += 1
        return length

    def __contains__(self, key):
        node = self.head
        while node.next != None:
            node = node.next
            if key == node.key:
                return True
        return False

# Hängt (key, value) an die ssl an. Überschreibt den Wert value falls es
# den Schlüssel key bereits gibt
    def store(self, key, value):
        node = self.head
        while node.next != None:
            node = node.next
            if key == node.key:
                node.value = value
                return 0
        node.next = Node(key, value)

# Sucht key in der ssl und gibt den value zurück, löst ansonsten KeyError aus
    def retrieve(self, key):
        node = self.head
        while node.next != None:
            node = node.next
            if key == node.key:
                return node.value
        raise KeyError

# Fügt (key, value) hinter key_loc ein
    def insert(self, key_loc, key, value):
        new_node = Node(key, value)
        if key_loc == None:
            new_node.next = self.head.next
            self.head.next = new_node
            return
        node = self.head
        while node.next != None:
            node = node.next
            if key_loc == node.key:
                new_node.next = node.next
                node.next = new_node
                return
        raise KeyError

# Sucht nach einem Knoten mit key und löscht diesen dann. Löst einen
# KeyError aus, wenn key nicht in ssl ist
    def delete(self, key):
        node = self.head
        while node.next != None:
            if key == node.next.key:
                node.next = node.next.next
                return
            node = node.next
        raise KeyError

# Iterator über die keys, __iter__
    def __iter__(self):
        self.node = self.head
        return self

# Iterator über die keys, __next__
    def __next__(self):
        if self.node.next != None:
            self.node = self.node.next
            current_key = self.node.key
            return current_key
        else:
            raise StopIteration



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
    print("\n")

# Jetzt den Iterator über die keys in d testen
print('Iterator über d testen:')
for key in d:
    value = d.retrieve(key)
    print(f"({key}, {value})")