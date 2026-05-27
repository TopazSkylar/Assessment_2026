import csv
import random


def get_song_var():
    """
    From the csv
    :return:
    """
    file = open("lyric_list.csv")
    all_vars = list(csv.reader(file, delimiter=","))
    file.close()
    # remove the first row
    all_vars.pop(0)
    return all_vars


def get_round_lyrics():
    # grab all the info from the csv
    all_song_list = get_song_var()

    round_song = []
    final_round_song = []


    # loop until we got them songs for each round
    while len(round_song) < 4:
        potential_song = random.choice(all_song_list)

        # Get the songs and check it's not a duplicate
        if potential_song[0] not in final_round_song:
            round_song.append(potential_song)
            final_round_song.append(potential_song[0])
    # everything
    print(f"List of songs, lyrics, album {round_song}")
    # final
    print(f"List of songs chosen {final_round_song}")

    # takes rand song from select
    questioned_song = random.choice(round_song)
    questioned_lyrics = questioned_song[1]  # The Randomly take the lyrics of all the generated songs and have it be the correct ans
    album = questioned_song[2]  # The album


    # this will be the question
    print(f"questioned_lyrics =  {questioned_lyrics}, album = {album}")


get_song_var()
get_round_lyrics()
