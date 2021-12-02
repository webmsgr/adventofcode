with open("data.txt") as fl:
    data = fl.read().strip().split("\n")
x = 0
y = 0
for line in data:
    print(line, end=" -> ")
    cmd, amt = line.split(" ")
    amt = int(amt)
    if cmd == "down":
        y += amt
    elif cmd == "up":
        y -= amt
    elif cmd == "forward":
        x += amt
    print(x,y,x*y,sep=",")
p1 = x*y
x=0
y=0
aim=0
 
for line in data:
    print(line, end=" -> ")
    cmd, amt = line.split(" ")
    amt = int(amt)
    if cmd == "up":
        aim -= amt
    elif cmd == "down":
        aim += amt
    elif cmd == "forward":
        x += amt
        y += amt*aim
    print(x,y,aim,x*y,sep=",")
p2 = x*y
print(p1,p2)