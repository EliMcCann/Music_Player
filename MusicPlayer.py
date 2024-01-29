"""

Author: Elijah McCann
Program: musicPlayer.py
1/12/2024

Simple Command-Line based music player app that can play a standard .mp3 audio file.

NOTE: MUST INSTALL the pygame package before running this app!!!
(  At command prompt[CLI] run: pip install pygame --pre  )

"""

# Import statement for the pygame mixer module
from pygame import mixer

# Initialize the mixer module
mixer.init()

def display_menu():
    # Display the user interface menu
    print("\nWelcome to the Python Music Player!")
    print("1. SELECT a song file.")
    print("2. PLAY the chosen song.")
    print("3. PAUSE an active song.")
    print("4. UNPAUSE the song.")
    print("5. Exit the program.")

def select_song():
    # Select a song file 
    song_file = input("Please enter the song's filename >> ")
    mixer.music.load(song_file)

def play_song():
    # Play the chosen song
    mixer.music.play()

def pause_song():
   # Pause an active song
    mixer.music.pause()

def unpause_song():
   # Unpause the song
    mixer.music.unpause()

# Display the initial menu
display_menu()

# Logic statements that determine which options to enter and what to do with the commands.
while True:
    menu_choice = input("Please enter a menu option (1-5) >> ")

    # Decision making that triggers each feature
    if menu_choice == "1":
        select_song()
    elif menu_choice == "2":
        play_song()
    elif menu_choice == "3":
        pause_song()
    elif menu_choice == "4":
        unpause_song()
    elif menu_choice == "5":
        input("Thank you for using the music player! Press ENTER to exit >> ")
        break
    else:
        print("Invalid option. Please enter a number from 1 to 5.")
    
    # Display the menu again after each operation
    display_menu()
