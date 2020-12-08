
def calc(code):
    l,w,h = list(map(int,code.split("x")))
    sides = [l*w,w*h,h*l]
    nslides = []
    slack = min(sides)
    for x in sides:
        nslides.append(2*x)
    return sum(nslides+[slack])

def ribben(code):
    l,w,h = list(map(int,code.split("x")))
    sides = sum([min(l,w),min(w,h),min(w,h),min(h,l)])
    extra = l*w*h
    return sides+extra
with open("data.txt") as fl:
    data = fl.read().strip().split("\n")
    print(sum([calc(x) for x in data]))
    print(ribben("2x3x4"))
    print(ribben("1x1x10"))
    print(sum([ribben(x) for x in data]))