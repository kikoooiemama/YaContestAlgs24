# Created by Nikolay Pakhomov 11.03.2024

with open('input.txt') as f:
    j = f.readline().strip()
    s = f.readline().strip()

result = 0
for ch in s:
    if ch in j:
        result += 1

print(result)

# with open('output.txt', 'w') as f:
#     f.write(str(result))
