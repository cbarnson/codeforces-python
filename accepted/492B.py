# 492B - Vanya and Lanterns
# http://codeforces.com/problemset/problem/492/B

F = int(1e9)
n, L = map(int, input().split())
L *= F
arr = [int(x) * F for x in input().split()]
arr.sort()


# Validation function, returns true if light radius 'd' is sufficient to cover
# the whole street.
def f(d):
    x, y = arr[0], arr[-1]
    if x > d or L - y > d:
        return False
    for i in range(n - 1):
        x, y = arr[i], arr[i + 1]
        if y - x > 2 * d:
            return False

    return True


lo = 0
hi = 1 * F
while not f(hi):
    hi *= 2

while hi - lo > 5:
    mid = lo + (hi - lo) // 2
    if f(mid):
        hi = mid
    else:
        lo = mid

while not f(lo):
    lo += 1

print(lo / 1e9)
