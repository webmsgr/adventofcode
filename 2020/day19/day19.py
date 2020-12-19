import re


def makeregex(ruleid,ruledata):
    tregex = "("
    trule = ruledata[ruleid]
    for item in trule.split(" "):
        if "\"" in item:
            return "({})".format(item.replace("\"",""))
        elif item == "|":
            tregex += "|"
        else:
            tregex += makeregex(int(item),ruledata)
    return tregex + ")"
def parseRules(rules):
    prules = {}
    for item in rules:
        ruleid, rule = item.split(": ")
        prules[int(ruleid)] = rule
    return re.compile("^" + makeregex(0,prules) + "$")    

data = open("data.txt").read().strip().split("\n\n")
rules = data[0].splitlines()
testr = data[1].splitlines()

r = parseRules(rules)
c = 0
for line in testr:
    if r.match(line):
        c += 1
print(c)