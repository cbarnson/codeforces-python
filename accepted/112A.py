# 112A - Petya and Strings
# http://codeforces.com/problemset/problem/112/A

a, b = input().lower(), input().lower()
print(-1 if a < b else (1 if a > b else 0))
