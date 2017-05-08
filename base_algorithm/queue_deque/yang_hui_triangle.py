from collections import deque


def yanghui(k):
    q = deque([1])
    for i in range(k):
        for _ in range(i):
            q.append(q.popleft() + q[0])
        q.append(1)
    return list(q)


for x in range(7):
    print(yanghui(x))

# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
