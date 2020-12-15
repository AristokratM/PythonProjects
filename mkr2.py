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


if __name__ == '__main__':
    table = [
        ['X\\Y', 1, 2, 4],
        [-1, 0.15, 0.2, 0.14],
        [1, 0.05, 0.1, 0.1],
        [2, 0.06, 0.15, 0.05]
    ]
    table1(table)