#Aufgabenblatt 7
#Autor: Jonas Niermann; Matr.-Nr.: 7418131

#Das Programm öffnet die in gen_pq.py erstellte Datei "pq.txt", ließt die Zahlenpaare aus
#und speichert die Paare zusammen mit ihrem ggT im neuen Dokument "pqggt.txt" ab.

from ggt import ggt

pq_list = open("pq.txt", "r")
ggt_list = open("pqggt.txt", "w")
for line in pq_list:
    p = int(line.split(",")[0])
    q = int(line.split(",")[-1])
    ggT = ggt(p, q)
    ggt_list.write(str(p) + ", ")
    ggt_list.write(str(q) + ", ")
    ggt_list.write(str(ggT) + "\n")
    

ggt_list.close()
pq_list.close()

#Ab hier nur noch Überprüfung des oberen Programms.

#print(ggt_list)
#print(p)
#print(q)

#f = open("pqggt.txt", "r")
#for line in f:
#    print(line, end="")
#f.close()
