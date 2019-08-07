# 474B - Worms
# http://codeforces.com/problemset/problem/474/B

# statistics
# time  : 560 ms
# memory: 13.67 MB
n = int(input())
a = [int(x) for x in input().split()]
lookup = []
group_no = 0
for x in a:
    group_no += 1
    for i in range(x):
        lookup.append(group_no)

m = int(input())
b = [int(x) for x in input().split()]
for x in b:
    print(lookup[x - 1])
