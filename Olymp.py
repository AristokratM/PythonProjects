n = int(input())
k = 1
s = 1
for i in range(2, n +1, 2):
    s += (i - 1) ** 2 * k * i
print(s)