import unittest

from document import Document
from dial import Dial
from solve import split_instruction, execute_instructions_part_one, execute_instructions_part_two


class TestSplitString(unittest.TestCase):
    def test_split_instruction_one_digit(self):
        instruction = "R3"
        output_instruction = split_instruction(instruction)
        self.assertEqual(output_instruction, ("R", 3))

    def test_split_instruction_two_digits(self):
        instruction = "L34"
        output_instruction = split_instruction(instruction)
        self.assertEqual(output_instruction, ("L", 34))

    def test_split_instruction_three_digits(self):
        instruction = "R888"
        output_instruction = split_instruction(instruction)
        self.assertEqual(output_instruction, ("R", 888))

class TestExecuteInstructionsPartOne(unittest.TestCase):
    def test_execute_instructions(self):
        dial = Dial()
        document = Document()
        instructions_list = document.create_instructions_list("test-puzzle-input.txt")
        zeroes_hit = execute_instructions_part_one(dial, instructions_list)
        self.assertEqual(3, zeroes_hit)

class TestExecuteInstructionsPartTwo(unittest.TestCase):
    def test_execute_instructions(self):
        dial = Dial()
        document = Document()
        instructions_list = document.create_instructions_list("test-puzzle-input.txt")
        zeroes_hit = execute_instructions_part_two(dial, instructions_list)
        self.assertEqual(6, zeroes_hit)