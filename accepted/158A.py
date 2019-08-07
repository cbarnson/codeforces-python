# 158A - Next Round
# http://codeforces.com/problemset/problem/158/A

n, k = map(int, input().split())
arr = [int(x) for x in input().split()]
next_round = [x for x in arr if (x > 0 and x >= arr[k - 1])]
print(len(next_round))
