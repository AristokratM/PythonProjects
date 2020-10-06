import random

res = ""
sym = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
for i in range(8):
    line = "          dw"
    for j in range(8):
        word = " 0"
        for k in range(4):
            rand = random.randint(0, len(sym)-1)
            word += sym[rand]
        line += word + "h"
        if j < 7:
            line += ','
    res += line + "\n"
print(res)
