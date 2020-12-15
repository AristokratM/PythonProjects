import random


def calc(n, m):
    good_list = [0]*(n+1)  # в i елементі зберігаємо кількість разів коли випало ЦЦГ на i-тий раз
    for i in range(m):  # проводимо дослід m разів
        k = 0  # кількість виконаних підкидань
        state = 0  # 0 - nothing or Г, 1 - Ц, 2 - ЦЦ, 3 - ЦЦГ
        flip = True  # індикатор чи слід підкидати монету
        while flip:
            k += 1
            a = random.randint(0, 1)  # 0 - Г, 1 - Ц
            if state == 2 and a == 0:  # Випало ЦЦГ, отже більше не підкидаємо монету
                state += 1
                flip = False
            elif (state == 2 and a == 1) or a == 0:  # Випало ЦЦЦ, або випала Г, але перед цим не випало ЦЦ отже, переходимо в 0 стан
                state = 0
            else:
                state += 1  # Випало Ц і ми не в 2 стані, отже переходимо або в 1, або в 2, залежно від того, що випадало до того
            if k == n:  # Зробили  n підкидань і не випало ЦЦГ
                flip = False
        if state != 3:
            continue
        good_list[k] += 1
    probability_list = [i / m for i in good_list]
    return probability_list  # в i елементі зберігаємо ймовірність того, що випало ЦЦГ на i-тий раз


def main(n, m):
    probability_list = calc(n, m)
    for i in range(3, len(probability_list)):
        print("Ймовірність того, що ЦЦГ випаде на {} раз дорівнює {}".format(i, probability_list[i]))


if __name__ == '__main__':
    n = 10  # за умовою задачі
    m = 100000  # кількість випробувань
    main(n, m)
