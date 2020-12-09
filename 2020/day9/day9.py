

def tryit(data,pos,sumr):
    addto = data[pos]
    data = data[pos-sumr:pos]
    for num1 in data:
        for num2 in data:
            if num1 + num2 == addto:
                return True
    return False

tdata = list(map(int,"""35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""".splitlines()))

rdata = list(map(int,open("data.txt").read().strip().splitlines()))

def doit(data,preamble,lst):
    for i,item in enumerate(data[preamble+1:]):
        if not tryit(data,i+preamble+1,lst):
            return item
print("test1",doit(tdata,5,5))
print("part1",doit(rdata,25,25))


def findit(data,addto,leng):
    queue = data[:leng]
    data = data[leng:]
    if sum(queue) == addto:
        return queue
    try:
        while sum(queue) != addto:
            queue.pop(0)
            queue.append(data.pop(0))
    except IndexError:
        return None
    return queue
def part2(data,preamble,lst):
    addto = doit(data,preamble,lst)
    for i in range(2,250000):
        d = findit(data,addto,i)
        if d is None:
            continue
        else:
            return max(d)+min(d)

print("part2test:",part2(tdata,5,5))
print("part2:",part2(rdata,25,25))