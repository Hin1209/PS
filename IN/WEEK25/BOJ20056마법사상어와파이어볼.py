import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

n, m, k = map(int, input().split())

world = [[deque() for _ in range(n)] for _ in range(n)]

for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    world[r-1][c-1].append((m, s, d, 1))
    
for i in range(1,k+1):
    for y in range(n):
        for x in range(n):
            while world[y][x]:
                m, s, d, t = world[y][x].popleft()
                if t > i:
                    world[y][x].append((m, s, d, t))
                    break
                ny = (y + s * dy[d]) % n
                nx = (x + s * dx[d]) % n
                world[ny][nx].append((m, s, d, t+1))
    
    for y in range(n):
        for x in range(n):
            even = 0
            odd = 0
            mass = 0
            speed = 0
            cnt = 0
            time = 0
            if len(world[y][x]) > 1:
                while world[y][x]:
                    m, s, d, t = world[y][x].popleft()
                    time = t
                    mass += m
                    speed += s
                    cnt += 1
                    if d % 2 == 0:
                        even += 1
                    else:
                        odd += 1
            if cnt > 1:
                if even > 0 and odd == 0:
                    direction = [0,2,4,6]
                elif even == 0 and odd > 0:
                    direction = [0,2,4,6]
                elif even > 0 and odd > 0:
                    direction = [1,3,5,7]
                mass = mass // 5
                if mass == 0:
                    continue
                speed = speed // cnt
                for next_d in direction:
                    world[y][x].append((mass, speed, next_d, time))

total_mass = 0
for i in range(n):
    for j in range(n):
        while world[i][j]:
            m, s, d, t = world[i][j].popleft()
            total_mass += m
print(total_mass)