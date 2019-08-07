# 339A - Helpful Maths
# http://codeforces.com/problemset/problem/339/A

s = input()
arr = [x for x in s if x.isdigit()]
ans = '+'.join(sorted(arr))
print(ans)
