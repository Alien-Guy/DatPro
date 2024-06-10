from time import sleep
import os

def isDescending(list):
    if not list:
        return True
    previous = list[0]
    for number in list:
        if number > previous:
            return False
        previous = number
    return True


class TowersOfHanoi:
    def __init__(self, N):
        self.N = N
        self.pegs = {"A":[str(i) for i in range(N, 0, -1)], "B":[], "C":[]}

    def __str__(self):
        s = ""
        for i in range(self.N-1, -1, -1):
            try:
                disk_a = self.pegs["A"][i]
            except IndexError:
                disk_a = " "
            try:
                disk_b = self.pegs["B"][i]
            except IndexError:
                disk_b = " "
            try:
                disk_c = self.pegs["C"][i]
            except IndexError:
                disk_c = " "
            line = f"          {disk_a}   {disk_b}   {disk_c}\n"
            s += line 
        s += f"          A   B   C\n"
        return s

    def check(self): # check if Hanoi condition is met
        if not isDescending(self.pegs["A"]):
            raise ValueError
        if not isDescending(self.pegs["B"]):
            raise ValueError
        if not isDescending(self.pegs["C"]):
            raise ValueError

    def show(self):
        os.system('clear')
        print(self)
        sleep(0.5)

    def move(self, source, target):
        disk = self.pegs[source].pop()
        self.pegs[target].append(disk)
        self.show()
        self.check()

    def hanoi(self, n, source, helper, target):
# implement me recursively
        pass

p = TowersOfHanoi(7)
p.show()
p.hanoi(p.N, "A", "B", "C")
