#Aufgabenblatt 7
#Autor: Jonas Niermann; Matr.-Nr.: 7418131

#Programm erstellt ein Dokument namens "pq.txt", in dem 1000 Paare aus zufällig generierten,
#ganzen Zahlen zwischen 1 und 1000 abgespeichert werden.
#Jedes Paar hat im Dokument eine eigene Zeile und die Zahlen sind durch ein Komma und Leerzeichen getrennt.

from random import randint

with open ("pq.txt", "w") as file:
    for i in range(1000):
        p = randint(1, 1000)
        file.write(str(p) + ", ")
        q = randint(1, 1000)
        file.write(str(q) + "\n")

#Ab hier nur noch Überprüfung des oberen Programms.
        
#print(file)
#print(p)
#print(q)

#f = open("pq.txt", "r")
#for line in f:
#    print(line, end="")
