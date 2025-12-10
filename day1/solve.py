from dial import Dial
from document import Document

def split_instruction(string):
    direction = string[0]
    number_of_rotations = int(string[1:])
    return (direction, number_of_rotations)

def execute_instructions_part_one(dial, instructions_list):
    for instruction in instructions_list:
        instruction_tuple = split_instruction(instruction)

        if instruction_tuple[0] == "L":
            new_position = dial.rotate_left(instruction_tuple[1], False)
        else:
            new_position = dial.rotate_right(instruction_tuple[1], False)

        if new_position == 0:
            dial.increment_zeroes_hit()

    return dial.get_zeroes_hit()

def execute_instructions_part_two(dial, instructions_list):
    for instruction in instructions_list:
        instruction_tuple = split_instruction(instruction)

        if instruction_tuple[0] == "L":
            dial.rotate_left(instruction_tuple[1], True)
        else:
            dial.rotate_right(instruction_tuple[1], True)


    return dial.get_zeroes_hit()

def solve(attachment_file):
    dial_part_1 = Dial()
    dial_part_2 = Dial()
    document = Document()
    instructions_list = document.create_instructions_list(attachment_file)
    zeroes_hit_part_one = execute_instructions_part_one(dial_part_1, instructions_list)
    zeroes_hit_part_two = execute_instructions_part_two(dial_part_2, instructions_list)
    return zeroes_hit_part_one, zeroes_hit_part_two