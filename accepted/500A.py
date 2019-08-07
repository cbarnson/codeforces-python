# 500A - New Year Transportation
# http://codeforces.com/problemset/problem/500/A


import sys
import threading


def dfs(s, g, vis):
    vis[s] = 1
    for x in g[s]:
        if not vis[x]:
            dfs(x, g, vis)


def main():

    n, t = map(int, input().split())
    arr = [int(x) for x in input().split()]

    vis = [0] * n
    g = [[] for i in range(n)]

    for i, x in enumerate(arr):
        g[i].append(i + x)

    dfs(0, g, vis)
    print('YES' if vis[t - 1] else 'NO')


sys.setrecursionlimit(1 << 30)  # or try 10**6
threading.stack_size(1 << 27)   # or try 10**8
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
