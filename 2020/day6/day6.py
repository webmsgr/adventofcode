
datar = open("data.txt").read().strip().splitlines()
#print(data)

def calc(data):
    datal = []
    tmp = []
    for item in data:
        if item == "":
            #print(tmp)
            datal.append(set("".join(tmp)))
            tmp = []
        else:
            tmp.append(item)
    datal.append(set("".join(tmp)))
    return sum([len(x) for x in datal])

print(calc(datar))

def calcpart2(data):
    datal = []
    tmp = []
    q = "abcdefghijklmnopqrstuvwxyz"
    for item in data:
        if item == "":
            #print(tmp)
            datal.append(tmp)
            tmp = []
        else:
            tmp.append(item)
    datal.append(tmp)
    o = []
    for group in datal:
        if group == []:
            continue
        alla = 0
        for letter in q:
            if all([letter in x for x in group]):
                alla += 1
                #print(group,letter)
        #print(alla)
        o.append(alla)
    #print(o)
    return sum(o)
print(calcpart2(datar))