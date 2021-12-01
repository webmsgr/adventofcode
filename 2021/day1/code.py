with open("data.txt","r") as fl:
    data = list(map(int,fl.read().split("\n")))
inc = 0
for num,line in enumerate(data):
    if num == 0:
        continue
    if data[num-1] < line:
        inc += 1
print(inc)

def get_sliding_window(winid,data):
    return data[winid:winid+3]
e = []
for i in range(0,len(data)-2):
    e.append(sum(get_sliding_window(i,data)))
inc = 0
for num,line in enumerate(e):
    if num == 0:
        continue
    if e[num-1] < line:
        inc += 1
print(inc)