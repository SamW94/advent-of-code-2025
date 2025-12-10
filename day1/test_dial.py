import unittest

from dial import Dial

class TestDialAttributesOnInit(unittest.TestCase):
    def test_start_position(self):
        dial = Dial()
        current_position = dial.get_current_position()
        self.assertEqual(current_position, 50)

    def test_numbers(self):
        dial = Dial()
        numbers = dial.get_numbers()
        expected = list(range(0, 100))
        self.assertEqual(numbers, expected)

    def test_zeroes_hit(self):
        dial = Dial()
        zeroes_hit = dial.get_zeroes_hit()
        self.assertEqual(zeroes_hit, 0)

class TestIncrementZeroesHit(unittest.TestCase):
    def test_increment_zeroes_hit(self):
        dial = Dial()
        dial.increment_zeroes_hit()
        zeroes_hit = dial.zeroes_hit
        self.assertEqual(zeroes_hit, 1)

class TestDialRotateRightPartOne(unittest.TestCase):
    def test_without_overflow(self):
        dial = Dial()
        new_position = dial.rotate_right(10, False)
        self.assertEqual(new_position, 60)

    def test_with_overflow(self):
        dial = Dial()
        new_position = dial.rotate_right(69, False)
        self.assertEqual(new_position, 19)

    def test_with_multiple_overflows(self):
        dial = Dial()
        new_position = dial.rotate_right(169, False)
        self.assertEqual(new_position, 19)

class TestDialRotateLeftPartOne(unittest.TestCase):
    def test_without_underflow(self):
        dial = Dial()
        new_position = dial.rotate_left(10, False)
        self.assertEqual(new_position, 40)

    def test_with_underflow(self):
        dial = Dial()
        new_position = dial.rotate_left(70, False)
        self.assertEqual(new_position, 80)

    def test_with_multiple_underflows(self):
        dial = Dial()
        new_position = dial.rotate_left(170, False)
        self.assertEqual(new_position, 80)

class TestDialRotateRightPartTwo(unittest.TestCase):
    def test_without_overflow(self):
        dial = Dial()
        new_position = dial.rotate_right(10, True)
        self.assertEqual(new_position, 60)

    def test_with_overflow(self):
        dial = Dial()
        new_position = dial.rotate_right(69, True)
        self.assertEqual(new_position, 19)
        self.assertEqual(dial.get_zeroes_hit(), 1)

    def test_with_multiple_overflows(self):
        dial = Dial()
        new_position = dial.rotate_right(169, True)
        self.assertEqual(new_position, 19)
        self.assertEqual(dial.get_zeroes_hit(), 2)

class TestDialRotateLeftPartTwo(unittest.TestCase):
    def test_without_underflow(self):
        dial = Dial()
        new_position = dial.rotate_left(10, True)
        self.assertEqual(new_position, 40)

    def test_with_underflow(self):
        dial = Dial()
        new_position = dial.rotate_left(70, True)
        self.assertEqual(new_position, 80)
        self.assertEqual(dial.get_zeroes_hit(), 1)

    def test_with_multiple_underflows(self):
        dial = Dial()
        new_position = dial.rotate_left(170, True)
        self.assertEqual(new_position, 80)
        self.assertEqual(dial.get_zeroes_hit(), 2)

if __name__ == "__main__":
    unittest.main()