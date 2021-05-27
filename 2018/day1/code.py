with open("data.txt") as datafl:
    data = datafl.readlines()
    sumof = 0
    for line in data:
        sumof += int(line)
    print(sumof)

import itertools,sys
with open("data.txt") as datafl:
    data = datafl.readlines()
    freq = 0
    freqc = []
    for q in itertools.repeat(data):
        for item in q:
            freq += int(item)
            if freq in freqc:
                print(freq)
                sys.exit()
            freqc.append(freq)
             
