#!/usr/bin/env python
# coding: utf-8
from library import Library
from playlist import Playlist

import pandas as pd
import unittest

class PlaylistTest(unittest.TestCase):
    def setUp(self):
        df = pd.read_csv('songs.csv')
        self.library = Library(df)
        self.playlist = Playlist()

    # Test create_a_new_playlist()
    def test_create_a_new_playlist_none_input(self):
        input = None
        expected_output = len(self.playlist.playlist_dict.keys())
        self.playlist.create_a_new_playlist(input)
        self.assertEqual(len(self.playlist.playlist_dict.keys()), expected_output)

    def test_create_a_new_playlist_empty_input(self):
        input = ""
        expected_output = len(self.playlist.playlist_dict.keys())
        self.playlist.create_a_new_playlist(input)
        self.assertEqual(len(self.playlist.playlist_dict.keys()), expected_output)

    def test_create_a_new_playlist_valid_input(self):
        input = "playlist1"
        expected_output =len(self.playlist.playlist_dict.keys())+1
        self.playlist.create_a_new_playlist(input)
        self.assertEqual(len(self.playlist.playlist_dict.keys()), expected_output)
        
    def test_create_a_new_playlist_existing_name_input(self):
        input = "playlist1"
        expected_output = len(self.playlist.playlist_dict.keys())+1
        self.playlist.create_a_new_playlist(input)
        self.playlist.create_a_new_playlist(input)
        self.assertEqual(len(self.playlist.playlist_dict.keys()), expected_output)

    def test_create_a_new_playlist_multiple_input(self):
        input1 = "playlist1"
        input2 = "playlist2"
        expected_output = len(self.playlist.playlist_dict.keys())+2
        self.playlist.create_a_new_playlist(input1)
        self.playlist.create_a_new_playlist(input2)
        self.assertEqual(len(self.playlist.playlist_dict.keys()), expected_output)

    # Test display_existing_playlists()
    def test_display_existing_playlists_input(self):
        input = None
        expected_output = len(self.playlist.playlist_dict.keys())
        output = self.playlist.display_existing_playlists()
        self.assertEqual(output, expected_output) 
    
    # Test add_song_into_playlist_dictionary()
    def test_add_song_into_playlist_dictionary_None_input(self):
        playlist_name_input = None
        title_name_input = None
        expected_output = False
        output = self.playlist.add_song_into_playlist_dictionary(playlist_name_input, title_name_input)
        self.assertEqual(output, expected_output) 

    def test_add_song_into_playlist_dictionary_empty_input(self):
        playlist_name_input = ""
        title_name_input = ""
        expected_output = False
        output = self.playlist.add_song_into_playlist_dictionary(playlist_name_input, title_name_input)
        self.assertEqual(output, expected_output) 
        
    def test_add_song_into_playlist_dictionary_valid_playlist_empty_title(self):
        playlist_name_input = "playlist1"
        title_name_input = ""
        expected_output = False
        output = self.playlist.add_song_into_playlist_dictionary(playlist_name_input, title_name_input)
        self.assertEqual(output, expected_output) 
    
    def test_add_song_into_playlist_dictionary_empty_playlist_valid_title(self):
        playlist_name_input = ""
        title_name_input = "Waka Waka"
        expected_output = False
        output = self.playlist.add_song_into_playlist_dictionary(playlist_name_input, title_name_input)
        self.assertEqual(output, expected_output) 
    
    def test_add_song_into_playlist_dictionary_valid_playlist_valid_title(self):
        playlist_name_input = "playlist1"
        title_name_input = "Waka Waka"
        expected_output = True
        self.playlist.create_a_new_playlist(playlist_name_input)
        output = self.playlist.add_song_into_playlist_dictionary(playlist_name_input, title_name_input)
        self.assertEqual(output, expected_output) 
        
    def test_add_song_into_playlist_dictionary_invalid_playlist_valid_title(self):
        playlist_name_input = "playlist100"
        title_name_input = "Waka Waka"
        expected_output = False
        output = self.playlist.add_song_into_playlist_dictionary(playlist_name_input, title_name_input)
        self.assertEqual(output, expected_output) 
        
if __name__ == '__main__':
    unittest.main()
