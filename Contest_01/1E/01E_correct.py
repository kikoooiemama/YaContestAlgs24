# Created by Nikolay Pakhomov 17.03.2024
with open('input.txt') as f:
    n, k, d = map(int, f.readline().split())

mod = n % k
ans = [n]
no_solution = False
for i in range(d):
    cont = True
    for new_digit in range(10):
        new_mod = (mod * 10 + new_digit) % k
        if new_mod == 0:
            ans.append(new_digit)
            mod = new_mod
            cont = False
            break
    if cont:
        no_solution = True
        break

if no_solution:
    print(-1)
else:
    print(''.join(map(str, ans)))
