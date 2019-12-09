# ガウス・ザイテル法
# 3
# 5 1 1 10
# 1 4 1 12
# 2 1 3 13

n = int(input())
A = []
X = [1]*n  # 解初期値
Y = [0]*n
eps = 1e-4
flag = False

for _ in range(n):
    A.append(list(map(int, input().split())))
for k in range(60):
    # 逐次計算
    for i in range(n):
        s = 0
        for j in range(n):
            if i != j:
                s += A[i][j]*X[j]
        Y[i] = (A[i][n] - s) / A[i][i]
    # 誤差集積
    q = 0
    for i in range(n):
        q += abs(X[i]-Y[i])
        X[i] = Y[i]
    # 収束判別
    if q < eps:
        flag = True
        break
if flag:
    for i in range(n):
        print('X = ', X[i])
else:
    print('収束せず.')
    exit()
