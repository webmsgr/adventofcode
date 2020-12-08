
def do20202(num1,num2):
    return num1 + num2 == 2020
def do20203(num1,num2,num3):
    return num1 + num2 + num3 == 2020


    return out
inp = list(map(int,open("data.txt").read().strip().split("\n")))
done1 = False
print("Solution 1:",end="")
for num1 in inp:
    for num2 in inp:
        if do20202(num1,num2):
            print(num1,"*",num2,"=",num1*num2,)
            done1 = True
            break
    if done1:
        break
print("Solution 2:",end="")
done2 = False
for num1 in inp:
    for num2 in inp:
        for num3 in inp:
            if do20203(num1,num2,num3):
                print(num1,"*",num2,"*",num3,"=",num1*num2*num3,)
                done2 = True
                break
        if done2:
            break
    if done2:
        break