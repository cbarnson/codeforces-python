# 231A - Team
# http://codeforces.com/problemset/problem/231/A

n = int(input())
c = 0
for i in range(n):
    arr = [x for x in input().split() if int(x) == 1]
    if len(arr) >= 2:
        c += 1

print(c)
