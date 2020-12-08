def visit(arr,x,y):
    key = "{}:{}".format(x,y)
    if key in arr:
        arr[key] += 1
    else:
        arr[key] = 1
    return arr

def santa(code):
    x,y = 0,0
    visited = visit({},0,0)
    for letter in code:
        if letter == "^":
            y += 1
        elif letter == "v":
            y -= 1
        elif letter == ">":
            x += 1
        elif letter == "<":
            x -= 1
        visited = visit(visited,x,y)
    return len(visited)

with open("data.txt") as fl:
    data = fl.read()
    print(santa(data))