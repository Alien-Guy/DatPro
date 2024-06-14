#Aufgabenblatt 7
#Autor: Jonas Niermann; Matr.-Nr.: 7418131

#Programm erstellt die Routine multiindex, die alle Indizes zu denen ein Element in der Liste
#vorkommt ausgibt.

def multiindex(list, element):
    for p in range(len(list)):
        if list[p] == element:
            yield p

# Ab hier Test des Generators
liste = [0,1,0,1,1,1]

for a in multiindex(liste, 1):
    print(a)