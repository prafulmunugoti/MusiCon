#!/usr/bin/env python
# coding: utf-8

import unittest

from playlist import Playlist


class PlaylistTest(unittest.TestCase):
    def setUp(self):
        self.playlist = Playlist()

    def create_a_new_playlist_empty_input(self):
        input = ""
        expected_output =len(self.playlist_dict.keys())
        output = self.playlist.create_a_new_playlist(input)
        self.assertEqual(len(self.playlist_dict.keys()), expected_output)

    def create_a_new_playlist_valid_input(self):
        input = "playlist1"
        expected_output =len(self.playlist_dict.keys())
        output = self.playlist.create_a_new_playlist(input)
        self.assertEqual(len(self.playlist_dict.keys()), expected_output)
        
    def create_a_new_playlist_existing_name_input(self):
        input = "playlist1"
        expected_output = len(self.playlist_dict.keys())
        output = self.playlist.create_a_new_playlist(input)
        self.assertEqual(len(self.playlist_dict.keys()), expected_output)

    def create_a_new_playlist_existing_name_input(self):
        input = "Pl@yL1sT"
        expected_output = len(self.playlist_dict.keys())
        output = self.playlist.check_if_title_exists_in_musicon_library(input)
        self.assertEqual(len(self.playlist_dict.keys()), expected_output)

    def display_existing_playlists_input(self):
        input = ""
        expected_output = len(self.playlist_dict.keys())
        output = self.playlist.check_if_title_exists_in_musicon_library(input)
        self.assertEqual(len(self.playlist_dict.keys()), expected_output) 
    
    def add_song_into_playlist_dictionary_empty_input(self):
        playlist_name_input = ""
        title_name_input = ""
        len(my_dict[3])
        expected_output = len(self.playlist_dict[playlist_name_input])
        self.assertEqual(len(self.playlist_dict[playlist_name_input]), expected_output) 
        
    def add_song_into_playlist_dictionary_valid_playlist_empty_title(self):
        playlist_name_input = "playlist1"
        title_name_input = ""
        len(my_dict[3])
        expected_output = len(self.playlist_dict[playlist_name_input])
        self.assertEqual(len(self.playlist_dict[playlist_name_input]), expected_output) 
        
    def add_song_into_playlist_dictionary_invalid_playlist_empty_title(self):
        playlist_name_input = "playlist100"
        title_name_input = ""
        len(my_dict[3])
        expected_output = len(self.playlist_dict[playlist_name_input])
        self.assertEqual(len(self.playlist_dict[playlist_name_input]), expected_output)
    
    def add_song_into_playlist_dictionary_valid_playlist_valid_title(self):
        playlist_name_input = "playlist1"
        title_name_input = "Waka Waka"
        len(my_dict[3])
        expected_output = len(self.playlist_dict[playlist_name_input])
        self.assertEqual(len(self.playlist_dict[playlist_name_input]), expected_output)
        
    def add_song_into_playlist_dictionary_valid_playlist_valid_title(self):
        playlist_name_input = "playlist1"
        title_name_input = "Perfect"
        len(my_dict[3])
        expected_output = len(self.playlist_dict[playlist_name_input])
        self.assertEqual(len(self.playlist_dict[playlist_name_input]), expected_output)
              
    def add_song_into_playlist_dictionary_invalid_playlist_valid_title(self):
        playlist_name_input = "playlist100"
        title_name_input = "Perfect"
        len(my_dict[3])
        expected_output = len(self.playlist_dict[playlist_name_input])
        self.assertEqual(len(self.playlist_dict[playlist_name_input]), expected_output)
        
if __name__ == '__main__':
    unittest.main()
