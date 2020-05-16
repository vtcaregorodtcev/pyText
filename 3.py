m = int(input())
n = int(input())

k = 0
p = 0

while (k < m and p < n):
    for i in range(p, n):
        print(k, i)

    k += 1

    for i in range(k, m):
        print(i, n-1)

    n -= 1

    if (k < m):

        for i in range(n - 1, (p - 1), -1):
            print(m-1, i)

        m -= 1

    if (p < n):
        for i in range(m - 1, k - 1, -1):
            print(i, p)

        p += 1
