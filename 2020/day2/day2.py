import re
passwordregex = re.compile("([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)$")
inp = open("data.txt").read().strip().split("\n")
def isvalid1(password):
    #print(password)
    matches = passwordregex.match(password)
    mini = int(matches[1])
    maxi = int(matches[2])
    char = matches[3]
    passw = matches[4]
    count = passw.count(char)
    if count >= mini and count <= maxi:
        return True
    else:
        return False

def countpasswords1(passwords):
    c = 0
    for password in passwords:
        c += 1 if isvalid1(password) else 0
    return c
print("part 1:",countpasswords1(inp))

def isvalid2(password):
    #print(password)
    matches = passwordregex.match(password)
    firstspot = int(matches[1])
    secondspot = int(matches[2])
    char = matches[3]
    passw = matches[4]
    c1 = passw[firstspot-1] == char
    c2 = passw[secondspot-1] == char
    count = 0
    if c1:
        count += 1
    if c2:
        count += 1
    return count == 1
    
def countpasswords2(passwords):
    c = 0
    for password in passwords:
        c += 1 if isvalid2(password) else 0
    return c

print("Part 2:",countpasswords2(inp))