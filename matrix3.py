n = int(input())
a = [[0] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        if (j % 2 != 0 or i % 2 != 0) and not (j % 2 != 0 and i % 2 != 0):
            a[i][j] = 1
if (n % 2 != 0):
    for i in range(n):
        for j in range(n):
            a[i][j] = 1 - a[i][j]
for i in a:
    print(i)
