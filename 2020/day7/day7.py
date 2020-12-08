od = open("data.txt").read()
def makearr(od):
    od = od.strip().splitlines()
    mdata = {}
    for line in od:
        line = line.split(" contain ")
        bagtype, contains = line
        bagtype = bagtype.replace("bags","").replace("bag","").strip()
        if "no other bags" in contains:
            continue
        contains = [x.strip().replace(".","") for x in contains.split(",")]
        oc = []
        for contained in contains:
            tmp = []
            amt = 0
            for token in contained.split(" "):
                if not token.isnumeric():
                    if not token in ["bag","bags"]:
                        tmp.append(token)
                else:
                    amt = int(token)
            oc.append((" ".join(tmp),amt))
        mdata[bagtype] = oc
    return mdata
def cancontain(bagtype,data):
    o = []
    for key in data:
        dk = data[key]
        for b in dk:
            if b[0] == bagtype:
                o.append(key)
    return o

arr = makearr(od)
#print(arr)
def findallcancontain(d,data):
    
    cc = cancontain(d,data)
    queue = cc
    o = set()
    while queue != []:
        a = queue.pop(0)
        #print("queue len",len(queue),"next",a)
        o.add(a)
        queue += cancontain(a,data)
    return o
#print(cancontain("shiny gold",arr))
print(len(findallcancontain("shiny gold",arr)))


def findcounts(bagtype,data):
    try:
        b = data[bagtype]
    except KeyError:
        #print("no bag: {}".format(bagtype))
        b = []
    count = 0
    #print(bagtype,b)
    for item,c in b:
        #print(item,c)
        count += c
        count += findcounts(item,data)*c
    return count
print(findcounts("shiny gold",arr))