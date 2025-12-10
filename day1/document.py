class Document:
    def __init__(self):
        self.instructions = []

    def create_instructions_list(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                self.instructions.append(line.rstrip())

        return self.instructions
