# 486A - Calculating Function
# http://codeforces.com/problemset/problem/486/A

n = int(input())
ans = ((n + 1) // 2) * (-1 if n & 1 else 1)
print(ans)
