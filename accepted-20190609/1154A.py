"""1154A - Restoring Three Numbers
https://codeforces.com/problemset/problem/1154/A In this problem, notice that a + b + c is going to be the maximum of
the given 4 numbers.  For each of the other 3 numbers, subtracting it from the maximum value gives you one of the
desired a, b, or c.  The answer cares not about the order of a, b, and c, all of which are positive integers (and (a + b
+ c) - (a + b + c) = 0, so that's easy to identify).
"""
# Problem #    : 1154A
# Created on   : 2019.06.09

arr = [int(val) for val in input().split()]
hi = max(arr)
for x in arr:
    if hi - x > 0:
        print(hi - x, end=' ')
