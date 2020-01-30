a = int(input())
b = int(input())
s = 0
for i in range(a, b+1):
    if i % 3 == 0:
        i = i / 3
        print(i)