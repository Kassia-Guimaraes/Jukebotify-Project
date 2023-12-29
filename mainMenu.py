import pandas as pd

import addNewMusic
import addStyle
import filterStyle
import removeSongMain
import musicReview
import prevalenceMusic
import rankingPlaylist
import bestRankStyleMain
import playlistManual
import playlistRules
import playlistAddMusic

playlist_df = pd.read_csv('data/playlist.csv')
tableMusic_df = pd.read_csv('data/tableMusic.csv')

main_menu = """
\033[1m J U K E B O T I F Y \033[0;0m
\033[1m MAIN MENU \033[0;0m
\033[1m 1 \033[0;0m manage database
\033[1m 2 \033[0;0m manage playlists
\033[1m 3 \033[0;0m quick play
\033[1m 0 \033[0;0m exit Jukebotify
 (enter a number) => """

submenu_1 = """
\033[1m J U K E B O T I F Y \033[0;0m
 main menu/\033[1mMANAGE DATABASE \033[0;0m
\033[1m 1 \033[0;0m add song to database
\033[1m 2 \033[0;0m delete song from database
\033[1m 3 \033[0;0m create new music style
\033[1m 4 \033[0;0m most popular songs in playlists
\033[1m 5 \033[0;0m highest rated songs
\033[1m 0 \033[0;0m back
 (enter a number) => """

submenu_2 = """
\033[1m J U K E B O T I F Y \033[0;0m
 main menu/\033[1mMANAGE PLAYLISTS \033[0;0m
\033[1m 1 \033[0;0m create random playlist
\033[1m 2 \033[0;0m create personalized a playlist
\033[1m 3 \033[0;0m edit a playlist
\033[1m 0 \033[0;0m back
 (enter a number) => """

submenu_2_1 = """
\033[1m J U K E B O T I F Y \033[0;0m
 main menu/manage playlists/\033[1mRANDOM PLAYLIST \033[0;0m
\033[1m 1 \033[0;0m start playback
\033[1m 0 \033[0;0m back
 (enter a number) => """

submenu_2_2 = """
\033[1m J U K E B O T I F Y \033[0;0m
 main menu/manage playlists/\033[1mPERSONALIZED PLAYLIST \033[0;0m
\033[1m 1 \033[0;0m rate song
\033[1m 2 \033[0;0m start playback
\033[1m 0 \033[0;0m back
 (enter a number) => """

submenu_2_3 = """
\033[1m J U K E B O T I F Y \033[0;0m
 main menu/manage playlists/\033[1mEDIT PLAYLIST \033[0;0m
\033[1m 1 \033[0;0m expand playlist
\033[1m 2 \033[0;0m add song to playlist
\033[1m 3 \033[0;0m remove song from playlist
\033[1m 0 \033[0;0m back
 (enter a number) => """

submenu_3 = """
\033[1m J U K E B O T I F Y \033[0;0m
 main menu\033[1m/QUICK PLAY \033[0;0m
\033[1m 1 \033[0;0m random
\033[1m 2 \033[0;0m pick playlist
\033[1m 0 \033[0;0m back
 (enter a number) => """

welcome_message = " WELCOME TO JUKEBOTIFY! "
print("\n",welcome_message.center(40, "#"))

def subMenu_1():
    second_input = -1
    while second_input != 0:
        second_input = input(submenu_1)
        match(second_input):
            case("1"):
                addNewMusic.addMusic()
            case("2"):
                removeSongMain.removeSongDatabase()
            case("3"):
                addStyle.addStyle()
            case("4"):
                prevalenceMusic.songRecurrence()
            case("5"):
                bestRankStyleMain.rankByStyle()
            case("0"):
                return
            case(_):
                subMenu_1()

def subMenu_2():
    second_input = -1
    while second_input != 0:
        second_input = input(submenu_2)
        match(second_input):
            case("1"):
                subMenu_2_1()
            case("2"):
                subMenu_2_2()
            case("3"):
                subMenu_2_3()
            case("0"):
                return
            case(_):
                subMenu_2()


def subMenu_2_1():
    playlistRules.playlistRulesFun()
    second_input = -1
    while second_input != 0:
        second_input = input(submenu_2_1)
        match(second_input):
            case("1"):
                print("NOT ADDED YET") # START PLAYING PLAYLIST
                return
            case("0"):
                return
            case(_):
                subMenu_2_1()

def subMenu_2_2():
    playlistManual.playlistManualFun()
    second_input = -1
    while second_input != 0:
        second_input = input(submenu_2_2)
        match(second_input):
            case("1"):
                musicReview.song_rating(tableMusic_df)
                return
            case("2"):
                print("NOT ADDED YET") # START PLAYING PLAYLIST
                return
            case("0"):
                return
            case(_):
                subMenu_2_2()

def subMenu_2_3():
    second_input = -1
    playlist_pick = playlistAddMusic.pickPlaylist(playlist_df)
    while second_input != 0:
        second_input = input(submenu_2_3)
        match(second_input):
            case("1"):
                songs_ids = list(playlist_df.loc[playlist_df['id_playlist'] == playlist_pick,'id_music'])
                for id in songs_ids:
                    print(tableMusic_df.loc[tableMusic_df['id_music'] == id])
            case("2"):
                playlistAddMusic.addMusic(playlist_df, tableMusic_df, playlist_pick)
            case("3"):
                removeSongMain.removeSongPlaylist(playlist_df,playlist_pick)
                return
            case("0"):
                return
            case(_):
                subMenu_2_3()

def subMenu_3():
    second_input = -1
    while second_input != 0:
        second_input = input(submenu_3)
        match(second_input):
            case("1"):
                print("NOT ADDED YET") # RANDOM PLAYBACK
                return
            case("2"):
                print("NOT ADDED YET") # PICK PLAYLIST
                return
            case("0"):
                return
            case(_):
                subMenu_3()

def mainMenu():
    first_input = -1
    while first_input != 0:
        first_input = input(main_menu)
        match(first_input):
            case("1"):
                subMenu_1()
            case("2"):
                subMenu_2()
            case("3"):
                subMenu_3()
            case("0"):
                return
            case(_):
                mainMenu()
mainMenu()
