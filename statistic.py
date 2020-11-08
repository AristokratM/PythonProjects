def format_input(s, *args):
    k = s
    for arg in args:
        old, new = arg.split("$")
        k = k.replace(old, new)
    return k


def average(lst):
    s = 0
    for i in lst:
        s += i
    return s, s / len(lst)


def dispersion(lst):
    s = 0
    a, b = average(lst)
    for i in lst:
        s += i ** 2
    return (s - a * b) / (len(lst) - 1)


def square_lst(lst):
    return [i ** 2 for i in lst]


def dispersion(lst):
    a, b = average(lst)
    return (sum(square_lst(lst)) - a * b) / (len(lst) - 1)


def sorted_lst(lst):
    return sorted(lst)


def mediana(lst):
    n = len(lst)
    lst1 = sorted_lst(lst)
    return lst1[n//2] if n % 2 == 1 else (lst1[n//2-1] + lst1[n//2])/2


def moda(lst):
    lst1 = sorted_lst(lst)
    current = 0
    ans = 1
    res = []
    prev = lst1[0]-1
    for i in lst1:
        current = current + 1 if i == prev else 1
        if current > ans:
            ans = current
            res = [i]
        elif ans != 1 and current == ans:
            res.append(i)
        prev = i
    return res


def dict_from_lst(lst):
    d = {}
    for i in lst:
        d[i] = d.get(i, 0) + 1
    return d


def print_dict(d):
    for i in sorted_lst(d.keys()):
        print("X {} : {}".format(i, d[i]))


def ni_n(lst):
    n = len(lst)
    d = dict_from_lst(lst)
    lst1 = sorted_lst(d.keys())
    return ["%0.3f" % (d[i] / n) for i in lst1]


def f(lst):
    n = len(lst)
    d = dict_from_lst(lst)
    lst1 = sorted_lst(d.keys())
    f_val = [(d[i] / n) for i in lst1]
    for i in range(1, len(f_val)):
        f_val[i] += f_val[i-1]
    return ["%0.3f" % i for i in f_val]


def print_dispersion(lst):
    a, b = average(lst)
    print(sum(square_lst(lst)))
    print(a*b)
    print(len(lst)-1)
    print(dispersion(lst))
    print(dispersion(lst) ** 0.5)


def lower_quartil(lst):
    lst1 = sorted_lst(lst)
    return mediana(lst1[:len(lst)//2])


def upper_quartil(lst):
    lst1 = sorted_lst(lst)
    return mediana(lst1[len(lst)//2:])


def iqr(lst):
    return upper_quartil(lst)-lower_quartil(lst)


def lower_tail(lst):
    return lower_quartil(lst) - 1.5 * iqr(lst)


def upper_tail(lst):
    return upper_quartil(lst) + 1.5 * iqr(lst)


def lower_not_exclude(lst):
    a = lower_tail(lst)
    lst1 = sorted_lst(lst)
    for i in lst1:
        if i >= a:
            return i


def upper_not_exclude(lst):
    a = upper_tail(lst)
    lst1 = sorted_lst(lst)
    for i in range(len(lst1)):
        if lst1[i] > a:
            return lst1[i-1]


def exluded(lst):
    lb = lower_not_exclude(lst)
    rb = upper_not_exclude(lst)
    ans = []
    for i in sorted_lst(lst):
        if i < lb or i > rb:
            ans.append(i)
    return ans


s = format_input(input())
lst = list(map(float, s.split(" ")))
print(mediana(lst))
print(lower_quartil(lst))
print(upper_quartil(lst))
print(iqr(lst))
print(lower_tail(lst))
print(upper_tail(lst))
print(lower_not_exclude(lst))
print(upper_not_exclude(lst))
print(exluded(lst))
