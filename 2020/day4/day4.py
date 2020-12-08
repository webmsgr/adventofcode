passports = []
import re
validhair = re.compile("#([0-9a-f]){6}")
data = open("data").read().strip().split("\n")
th = ""
for line in data:
    if line == "":
        passports.append(th.strip())
        th = ""
        continue
    th += " {}".format(line)

req = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
good = 0
goodp = []
for passport in passports:
    passport = passport.split(" ")
    passport = {x.split(":")[0]:x.split(":")[1] for x in passport}
    for item in req:
        if not item in passport:
            good -= 1
            break
    else:
        goodp.append(passport)
good = len(goodp)
print(good)
validp = []
for passport in goodp:
    valid = True
    for item in passport:
        if item == "byr":
            value = int(passport[item])
            if value >= 1920 and value <= 2002:
                pass
            else:
                valid = False
        elif item == "iyr":
            value = int(passport[item])
            if value >= 2010 and value <= 2020:
                pass
            else:
                valid = False
        elif item == "eyr":
            value = int(passport[item])
            if value >= 2020 and value <= 2030:
                pass
            else:
                valid = False
        elif item == "hgt":
            iscm = "cm" in passport[item]
            repl = "cm" if iscm else "in"
            value = int(passport[item].replace(repl,""))
            lower = 150 if iscm else 59
            high = 193 if iscm else 76
            if value >= lower and value <= high:
                pass
            else:
                valid = False
        elif item == "hcl":
            if validhair.match(passport[item]):
                pass
            else:
                valid = False
        elif item == "ecl":
            if passport[item] in "amb blu brn gry grn hzl oth".split(" "):
                pass
            else:
                valid = False
        elif item == "pid":
            if len(passport[item]) == 9 and passport[item].isdigit():
                pass
            else:
                valid = False
    if valid:
        validp.append(passport)
print(len(validp))