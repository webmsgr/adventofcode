from hashlib import md5
scode = "bgvyzdsv".encode()


def tryit(code,zeroamt=5):
    code = str(code).encode()
    hash = md5(scode)
    hash.update(code)
    if hash.hexdigest().startswith("0"*zeroamt):
        return True
    else:
        return False

def infinite():
    i = 0
    while True:
        yield i
        i += 1
for i in infinite():
    if tryit(i,5):
        print(i)
        break
for i in infinite():
    if tryit(i,6):
        print(i)
        break