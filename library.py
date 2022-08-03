#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from copy import deepcopy
from random import randint
import time

#reading the information in CSV file into a dataframe object 
df = pd.read_csv('songs.csv')

#Song with attributes title, artist, album, year, lyrics
# e.g:
# title  : Bad Habits
# artist : EdSheeran
# year   : 2021
# length : 3:04
# lyrics : Every time you come around, you know I can't say no
#          Every time the sun goes down, I let you take control
#          I can feel the paradise before my world implodes
#          And tonight had something wonderful .... goes on
#
#Class definition to store music library which has the above information 
class Library:
    def __init__(self):
        self.dummy = None
   
    def add_song_attributes_into_library_list(self,artist,title,length,genre,year,lyrics):
        print(" adding ",title," song into library using Data frame")
        df.loc[len(df.index)] = [artist,title,length,genre,year,lyrics]
        print("completed adding the song to Data frame object")
    
    def delete_song_attributes_from_library_with_title_name(self,title):
        print(" deleting ",title," song from libary using Data frame\n")
        df.drop(df.loc[df['title']==title].index, inplace=True)
        print("completed deleting the song from Data frame object")
        
    def searching_for_titles_in_musicon_library_by_artist(self,artist):
        #extract the unique artist list 
        artist_list = df["artist"].unique().tolist()
        #extract the titles based on artist name
        musicon_artists_df = df.loc[df['artist'] == artist]
        musicon_artist_list = musicon_artists_df["title"].tolist()
        print("\n\nSongs of ",artist," in library are : \n")
        total_songs = len(musicon_artist_list)
        if total_songs == 0:
            print("there are no songs with artist ",artist," in library\n")
        else:
            for artist_song in musicon_artist_list:
                print("    ",artist_song)
        
    def check_if_title_exists_in_musicon_library(self,title):
        #check if the song name exists in the library and returns true or false
        title_exists = df['title'].eq(title).any()
        return title_exists
        
    def show_all_titles_present_in_musicon_library(self):
        #extract the unique song titles list 
        song_titles_list = df["title"].unique().tolist()
        for song_title in song_titles_list:
            print("  ",song_title," \n")
    
    def show_info_about_song_title_from_musicon_library(self,title):
        #extract the information about the song 
        df_song_info = df.loc[df['title'] == title]
        print ("Attributes of the Song : ",title,"\n\n")
        # Iterate over each row
        for attribute in df_song_info.itertuples():
        # print requested song attributes for the title
            print("    Title :",attribute.title,"\n")
            print("    Artist :",attribute.artist,"\n")
            print("    Length :",attribute.length,"\n")
            print("    Genre :",attribute.genre,"\n")
            print("    Year :",attribute.year,"\n")
            print("    Lyrics :\n",attribute.lyrics,"\n")


# In[ ]:




