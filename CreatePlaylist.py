from Playlist import *

def main():
    print("Welcome to Spotify Playlist Generator")
    print('For the next few questions, write your answer within quotations ("Nick")')

    #Generic questions for the playlist
    n = input("What would you like your playlist to be named? ")
    d = input("What would you like the description of the playlist to be? ")
    #Spotify writes that time frame is several years for long_term, last 6 months for medium, and last 4 weeks for short
    t = input("What time-frame of your Spotify history would you like to use? (short_term, medium_term, or long_term) ")
    total_songs = int(input("How many total songs would you like in the playlist? (enter a number 1 - 99) "))

    #Creating the playlist
    playlist = Playlist(n,d,t,20)
    playlist.create_playlist()

    #Deciding if your playlist will include new artists, or a combination of current artists and new artists
    ans = input("Will your playlist be of your top artists(1) or recommended songs(2)? ")
    if(ans is 1):
        playlist.add_songs_top()
    elif(ans is 2):
        playlist.add_songs_related()
    print('Your playlist has been created!')

main()
