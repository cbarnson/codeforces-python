# 479A - Expression
# http://codeforces.com/problemset/problem/479/A

a, b, c = int(input()), int(input()), int(input())
mx = -1
mx = max(mx, a + b + c)
mx = max(mx, a * (b + c))
mx = max(mx, (a + b) * c)
mx = max(mx, a * b * c)
print(mx)
