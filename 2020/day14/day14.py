import copy
def numto36(num):
    return bin(num).replace("0b","").zfill(36)
def bin36tonum(bin36):
    return int(bin36,2)
def domask(mask,num):
    out = ""
    num = numto36(num)
    for c,item in enumerate(mask):
        if item == "X":
            out += num[c]
        else:
            out += item
    return bin36tonum(out)

class Memory:
    def __init__(self):
        self.mem = {}
        self.mask = ""
    def set(self,spot,value):
        self.mem[spot] = domask(self.mask,value)
    def get(self,spot):
        if spot in self.mem.keys():
            return self.mem[spot]
        else:
            return 0
    def sum(self):
        return sum([self.mem[x] for x in self.mem])
    def set_mask(self,mask):
        self.mask = mask
class MemoryV2:
    def __init__(self):
        self.mem = {}
        self.mask = ""
    def set(self,spot,value):
        for addr in self.maskmemory(spot):
            self.mem[addr] = value
    def get(self,spot):
        if spot in self.mem.keys():
            return self.mem[spot]
        else:
            return 0
    def sum(self):
        return sum([self.mem[x] for x in self.mem])
    def set_mask(self,mask):
        self.mask = mask
    def maskmemory(self,addr):
        addr = self.domask(addr)
        out = []
        this = None
        if not "X" in addr:
            return [addr]
        else:
            end = int("1"*addr.count("X"),2)
            for i in range(end+1):
                t = bin(i).replace("0b","").zfill(addr.count("X"))
                this = copy.copy(addr)
                for item in t:
                    this = this.replace("X",item,1)
                out.append(this)
        return out

    def domask(self,num):
        out = ""
        mask = self.mask
        num = numto36(int(num))
        for c,item in enumerate(mask):
            if item == "0":
                out += num[c]
            elif item == "X":
                out += "X"
            else:
                out += "1"
        return out
def run(prog,memobj):
    mask = ""
    mem = memobj()
    for line in prog:
        if line.startswith("mask = "):
            mem.set_mask(line.replace("mask = ",""))
        elif line.startswith("mem"):
            bef,val = line.split(" = ")
            mems = bef.replace("mem[","").replace("]","")
            val = int(val)
            mem.set(mems,val)
    return mem.sum()
prog = open("data.txt").read().splitlines()
print("part1",run(prog,Memory))
print("part2",run(prog,MemoryV2))