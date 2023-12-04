import pandas as pd
import bestRankStyle

tableMusic = pd.read_csv('tableMusic.csv')
print("Here are the music Styles:")
print(pd.unique(tableMusic["style"]))
styleInput = input("Enter a music style:")
songStyle = bestRankStyle.getSongsOfStyle(tableMusic,styleInput)
bestRankStyle = bestRankStyle.rankingStyle(songStyle)
print("Here ara the best ranking "+styleInput+" songs: ")
print(bestRankStyle)


