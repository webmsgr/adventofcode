
data = open("data.txt").read().strip().splitlines()
def iterover(inp,xo=3,yo=1):
    x = 0
    y = 0
    while y < len(inp):
        x += xo
        y += yo
        x %= len(inp[0])
        if y < len(inp):
            yield inp[y][x]
def docount(xo,yo):
    return list(iterover(data,xo,yo)).count("#")
def mult(stuff):
    i = stuff.pop(0)
    for x in stuff:
        i *= x
    return i
print(docount(3,1))
print(mult([
    docount(1,1),
    docount(3,1),
    docount(5,1),
    docount(7,1),
    docount(1,2)
]))