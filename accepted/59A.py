# 59A - Word
# http://codeforces.com/problemset/problem/59/A

s = input()
c = 0
for x in s:
    if x.isupper():
        c += 1

if c > len(s) // 2:
    s = s.upper()
else:
    s = s.lower()

print(s)