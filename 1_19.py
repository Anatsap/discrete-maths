def print_partition(block, n):
    group = {}
    for i in range(1, n + 1):
        key = block[i]
        if key not in group:
            group[key] = []
        group[key].append(i)
    for key in group:
        print("{", *group[key], "}", end=" ")
    print()




def partitionss(n):
    block = [0] * (n * 2)
    forward = [0] * (n * 2)
    next_el = [0] * (n * 2)
    past = [0] * (n * 2)
    for i in range(1, n + 1):
        block[i] = 1
        forward[i] = True
    next_el[1] = 0
    print_partition(block, n)
    j = n
    while j > 1:
        k = block[j]
        if forward[j]:
            if next_el[k] == 0:
                next_el[k] = j
                past[j] = k
                next_el[j] = 0
            if next_el[k] > j:
                past[j] = k
                next_el[j] = next_el[k]
                past[next_el[j]] = j
                next_el[k] = j
            block[j] = next_el[k]
        else:
            block[j] = past[k]
            if k == j:
                if next_el[k] == 0:
                    next_el[past[k]] = 0
                else:
                    next_el[past[k]] = next_el[k]
                    past[next_el[k]] = past[k]
        print_partition(block, n)
        j = n
        while (j > 1) and (forward[j] and (block[j] == j)) or (not forward[j] and (block[j] == 1)):
            forward[j] = not forward[j]
            j -= 1

if __name__ == "__main__":
    print("All Unique Partitions of 3:")
    partitionss(4)

