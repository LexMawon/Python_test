'''*** s1 = [[8, 9, 10], [3, 4, 5], [11, 12, 13]]
for i in s1:
    for j in i:
        print(j, end=' ')
    print()'''

s1 = [[8, 9, 10], [3, 4, 5], [11, 12, 13]]
for i in range(3):
    for j in range(3):
        print(s1[j][i], end=' ')
    print()