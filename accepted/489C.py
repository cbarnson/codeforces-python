# 489C - Given Length and Sum of Digits...
# http://codeforces.com/problemset/problem/489/C

m, s = map(int, input().split())
if s == 0:
    print('0 0\n' if m == 1 else '-1 -1\n')
    exit()

a = '9' * (s // 9)

if s % 9:
    a += f'{s % 9}'

if len(a) > m:
    print('-1 -1\n')
    exit()

# Keep a copy before we start changing things in 'a'
max_ans = a

# Min
while len(a) < m:
    a = a[:-1] + f'{int(a[-1]) - 1}'
    while len(a) < (m - 1):
        a += '0'
    a += '1'

# Reverse the string
# Slicing syntax is a[start_pos:end_pos:step], start_pos default 0, end_pos
# default N-1, step default 1. But you can do a[::-1] to copy it in reverse,
# pretty cool!
min_ans = a[::-1]

# Max
while len(max_ans) < m:
    max_ans += '0'

# Print solution
print(f'{min_ans} {max_ans}')
