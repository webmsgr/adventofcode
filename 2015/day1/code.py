def apartment(data):
    return data.count("(") - data.count(")")

def basement(data):
    pos = 0
    t = 1
    for char in data:
        pos += -1 if char == ")" else 1
        if pos == -1:
            return t
        t += 1

with open("data.txt") as fl:
    data = fl.read()
    print(apartment(data))
    print(basement(data))