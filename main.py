from src.solver import *
from src.visualizer import *
import argparse
from src.file_parser import parse_file
from colorama import init
from src.puzzle_generator import generate_puzzle


def config_cmd():
    config = argparse.ArgumentParser(description='Solve Shikaku - returns a '
                                                 'solution of shikaku puzzle')
    config.add_argument('-f', '--file', type=argparse.FileType(mode='r'),
                        help="Provide a name of file with puzzle grid. "
                             "Empty squares should be marked as '-'. "
                             "Squares must be separated by space in each row.")
    config.add_argument('-n', '--number', type=int, dest='n',
                        help='Provide a number of solutions to show')
    return config


if __name__ == "__main__":
    init()
    arguments = config_cmd().parse_args()
    if arguments.file is None:
        generate_puzzle()
        with open("src/generated_puzzle.txt", "r") as file:
            print(green_color_string("Generated puzzle:"))
            print(*[line for line in file], sep='')
            file.seek(0)
            numbers_list, size_x, size_y = parse_file(file)
            print(green_color_string("Solutions:"))
    else:
        numbers_list, size_x, size_y = parse_file(arguments.file)
    if not size_y:
        print(red_color_string('Provided file is empty.'))
        quit()
    answers = []
    for numbers in numbers_list:
        answers.extend(solve(numbers, size_x, size_y))
    if not answers:
        print(red_color_string('This puzzle has no solution.'))
        quit()
    solutions_count = len(answers) if arguments.n is None else arguments.n
    if solutions_count > len(answers):
        s = 's' if len(answers) > 1 else ''
        print(green_color_string(f'There are only {len(answers)} solution{s}'))
    for i in range(min(solutions_count, len(answers))):
        matrix = answer_to_matrix(answers[i], size_x, size_y)
        visual = matrix_to_visual(matrix, size_x, size_y)
        for line in visual:
            print(*line)
        print()
