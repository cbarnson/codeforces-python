# 459B - Pashmak and Flowers
# http://codeforces.com/problemset/problem/459/B

# time: 374 ms
# memory: 16.89 MB


def n_choose_k(n, k):
    k = min(k, n - k)
    ans = 1
    for i in range(k):
        ans = ans * (n - i) / (i + 1)
    return ans


n = int(input())
arr = [int(x) for x in input().split()]

mi, mx, mic, mxc = -1, -1, 0, 0
for x in arr:
    mi = x if mi == -1 else min(mi, x)
    mx = x if mx == -1 else max(mx, x)

for x in arr:
    if x == mi:
        mic += 1
    if x == mx:
        mxc += 1

ans = int(mic * mxc) if mi != mx else int(n_choose_k(mic, 2))
print(f'{abs(mx - mi)} {ans}')
