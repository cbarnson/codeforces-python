# 50A - Domino piling
# http://codeforces.com/problemset/problem/50/A

m, n = map(int, input().split())
if m == 1 and n == 1:
    print(0)
else:
    print(int(m * n) // 2)
