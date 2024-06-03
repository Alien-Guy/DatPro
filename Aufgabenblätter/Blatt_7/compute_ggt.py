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

#print(ggt_list)
#print(p)
#print(q)

#f = open("pqggt.txt", "r")
#for line in f:
#    print(line, end="")
#f.close()