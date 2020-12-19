import multiprocessing as mp
from functools import partial
def busAt(buses,timestamp):
    print("======")
    for bus in buses:
        print("Bus {} returning in: {} (timestamp: {})".format(bus,timestamp%bus,timestamp))
        if doesbusleaveat(bus,timestamp):
            yield bus

def inf(start,step):
    i = start
    while True:
        yield i
        i += step
        
def doesbusleaveat(bus,timestamp):
    if bus == "x":
        return True
    else:
        bus = int(bus)
    return timestamp % bus == 0

def part1(data):
    timestampstart, tbuses = data
    buses = [int(x) for x in tbuses.split(",") if x != "x"]
    timestampstart = int(timestampstart)
    for i in inf(timestampstart,1):
        pl = list(busAt(buses,i))
        if pl != []:
            return pl[0]*(i-timestampstart)
def matchespart2(buses,i):
    if doesbusleaveat(buses[0],i):
        d = ""
        for offset,bus in enumerate(buses):
            d += " ".join(map(str,[i,bus,offset,offset+i,doesbusleaveat(bus,i+offset)])) + "\n"
            if not doesbusleaveat(bus,i+offset):
                break
        else:
            #print("match found!")
            #print(d)
            return True
    return False
def getfromiter(iterable,amt):
    for i in range(amt):
        yield next(iterable)
def part2(data,start=100000000000000):
    _, buses = data
    buses = buses.split(",")
    m = None
    item = None
    qf = partial(matchespart2,buses)
    with mp.Pool() as pl:
        q = []
        has = False
        out = None
        gen = inf(start,len(buses)-1)
        it = pl.imap(qf,gen)
        for m,item in enumerate(it):
            if item:
                #print(m)
                break
    return (len(buses)-1)*m
                        


            
if __name__ == "__main__":
    data = open("data.txt").read().splitlines()
    p1 = part1(data)
    print("part1",p1)
    print("testpart2",part2(["","17,x,13,19"],0))
    print("doing part 2, this may take a while")
    p2 = part2(data)
    print("part1",p1,"part2",p2)
