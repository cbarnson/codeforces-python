# 520B - Two Buttons
# http://codeforces.com/problemset/problem/520/B
import queue

max_n = 10**4 * 2 + 1


def bfs(n, m):
    D = [-1] * max_n
    D[n] = 0
    Q = queue.Queue()
    Q.put(n)
    while not Q.empty():
        u = Q.get()
        x, y = u - 1, u * 2
        if x < 0 or y > max_n:
            continue

        for i in [x, y]:
            if D[i] == -1:
                D[i] = D[u] + 1
                Q.put(i)

    return D[m]


n, m = map(int, input().split())
print(bfs(n, m))
