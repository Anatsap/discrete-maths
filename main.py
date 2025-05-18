def printArray(s, start, end):
    for i in range(start, end + 1):
        print(s[i], end=" ")
    print()

def partitions(n):
    s = [0] * (n + 1)
    d = 1
    s[1] = n

    while True:
        printArray(s, 1, d)

        sum_1 = 0
        while d >= 0 and s[d] == 1:
            sum_1 += s[d]
            d -= 1

        if d == 0:
            return

        s[d] -= 1
        sum_1 += 1
        q = sum_1 // s[d]
        r = sum_1 % s[d]

        for j in range(1, q + 1):
            s[d + j] = s[d]

        d = d + q

        if r != 0:
            d += 1
            s[d] = r


print('All Unique Partitions of 5')
partitions(5)

print('All Unique Partitions of 3')
partitions(3)

print('All Unique Partitions of 4')
partitions(4)




