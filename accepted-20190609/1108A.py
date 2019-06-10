"""1108A - Two distinct points
http://codeforces.com/problemset/problem/1108/A Here we have two one-dimensional integer ranges that may intersect,
overlap, or coincide with each other.  The bounds for each endpoint are between 1 and 10^9 inclusive, but the endpoints
of each range, independently, do not coincide.  In fact we are given l1 < r1, and l2 < r2.  We want two distinct points,
the first in the first range, and the second in the second range.  We also are given that there may be up to 500
queries.  Basically, we want to narrow the 'two' ranges down, then step through and look for two distinct points.
"""
# Problem #    : 1108A
# Created on   : 2019.06.09


def solve():
    l1, r1, l2, r2 = map(int, input().split())

    mx1 = min(r1, max(r1, l2), max(r1, r2))
    mx2 = min(r2, max(r2, l1), max(r2, r1))

    i, j = l1, l2
    for i in range(l1, mx1 + 1):
        for j in range(l2, mx2 + 1):
            if i != j:
                return (i, j)


n = int(input())
for i in range(n):
    print(*solve())
