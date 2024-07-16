
import sys

n = int(input())
row_info = []
col_info = []

for i in range(n):
    row_info.append(sys.stdin.readline())

# column버전 만들기
for i in range(n):
    now_col = ""
    for j in range(n):
        now_col += row_info[j][i]
    col_info.append(now_col+"\n")

row_cnt = 0
col_cnt = 0

for line in range(n):
    count_dots = 0
    for index in range(n+1):
        if row_info[line][index] == '.':
            count_dots += 1

        elif row_info[line][index] != '.':
            if count_dots > 1:
                row_cnt += 1
                count_dots = 0
            else:
                count_dots = 0
print(row_cnt)

for line in range(n):
    count_dots = 0
    for index in range(n+1):
        if col_info[line][index] == '.':
            count_dots += 1

        elif col_info[line][index] != '.':
            if count_dots > 1:
                col_cnt += 1
                count_dots = 0
            else:
                count_dots = 0
print(col_cnt)