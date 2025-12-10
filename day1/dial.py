class Dial:
    def __init__(self):
        self.current_position = 50
        self.numbers = list(range(0, 100))
        self.zeroes_hit = 0
    
    def get_current_position(self):
        return self.current_position
    
    def get_numbers(self):
        return self.numbers
    
    def get_zeroes_hit(self):
        return self.zeroes_hit
    
    def increment_zeroes_hit(self):
        self.zeroes_hit += 1

    def rotate_right(self, number_of_rotations, is_part_two):
        while number_of_rotations > 0:
            self.current_position += 1
            number_of_rotations -= 1

            if self.current_position == 100:
                self.current_position = 0
                if is_part_two:
                    self.increment_zeroes_hit()
        
        return self.current_position
    
    def rotate_left(self, number_of_rotations, is_part_two):
        while number_of_rotations > 0:
            self.current_position -= 1
            number_of_rotations -= 1

            if self.current_position == -1:
                self.current_position = 99
                if is_part_two:
                    self.increment_zeroes_hit()

        return self.current_position