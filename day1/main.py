from solve import solve

def main():
    solution_part_one, solution_part_two = solve("puzzle-input.txt")
    print(f"Part1: The dial was left pointed at zero after rotation {solution_part_one} times!")
    print(f"Part2: The dial pointed at zero {solution_part_two} total times!")

if __name__ == "__main__":
    main()