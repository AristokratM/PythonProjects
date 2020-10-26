def reverse(s1):
    return s1[::-1]


def inv_count(lst):
    if len(lst) <2 :
        return 0
    m = (len(lst) + 1) // 2
    f = inv_count
    left = lst[:m]
    right = lst[m:]
    return f(left) + f(right) + merge(lst, left, right)


def merge(arr, left, right):
    i = j = invNumber = 0
  #  print(arr, left, right)
    while i < len(left) or j < len(right):
        if i == len(left):
            arr[i + j] = right[j]
            j += 1
  #          print("#1")
        elif j == len(right):
            arr[i + j] = left[i]
            i += 1
  #          print("#2")
        elif left[i] <= right[j]:
            arr[i + j] = left[i]
            i += 1
   #         print("#3")
        else:
            arr[i + j] = right[j]
            j += 1
            invNumber += len(left) - i
  #          print("#4")
  #  print(arr)
    return invNumber


n = int(input())
s = input()
a = []
s1 = reverse(s)
d = {}
for i in range(len(s1)):
    d[s1[i]] = d.get(s1[i], [])
    d[s1[i]].append(i)



p =[]

for i in s:
    p.append(d[i].pop(0))
#print(p)

print(inv_count(p))
#print(p)


