# Created by Nikolay Pakhomov 17.03.2024

with open('input.txt') as f:
    n = int(f.readline().strip())
    nums = list(map(int, f.readline().split()))

ans = []
# Решение через состояния
state = 'no_odd_summand'
for num in nums:
    if state == 'no_odd_summand':
        if num % 2 == 0:
            ans.append('+')
        else:
            state = 'last_odd'
    elif state == 'last_odd':
        if num % 2 == 0:
            ans.append('+')
            state = 'multiply_even'
        else:
            ans.append('x')
    elif state == 'multiply_even':
        ans.append('x')

print(''.join(ans))
