# 1A - Theatre Square
# http://codeforces.com/problemset/problem/1/A

n, m, a = map(int, input().split())
t = ((n // a) + (1 if n % a != 0 else 0)) * ((m // a) + (1 if m % a != 0 else 0))
print(t)
