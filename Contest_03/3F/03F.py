# Created by Nikolay Pakhomov 04.11.2024
with open("input.txt") as f:
    n = int(f.readline().strip())
    order = f.readline()
    s = f.readline()

count_sq = 0
count_ci = 0
# Если у строк A, B одинаковые подстроки s, то если A_s+1 < B_s+1, то A < B.
