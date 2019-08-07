# 339B - Xenia and Ringroad
# http://codeforces.com/problemset/problem/339/B

n, m = map(int, input().split())
arr = [int(x) - 1 for x in input().split()]
p, t = 0, 0

for x in arr:
    if x < p:
        t += n - abs(x - p)
    else:
        t += abs(x - p)
    p = x

print(t)
