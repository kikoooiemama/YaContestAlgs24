# Created by Nikolay Pakhomov 11.03.2024


# def main():
#     with open('input.txt') as f:
#         nums = f.read().split()
#
#     a, b = map(int, nums)
#     result = a + b
#
#     with open('output.txt', 'w') as f:
#         f.write(str(result))
#
#
# if __name__ == '__main__':
#     main()

with open('input.txt') as f:
    nums = f.read().split()

a, b = map(int, nums)
result = a + b

with open('output.txt', 'w') as f:
    f.write(str(result))