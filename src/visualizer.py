from src.solver import Rectangle


def green_color_string(string):
    return '\033[1m\033[32m{}\033[0m'.format(string)


def red_color_string(string):
    return '\033[1m\033[31m{}\033[0m'.format(string)


def answer_to_matrix(answer: [Rectangle], size_x: int, size_y: int) -> [[int]]:
    field = [[0] * size_x for _ in range(size_y)]
    for i in range(len(answer)):
        for y in range(answer[i].top_left.y,
                       answer[i].top_left.y + answer[i].height):
            for x in range(answer[i].top_left.x,
                           answer[i].top_left.x + answer[i].width):
                field[y][x] = i + 1
    return field


def matrix_to_visual(m: [[int]]) -> [[str]]:
    vertical_border = green_color_string('—')
    horizontal_border = green_color_string('|')
    size_y, size_x = len(m), len(m[0])
    initial = []
    for i in range(size_y):
        initial.append(
            [horizontal_border] + [i for i in ' '.join(['x'] * size_x)] + [
                horizontal_border])
        if i != size_y - 1:
            initial.append([horizontal_border] + [' '] * (2 * size_x - 1) + [
                horizontal_border])
    initial.insert(0, [vertical_border] * (2 * size_x + 1))
    initial.append([vertical_border] * (2 * size_x + 1))
    for y in range(size_y):
        for x in range(size_x):
            if y + 1 < size_y and m[y][x] != m[y + 1][x]:
                initial[(y + 1) * 2][x * 2 + 1] = vertical_border
                if x + 1 < size_x:
                    initial[(y + 1) * 2][(x + 1) * 2] = vertical_border
            if x + 1 < size_x and m[y][x] != m[y][x + 1]:
                initial[y * 2 + 1][(x + 1) * 2] = horizontal_border
                if y + 1 < size_y:
                    initial[(y + 1) * 2][(x + 1) * 2] = horizontal_border
    for y in range(2, size_y * 2, 2):
        for x in range(2, size_x * 2, 2):
            if initial[y][x - 1] == initial[y][x + 1] == vertical_border \
                    and initial[y][x] == horizontal_border and \
                    (initial[y - 1][x] != horizontal_border or
                     initial[y + 1][x] != horizontal_border):
                initial[y][x] = vertical_border
    return initial


def answer_to_visual(answer: [Rectangle], size_x: int, size_y: int) -> [[str]]:
    return matrix_to_visual(answer_to_matrix(answer, size_x, size_y))
