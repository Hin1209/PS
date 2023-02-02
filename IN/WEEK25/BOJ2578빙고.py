import sys

input = sys.stdin.readline

my_num = [list(map(int, input().split())) for _ in range(5)]
call_num = [list(map(int, input().split())) for _ in range(5)]

row = [0] * 5
col = [0] * 5
cross = [0, 0]


def make_bingo():
    bingo = 0
    for i in range(5):
        for j in range(5):
            n = call_num[i][j]
            for y in range(5):
                for x in range(5):
                    if my_num[y][x] == n:
                        row[y] += 1
                        col[x] += 1
                        if y == x:
                            cross[0] += 1
                            if cross[0] == 5:
                                bingo += 1
                        if y + x == 4:
                            cross[1] += 1
                            if cross[1] == 5:
                                bingo += 1
                        if row[y] == 5:
                            bingo += 1
                        if col[x] == 5:
                            bingo += 1
                        if bingo >= 3:
                            return (j+1) + i * 5
print(make_bingo())