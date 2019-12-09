# input
# 3
# 2 1 3 13
# 1 3 2 13
# 3 2 1 10

eps = 1e-5
n = int(input())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))
for i in range(n):
    piv = A[i][i]
    if abs(piv) < eps:
        print('pivot number is too small.')
        exit()
    for j in range(n+1):
        A[i][j] /= piv
    for k in range(n):
        d = A[k][i]
        for j in range(n+1):
            if k != i:
                A[k][j] -= d*A[i][j]
for l in range(n):
    print('x%d' % (l+1), '=', A[l][n])
