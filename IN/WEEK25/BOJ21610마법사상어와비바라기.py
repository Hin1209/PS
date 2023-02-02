import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

n, m = map(int, input().split())

world = [list(map(int, input().split())) for _ in range(n)]

cloud = deque()
cloud.append((n-1, 0))
cloud.append((n-1, 1))
cloud.append((n-2, 0))
cloud.append((n-2, 1))

for _ in range(m):
    d, s = map(int, input().split())
    d -= 1
    after_move = deque()
    clear = [[0] * n for _ in range(n)]

    while cloud:
        y, x = cloud.popleft()
        ny = (y + s * dy[d]) % n
        nx = (x + s * dx[d]) % n
        after_move.append((ny, nx))
        clear[ny][nx] = 1
        
    while after_move:
        y, x = after_move.popleft()
        world[y][x] += 1
        
    for i in range(n):
        for j in range(n):
            if clear[i][j]:
                cnt = 0
                for k in [1, 3, 5, 7]:
                    ny, nx = i+dy[k], j+dx[k]
                    if 0 <= ny < n and 0 <= nx < n:
                        if world[ny][nx] > 0:
                            cnt += 1
                world[i][j] += cnt
            else:
                if world[i][j] >= 2:
                    cloud.append((i, j))
    
    for y, x in cloud:
        world[y][x] -= 2

total_water = 0
for i in range(n):
    for j in range(n):
        total_water += world[i][j]

print(total_water)