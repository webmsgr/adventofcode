

def run(prog):
    prog = prog.strip().splitlines()
    ip = 0
    ac = 0
    uip = []
    while True:
        try:
            exc = prog[ip]
        except IndexError:
            return ac,"term"
        ist,arg = exc.split(" ")
        if ist == "nop":
            pass
        elif ist == "acc":
            ac += int(arg)
        elif ist == "jmp":
            ip += int(arg)-1
        ip += 1
        if ip in uip:
            break
        else:
            uip.append(ip)
    return ac,"inf"
test = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""
d = open("data.txt").read()
print("test1",run(test)[0])
print("part1",run(d)[0])

def repl(base,place,ndata):
    base = base.strip().splitlines()
    ints = base[place]
    _, arg = ints.split(" ")
    nist = "{} {}".format(ndata,arg)
    nbase = []
    for ip,item in enumerate(base):
        if ip == place:
            nbase.append(nist)
        else:
            nbase.append(item)
    return "\n".join(nbase)


def fixprog(data):
    data = data.strip()
    floc = []
    for c,i in enumerate(data.splitlines()):
        if "jmp" in i or "nop" in i:
            floc.append(c)
    for item in floc:
        newinst = "jmp" if "nop" in data.splitlines()[item] else "nop"
        nprog = repl(data,item,newinst)
        r,t = run(nprog)
        if t == "term":
            return r
print("test2",fixprog(test))
print("part2",fixprog(d))