from library import Library
import unittest

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

    def test_add_song_attributes_into_library_list_new_song(self):
        input_artist = "artist"
        input_title = "title"
        input_length = "length"
        input_genre = "genre"
        input_year = "year"
        input_lyrics = "Some lyrics"
        expected_length = len(self.library.df)+1
        self.library.add_song_attributes_into_library_list(
            input_artist, input_title, input_length, input_genre, input_year, input_lyrics)
        self.assertEqual(len(self.library.df), expected_length)
    
    def test_add_song_attributes_into_library_list_limited_info(self):
        input_artist = "artist"
        input_title = ""
        input_length = ""
        input_genre = ""
        input_year = ""
        input_lyrics = ""
        expected_length = len(self.library.df)+1
        self.library.add_song_attributes_into_library_list(
            input_artist, input_title, input_length, input_genre, input_year, input_lyrics)
        self.assertEqual(len(self.library.df), expected_length)
    
    def test_add_song_attributes_into_library_list_empty(self):
        input_artist = ""
        input_title = ""
        input_length = ""
        input_genre = ""
        input_year = ""
        input_lyrics = ""
        expected_length = len(self.library.df)
        self.library.add_song_attributes_into_library_list(
            input_artist, input_title, input_length, input_genre, input_year, input_lyrics)
        self.assertEqual(len(self.library.df), expected_length)

    def test_add_song_attributes_into_library_list_all_None(self):
        input_artist = None
        input_title = None
        input_length = None
        input_genre = None
        input_year = None
        input_lyrics = None
        expected_length = len(self.library.df)
        self.library.add_song_attributes_into_library_list(
            input_artist, input_title, input_length, input_genre, input_year, input_lyrics)
        self.assertEqual(len(self.library.df), expected_length)

    def test_delete_song_attributes_from_library_with_title_name_None(self):
        input = None
        expected_length = len(self.library.df)
        self.library.delete_song_attributes_from_library_with_title_name(input)
        self.assertEqual(len(self.library.df), expected_length)

    def test_delete_song_attributes_from_library_with_title_name_empty(self):
        input = ""
        expected_length = len(self.library.df)
        self.library.delete_song_attributes_from_library_with_title_name(input)
        self.assertEqual(len(self.library.df), expected_length)

    def test_delete_song_attributes_from_library_with_title_not_exist(self):
        input = "something does not exist"
        expected_length = len(self.library.df)
        self.library.delete_song_attributes_from_library_with_title_name(input)
        self.assertEqual(len(self.library.df), expected_length)

    def test_delete_song_attributes_from_library_with_title_success(self):
        input = "Shape Of You"
        expected_length = len(self.library.df)-1
        self.library.delete_song_attributes_from_library_with_title_name(input)
        self.assertEqual(len(self.library.df), expected_length)
if __name__ == '__main__':
    unittest.main()