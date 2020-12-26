t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    ans = [n + 1 - i for i in range(1, n + 1)]
    for i in ans:
        print(i, end=" ")
    print()