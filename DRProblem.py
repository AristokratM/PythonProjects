import random
a = []
def add_days(n, val):
    for i in range(n):
        a.append(val)

for i in range(12):
    if i < 8:
        add_days(31, i)
    elif i < 12:
        add_days(30, i)
    else:
        add_days(28, i)

ans = 0
m = 500_000
for i in range(m):
    monthes = [0] *12
    k = 0
    c = 0
    for j in range(30):
        b = random.randint(0, 365)
        monthes[a[b]] +=1
    for month in monthes:
        if month == 2:
            k +=1
        elif month == 3:
            c +=1
    if k == 6 and c == 6:
        ans += 1
print(ans, ans / m)
