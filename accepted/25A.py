# 25A - IQ test
# http://codeforces.com/problemset/problem/25/A

n = int(input())
arr = [int(x) for x in input().split()]

odd_count = sum(x & 1 for x in arr)
for i, v in enumerate(arr):
    if (odd_count != 1 and ~v & 1) or (odd_count == 1 and v & 1):
        print(i + 1)
        exit()
