# 58A - Chat room
# http://codeforces.com/problemset/problem/58/A

import re
s = input()
if re.match(r'.*h.*e.*l.*l.*o.*', s):
    print('YES')
else:
    print('NO')
