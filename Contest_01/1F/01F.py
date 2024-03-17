# Created by Nikolay Pakhomov 17.03.2024
with open('input2.txt') as f:
    n = int(f.readline().strip())
    numbers = list(map(int, f.readline().split()))

print(n)
print(numbers)
ans = []

# ВАЖНО!!! ПОМНИ, ЧТО УМНОЖЕНИЕ СЧИТАЕТСЯ ПЕРВЫМ!!!!!!!!!!!
first = True
leftIsEven = False
for i in numbers:
    if first:
        if i % 2 == 0:
            leftIsEven = True
        first = False
        continue

    if i % 2 == 0:
        if leftIsEven:
            ans.append('x')
        else:
            ans.append('+')
            leftIsEven = False
    else:
        if leftIsEven:
            ans.append('+')
            leftIsEven = False
        else:
            ans.append('x')

print("".join(ans))
