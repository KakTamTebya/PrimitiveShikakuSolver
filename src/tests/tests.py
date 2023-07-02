import unittest
from src.puzzle_generator import generate_puzzle
from src.file_parser import parse_file
from src.solver import *
from src.visualizer import *


class TestPuzzleGenerator(unittest.TestCase):
    def test_all_puzzles_have_solution(self):
        for i in range(10):
            generate_puzzle()
            with open("generated_puzzle.txt", "r") as file:
                numbers_list, size_x, size_y = parse_file(file)
                answers = []
                for numbers in numbers_list:
                    answers.extend(solve(numbers, size_x, size_y))
                self.assertTrue(len(answers) > 0)

    def test_puzzles_have_provided_length_and_width(self):
        for i in range(1, 8):
            for j in range(i, 8):
                generate_puzzle(i, j)
                with open("generated_puzzle.txt", "r") as file:
                    numbers_list, size_x, size_y = parse_file(file)
                    self.assertTrue(size_x == i and size_y == j)


class TestSolver(unittest.TestCase):
    def test_returns_empty_list_when_no_solution(self):
        numbers_list = [FieldNumber(444, Point(1, 1)),
                        FieldNumber(228, Point(3, 4))]
        answers = solve(list(numbers_list), 100, 100)
        self.assertTrue(len(answers) == 0)

    def test_returns_all_solutions(self):
        with open("../grid_examples/grid3.txt", "r") as file:
            numbers_list, size_x, size_y = parse_file(file)
            answers = []
            for numbers in numbers_list:
                answers.extend(solve(numbers, size_x, size_y))
            self.assertTrue(len(answers) == 6)


class TestRectangle(unittest.TestCase):
    def test_contains_point(self):
        rect = Rectangle(Point(0, 0), 5, 7)
        self.assertTrue(rect.contains_point(Point(1, 1)))
        self.assertTrue(rect.contains_point(Point(4, 6)))
        self.assertFalse(rect.contains_point(Point(228, 1337)))

    def test_intersects_with(self):
        rect = Rectangle(Point(0, 0), 5, 7)
        test = Rectangle(Point(4, 4), 10, 3)
        self.assertTrue(rect.is_intersected_with(test))
        self.assertTrue(test.is_intersected_with(rect))

    def test_does_not_intersect_with(self):
        rect = Rectangle(Point(0, 0), 5, 7)
        test = Rectangle(Point(-10, -20), 10, 3)
        self.assertFalse(rect.is_intersected_with(test))
        self.assertFalse(test.is_intersected_with(rect))


class TestVisualizer(unittest.TestCase):
    def test_answer_to_matrix_saves_dimensions(self):
        rs = [Rectangle(Point(0, 0), 1, 1), Rectangle(Point(2, 2), 3, 8)]
        matrix = answer_to_matrix(rs, 10, 23)
        self.assertTrue(len(matrix) == 23 and len(matrix[0]) == 10)

    def test_matrix_to_visual_multiplies_dimensions(self):
        rs = [Rectangle(Point(0, 0), 1, 1), Rectangle(Point(2, 2), 3, 8)]
        matrix = answer_to_matrix(rs, 10, 23)
        x = matrix_to_visual(matrix, 10, 23)
        self.assertTrue(len(x) == 47 and len(x[0]) == 21)


if __name__ == '__main__':
    unittest.main()
