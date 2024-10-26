# Created by Nikolay Pakhomov 25.10.2024

# I, O, C, L, H, P, X
def define_mask(vector, fill_on, fill_off):
    start = True
    mask = ""
    for i in vector:
        if start:
            mask = fill_on if i == fill_on else fill_off
            start = False
        else:
            if i == fill_on and mask[-1] == fill_off:
                mask += fill_on
            if i == fill_off and mask[-1] == fill_on:
                mask += fill_off
    return mask


def matches_mask_and_clear(tmp, templates: dict, part, build: dict):
    result = []
    bad_keys = []
    for k in templates.keys():
        ref = templates.get(k)[part]
        if ref == tmp:
            result.append(k)
        else:
            bad_keys.append(k)
    # clear
    for k in bad_keys:
        templates.pop(k)
        build.pop(k)
    return result


def define_letter(img, x1, y1, y2, bn, d_on, d_off, fill_on, fill_off, br_marker):
    templates = {"I": ["x", "-"], "O": ["x", "x-x", "x", "-"], "C": ["x", "x-x", "-"], "L": ["x", "-x", "-"],
                 "H": ["x", "-x-", "x", "-"], "P": ["x", "x-x-", "x-", "-"]}
    build = {"I": [0, 0], "O": [0, 0, 0, 0], "C": [0, 0, 0], "L": [0, 0, 0], "H": [0, 0, 0, 0], "P": [0, 0, 0, 0]}
    part = 0
    end_border = []
    end_diodes = []
    previous_vector = []
    for j in range(y2, y1 + 1):
        # if img[j][x1] == d_on:
        #     img[j][x1] = fill_on
        # elif img[j][x1] == d_off
        previous_vector.append(img[j][x1])
        end_border.append(br_marker)
        end_diodes.append(fill_off)
    # 1 часть
    for k in build.keys():
        build.get(k)[part] = previous_vector.copy()
    part = 1
    vector = []
    # находим часть 2
    for i in range(x1 + 1, bn):
        for j in range(y2, y1 + 1):
            if img[j][i] == d_on:
                img[j][i] = fill_on
            elif img[j][i] == d_off or img[j][i] == br_marker:
                img[j][i] = fill_off
            vector.append(img[j][i])
        if vector == previous_vector:
            vector.clear()
            continue
        options = matches_mask_and_clear(define_mask(vector, fill_on, fill_off), templates, part, build)
        if len(options) == 0:
            return "X"
        else:
            # analysis options
            for k in build.keys():
                builder = build.get(k)
                builder[part] = vector.copy()
                if 0 not in builder:
                    return k
            previous_vector = vector.copy()
            part += 1
            vector.clear()
            # проверяем завершилось ли определение
    return "X"


def find_letter(img, bn, br_marker):
    # маркеры
    letter_x, d_on, d_off, fill_on, fill_off = "X", "#", ".", "x", "-"
    # поиск вертикали
    x0, y0 = 1, bn - 1
    for j in range(y0, -1, -1):
        find = False
        for i in range(x0, bn):
            if img[j][i] == d_on:
                x1 = i
                y1 = j
                img[j][i] = fill_on
                nj = j - 1
                while img[nj][i] == d_on:
                    img[nj][i] = fill_on
                    nj += -1
                y2 = nj + 1
                find = True
                break
        if find:
            break
    if not find:
        return letter_x
    # идем по горизонтали вдоль вертикали
    result = define_letter(img, x1, y1, y2, bn, d_on, d_off, fill_on, fill_off, br_marker)
    if result == letter_x:
        return result
    # проверка на включенные диоды
    for row in img:
        for ceil in row:
            if ceil == d_on:
                return letter_x
    return result


examples = []
results = []
with open('input_test.txt') as f:
    test_n = int(f.readline().strip())
    for i in range(test_n):
        table = []
        f.readline()
        n = int(f.readline().strip())
        for j in range(n):
            table.append(f.readline().strip())
        examples.append(table)

print(test_n)
with open('output_test.txt') as f:
    for i in range(test_n):
        results.append(f.readline().strip())

for ex in range(test_n):
    tb = examples[ex]
    rs = results[ex]

    n = len(tb)
    m = n + 2
    field = [list('b' * m)]
    for p in range(n):
        field.append(['b'] + list(tb[p]) + ['b'])
    field.append(list('b' * m))

    letter = find_letter(field, m, "b")

    print()
    for i in range(len(tb)):

        if len(tb) // 2 == i:
            print(f"{tb[i]} -----> Test {ex+1}: {letter == rs} [{letter}, {rs}]")
        else:
            print(tb[i])
