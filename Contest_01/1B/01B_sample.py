with open('input3.txt') as f:
    g11, g21 = map(int, f.readline()[:-1].split(':'))
    g12, g22 = map(int, f.readline()[:-1].split(':'))
    flag = f.readline().strip()

if flag == "1":
    score1 = g11 * 100 + g12 * 101
    score2 = g21 * 101 + g22 * 100
    print(max(0, (score2 - score1 + 101) // 101))
else:
    score1 = g11 * 101 + g12 * 100
    score2 = g21 * 100 + g22 * 101
    print(max(0, (score2 - score1 + 100) // 100))
