def table1(a):
    sy = [0] * len(a[0])
    mx = 0
    my = 0
    mxy = 0
    dx = 0
    dy = 0
    for i in range(1, len(a)):
        for j in range(1, len(a[0])):
            mxy += a[i][j] * a[i][0] * a[0][j]
            sy[j] += a[i][j]

    for i in range(1, len(a)):
        s = sum(a[i][1:])
        mx += a[i][0] * s
        dx += a[i][0] ** 2 * s
    dx -= mx ** 2
    for j in range(1, len(a[0])):
        my += a[0][j] * sy[j]
        dy += a[0][j] ** 2 * sy[j]
    dy -= my ** 2
    kxy = mxy - mx * my
    rxy = kxy / (dx ** 0.5 * dy ** 0.5)
    print("M(X): ", "{:.4f}".format(mx))
    print("M(Y): ", "{:.4f}".format(my))
    print("M(X,Y): ", "{:.4f}".format(mxy))
    print("K(X,Y): ", "{:.4f}".format(kxy))
    print("D(X): ", "{:.4f}".format(dx))
    print("D(Y): ", "{:.4f}".format(dy))
    print("rxy: ", "{:.4f}".format(rxy))


def XY(list_x, list_y):
    ans = 0
    for i in range(len(list_x)):
        ans += list_x[i] * list_y[i]
    return ans


def square_list(list_x):
    return [i ** 2 for i in list_x]


def B1(list_x, list_y):
    n = len(list_x)
    s_x = sum(list_x)
    return (XY(list_x, list_y) - s_x * sum(list_y) / n) / (sum(square_list(list_x)) - s_x ** 2 / n)


def average(list):
    return  sum(list) / len(list)


def B0(list_x, lixt_y):
    return average(list_y) - B1(list_x, lixt_y) * average(list_x)


def depresion_otsinka(list_x, list_y):
    n = len(list_x)
    b1 = B1(list_x, list_y)
    b0 = B0(list_x, list_y)
    y_otsinka = [b0 + b1 * x for x in list_x]
    s = 0
    for i in range(len(list_y)):
        s += (list_y[i] - y_otsinka[i]) ** 2
    return s, n - 2, s / (n - 2)


def Sxx(list_x):
    return sum(square_list(list_x)) - sum(list_x) ** 2 / len(list_x)


def T0(list_x, list_y):
    return B1(list_x, list_y) / (depresion_otsinka(list_x, list_y)[2] / Sxx(list_x)) ** 0.5


def dispersion(lst):
    a = average(lst)
    b = average(lst) / len(lst)
    return (sum(square_list(lst)) - a * b) / (len(lst) - 1)


def SP(n1, n2, s1, s2):
    return ((n1 - 1) * s1 ** 2 + (n2 -1) ** s2 ** 2) / (n1 + n2 - 2) ** 0.5


if __name__ == '__main__':
    table = [
        ['X\\Y', 1, 2, 4],
        [1, 0.1, 0.2, 0.1],
        [2, 0.05, 0.15, 0.15],
        [3, 0.07, 0.13, 0.05]
    ]
    print(0.1 + 0.2 + 0.1 + 0.05 + 0.15 + 0.15 + 0.07 + 0.13 + 0.05)
    table1(table)
    list_x = [23.1, 32.8, 31.8, 32.0, 30.4, 24, 39.5, 24.2, 52.5, 37.9, 30.5, 25.1, 12.4, 35.1, 31.5, 21.1, 27.6]
    list_y = [10.5, 16.7, 18.2, 17.0, 16.3, 10.5, 23.1, 12.4, 24.9, 22.8, 14.1, 12.9, 8.8, 17.4, 14.9, 10.5, 16.1]
    # print(XY(list_x, list_y))
    # print(sum(list_x), sum(list_y))
    # print(len(list_x))
    # print(sum(square_list(list_x)), sum(list_x) ** 2 / len(list_x))
    # print(B1(list_x, list_y))
    # # table1(table)
    # print(average(list_y), average(list_x))
    # print(B0(list_x, list_y))
    # print(depresion_otsinka(list_x, list_y))
    # print(Sxx(list_x))
    # print(T0(list_x, list_y))
    # print(SP(15, 17, 0.35, 0.4))