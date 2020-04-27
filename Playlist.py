import sys
import spotipy
import spotipy.util as util
import random

#first 6 lines are getting credentials to authorize my account
#top_artists is a list of my top artists over a specified time range
#time_range specifies what that time range is: short_term, medium_term, or long_term
#With spotipy, artists/playlists/songs are read in as id/uri/url so need to convert to one of these three options
class Playlist:
    def __init__(self, name, desc, time, songs):
        self.client_id = 'YOUR_CLIENT_ID_HERE'
        self.client_secret = 'YOUR_CLIENT_SECRET_HERE'
        self.scope = 'YOUR_SCOPE_HERE'
        self.username = 'YOUR_USERNAME_HERE'
        self.redirect_uri = 'YOUR_REDIRECT_URI_HERE'
        self.token = util.prompt_for_user_token(self.username,
                                   self.scope,
                                   client_id=self.client_id,
                                   client_secret=self.client_secret,
                                   redirect_uri='https://www.google.com/')

        self.playlist_name = name
        self.description = desc
        self.time_range = time
        self.sp = spotipy.Spotify(auth = self.token) #spotify object
        self.total_songs = songs

    #If user wants information about their account
    def me(self):
        return self.sp.current_user()

    #Create the playlist with the above information
    #Initialize the playlist id
    def create_playlist(self):
        self.playlist_info = self.sp.user_playlist_create(self.username, self.playlist_name,True,self.description)
        self.playlist_id = self.playlist_info['id']

    #Returns the top artists for the user over a specified time range
    def get_top_artists(self):
        return self.sp.current_user_top_artists(15, 0, self.time_range)

    #Gets an id from a random arist from the list of top artists
    def get_top_artist_id(self, artists):
        if(len(artists) == 0):
            print('No artists in this time frame')
            return -1
        else:
            artist_list = artists['items']
            rand_int = random.randint(0, len(artist_list) - 1)
            artist_info = artist_list[rand_int]
            artist_id = artist_info['id']
            return artist_id

    #Gets a releated artist id from a list of related artists
    def get_related_artist_id(self, artists):
        if(len(artists) == 0):
            print('No artists in this time frame')
            return -1
        else:
            artist_list = artists['artists']
            rand_int = random.randint(0, len(artist_list) - 1)
            artist_info = artist_list[rand_int]
            artist_id = artist_info['id']
            return artist_id

    #Gets the song id
    def get_song_id(self, songs):
        if(len(songs) == 0):
            print("No songs")
            return -1
        else:
            songs_list = songs['tracks']
            rand_int = random.randint(0, len(songs) - 1)
            song_info = songs_list[rand_int]
            song_id = song_info['id']
            return [song_id]

    #Adds songs to playlist if user selects that the playlist should be of their top artists
    def add_songs_top(self):
        top_artists = self.get_top_artists()
        for i in range(0, self.total_songs):
            rand_artist = self.get_top_artist_id(top_artists)
            songs = self.sp.artist_top_tracks(rand_artist, 'US')
            song_id = self.get_song_id(songs)
            self.sp.user_playlist_add_tracks(self.username, self.playlist_id, song_id)

    #Adds songs to playlist if user selects that playlist should be of recommended artists
    def add_songs_related(self):
        top_artists = self.get_top_artists()
        for i in range(0, self.total_songs):
            related_artist_id = self.get_top_artist_id(top_artists)
            related_artists = self.sp.artist_related_artists(related_artist_id)
            related_artist = self.get_related_artist_id(related_artists)
            songs =self.sp.artist_top_tracks(related_artist, 'US')
            song_id = self.get_song_id(songs)
            self.sp.user_playlist_add_tracks(self.username, self.playlist_id, song_id)
