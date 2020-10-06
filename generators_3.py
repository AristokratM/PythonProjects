def gen1(s):
    for i in s:
        yield i


def gen2(n):
    a = 0
    while True:
        a += n
        yield a
        print("Ha")


g1 = gen1('Oleh')
g2 = gen2(5)
print(next(g2))
tasks = [g1, g2]
while tasks:
    task = tasks.pop(0)
    try:
        print(next(task))
        tasks.append(task)
    except StopIteration:
        pass
