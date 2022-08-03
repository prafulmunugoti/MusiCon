import unittest

from library import Library


class libraryTest(unittest.TestCase):
    def setUp(self):
        self.library = Library()

    def test_check_if_title_exists_in_musicon_library_empty_input(self):
        input = ""
        expected_output = False
        output = self.library.check_if_title_exists_in_musicon_library(input)
        self.assertEqual(output, expected_output)

    def test_check_if_title_exists_in_musicon_library_exist(self):
        input = "Shape Of You"
        expected_output = True
        output = self.library.check_if_title_exists_in_musicon_library(input)
        self.assertEqual(output, expected_output)

    def test_check_if_title_exists_in_musicon_library_not_exist(self):
        input = "something does not exist"
        expected_output = False
        output = self.library.check_if_title_exists_in_musicon_library(input)
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()