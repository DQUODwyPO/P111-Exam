from math import inf


def main():
    a = [4, 7, 2, 18, 3, 8,-7, -5, 21, 0]
    b = [5, 1, 6, 19, 10, 9,-9, -1, 22, -2]
    print(alg(a, b))


def alg(a: list, b: list) -> list:
    a.sort()
    b.sort()
    a += [inf]
    b += [inf]
    m = abs(a[0] - b[0])
    i = 0
    j = 0
    move = False
    answ2 = []
    while 1:
        while (i + 1) != (len(a) - 1) and abs(a[i + 1] - b[j]) < m:
            i += 1
            m = abs(a[i] - b[j])
            move = True
        while (j + 1) != (len(b) - 1) and abs(a[i] - b[j + 1]) < m:
            j += 1
            m = abs(a[i] - b[j])
            move = True

        if not move:
            if abs(a[i] - b[j]) == m:
                answ2.append([a[i], b[j]])
            if a[i] > b[j] and (j + 1) != (len(b) - 1):
                j += 1
                continue
            elif a[i] == b[j] and (j + 1) != (len(b) - 1) and (i + 1) != (len(a) - 1):
                i += 1
                j += 1
                continue
            elif (i + 1) != (len(a) - 1):
                i += 1
                continue
            elif (j + 1) != (len(b) - 1):
                j += 1
                continue
        if i == j and i == (len(a) - 2):
            break
        move = False
    answ = []
    print(a)
    print(b)
    print(answ2)
    for i in range(len(answ2)):
        if abs(answ2[i][0] - answ2[i][1]) == m:
            answ.append([answ2[i][0], answ2[i][1]])
    return answ


if __name__ == '__main__':
    main()
