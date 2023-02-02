import sys

input = sys.stdin.readline

n = int(input())

sum = 0
num_list = list(map(int, input().split()))
sum_list = [0] * n

for i in range(n):
    if sum + num_list[i] > 0:
        sum = sum + num_list[i]
        sum_list[i] = sum
    else:
        sum_list[i] = sum
        sum = 0
        
print(max(sum_list) if max(sum_list) > 0 else max(num_list))