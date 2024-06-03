from random import randint

with open ("pq.txt", "w") as file:
    for i in range(500):
        p = randint(1, 1000)
        file.write(str(p) + ", ")
        q = randint(1, 1000)
        file.write(str(q) + "\n")

print(file)
print(p)
print(q)

f = open("pq.txt", "r")
for line in f:
    print(line, end="")