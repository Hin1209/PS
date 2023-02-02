import sys
import heapq

input = sys.stdin.readline

N = int(input())

board = [[0] * N for _ in range(N)]

for i in range(N):
    tmp = list(map(int, input().split()))

    for j in range(N):
        board[i][j] = tmp[j]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                if board[i][k] == 1 and board[k][j] == 1:
                    board[i][j] = 1

for i in range(N):
    for j in range(N):
        print(board[i][j], end = ' ')
    print()
