from src.solver import Point, FieldNumber
from src.visualizer import red_color_string
import re


def parse_file(f):
    def continue_defining(q, un_number, current_defined, index, current_sum):
        nonlocal defined_numbers, undefined
        next_defined = current_defined.copy()
        next_defined.append(FieldNumber(q, un_number.location))
        if index + 1 == len(undefined):
            if current_sum - q == 0:
                defined_numbers.append(next_defined)
        else:
            define_numbers(index + 1, current_sum - q, next_defined)

    def define_numbers(index, current_sum, current_defined):
        nonlocal undefined
        un_number, is_smaller = undefined[index][0], undefined[index][1]
        if is_smaller:
            for q in range(min(un_number.value, current_sum + 1)):
                continue_defining(q, un_number, current_defined, index,
                                  current_sum)
        else:
            for q in range(un_number.value + 1, current_sum + 1):
                continue_defining(q, un_number, current_defined, index,
                                  current_sum)

    sz_y, sz_x, numbers_list = 0, 0, []
    undefined, initial_sum = [], 0
    for row in f:
        row = row.split()
        sz_x = len(row)
        for j in range(sz_x):
            if re.fullmatch(r'\d+', row[j]):
                field_number = FieldNumber(int(row[j]), Point(j, sz_y))
                numbers_list.append(field_number)
                initial_sum += field_number.value
            elif re.fullmatch(r'<\d+', row[j]):
                field_number = FieldNumber(int(row[j][1:]), Point(j, sz_y))
                undefined.append((field_number, True))
            elif re.fullmatch(r'>\d+', row[j]):
                field_number = FieldNumber(int(row[j][1:]), Point(j, sz_y))
                undefined.append((field_number, False))
            elif row[j] != '-':
                print(red_color_string(
                    'Provided file is not in correct format.'))
                quit()
        sz_y += 1
    if undefined:
        defined_numbers, area = [], sz_x * sz_y
        define_numbers(0, area - initial_sum, [])
        result_numbers_list = []
        for numbers in defined_numbers:
            case = numbers_list.copy()
            case.extend(numbers)
            case.sort(key=lambda x: (x.location.y, x.location.x))
            result_numbers_list.append(case)
    else:
        result_numbers_list = [numbers_list]
    return result_numbers_list, sz_x, sz_y
