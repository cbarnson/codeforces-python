"""935A - Fafa and his Company
http://codeforces.com/problemset/problem/935/A In this problem we are asked how many ways we can pick a non-zero number
of leaders such that the remaining employees, after leaders are taken from the total, can each have an equal number of
employees assigned to them. The input bounds are small, 2 <= n <= 10^5, so brute force is possible.  Just take i from 1
to half of n and each time ask, does i go into (n - i) evenly?  If so, increment our counter and continue.
"""
# Problem #    : 935A
# Created on   : 2019.06.09

n = int(input())
ans = 0

for i in range(1, (n // 2) + 1):
    if (n - i) % i == 0:
        ans = ans + 1

print(ans)
