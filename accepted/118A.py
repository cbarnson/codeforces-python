# 118A - String Task
# http://codeforces.com/problemset/problem/118/A

v = 'aoyeui'
s = input().lower()
ans = [f'.{x}' for x in s if x not in v]
print(''.join(ans))
