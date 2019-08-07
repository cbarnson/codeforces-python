"""996A - Hit the Lottery
https://codeforces.com/problemset/problem/996/A
Here, all you need to do is start from the larger denominations first, and work your way down.  By doing this, we ensure
we'll end up with the smallest possible number of bills.
"""
# Problem #    : 996A
# Created on   : 2019.06.09

n = int(input())
denom = [1, 5, 10, 20, 100]
denom.reverse()
c = 0

for x in denom:
    if n >= x:
        num = n // x
        n = n - (num * x)
        c += num

print(c)
