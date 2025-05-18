def printArray(s, r, d):
    result = []
    for i in range(1, d + 1):
        result += [s[i]] * r[i]
    print(result)


def partitions_1(n):
    s = [0] * (n * 2)
    r = [0] * (n * 2)
    d = 1
    s[1] = n
    r[1] = 1
    d = 1
    printArray(s, r, d)
    while s[1] > 1:
        sum_1 = 0
        while s[d] == 1:
            sum_1 += r[d]
            d -= 1
        sum_1 += s[d]
        r[d] -= 1
        l = s[d] - 1
        if r[d] > 0:
            d += 1
        s[d] = l
        r[d] = sum_1 // l
        l = sum_1 % l
        for j in range(1, r[d] + 1):
            s[d + j] = l
            r[d + j] = 1
        if l != 0:
            d += 1
            s[d] = l
            r[d] = 1

        printArray(s, r, d)

print('All Unique Partitions of 3')
partitions_1(3)

print('All Unique Partitions of 4')
partitions_1(4)
print('All Unique Partitions of 6')
partitions_1(6)

