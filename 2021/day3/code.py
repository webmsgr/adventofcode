with open("data.txt","r") as fl:
    fline = fl.readline().strip()
    data = []
    for i in fline:
        data.append([i])
    for line in fl.readlines():
        for tn,i in enumerate(line.strip()):
            data[tn].append(i)
getbit = lambda x: "1" if x.count("1") > x.count("0") else "0"
notb = lambda x: 0 if int(x) else 1
bits = [getbit(x) for x in data]
gamma = int("".join(bits),2)
epsilon = int("".join([str(notb(x)) for x in bits]),2)
print(gamma,epsilon,"pt1:",gamma*epsilon)

# oh god part 2
with open("data.txt") as fl:
    data2 = [x.strip() for x in fl.readlines()]