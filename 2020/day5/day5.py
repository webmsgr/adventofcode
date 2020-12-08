

def get_row(data):
    rowdata = data[:-3]
    rows = list(range(128))
    for char in rowdata:
        if char == "F":
            rows = rows[:(len(rows))//2]
        else:
           rows = rows[(len(rows))//2:]
    return rows[0]
def get_col(data):
    rowdata = data[-3:]
    rows = list(range(8))
    for char in rowdata:
        if char == "L":
            rows = rows[:(len(rows))//2]
        else:
           rows = rows[(len(rows))//2:]
        #print(rows)
        if len(rows) == 1:
            break
    return rows[0]
def seat(data):
    return get_row(data),get_col(data),get_row(data)*8+get_col(data)

d = open("data.txt").read().strip().splitlines()

mx = 0
for item in d:
    mx = max(seat(item)[2],mx)
print(mx)


def find_empty_seats(data):
    out = []
    for _ in range(128):
        tmp = []
        for _ in range(8):
            tmp.append(False)
        out.append(tmp)
    for seata in data:
        x,y,id = seat(seata)
        out[x][y] = True
    for i,row in enumerate(out):
        if False in row:
            if i < 10 or i >= 100:
                pass
            else:
                print(i,row.index(False),i*8+row.index(False))
find_empty_seats(d)