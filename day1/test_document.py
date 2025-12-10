import unittest

from document import Document

class TestDocumentAttributesOnInit(unittest.TestCase):
    def test_document_on_init(self):
        document = Document()
        self.assertEqual(document.instructions, [])

class TestDocumentCreateInstructionsList(unittest.TestCase):
    def test_document_create_instructions_list(self):
        document = Document()
        instructions_list = document.create_instructions_list("test-puzzle-input.txt")
        expected = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
        self.assertEqual(instructions_list, expected)