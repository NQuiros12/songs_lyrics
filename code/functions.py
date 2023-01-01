import pandas as pd
import seaborn as sns
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import sys
import lyricsgenius as lg
#Create a Genius object
name = "Metallica"
K = 1
def search_lyrics(artist:name):
    #Create a Genius object
    genius = lg.Genius('4XlLAe5wuw8CZQsIrMpf5HjMu2su7SKwKDK-FLLSE6Qvdlx2NYpQoUwFHhnM_Fyr',  # Client access token from Genius Client API page
                             skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"],
                             remove_section_headers=True)
    #Get the songs
    songs = (genius.search_artist(name, max_songs=K, sort='popularity')).songs
    #Songs objects
    text = songs[0].lyrics

    # Generate a word cloud image
    wordcloud = WordCloud().generate(text)

    # Display the generated image:
    # the matplotlib way:

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig("../img/"+songs[0].title+".png")
    return """
        <html>
        <head>
            <title>Imagen</title>
        </head>
        <body>
            <h1>Look ma!</h1>
            <img src = "../img/%s.png"</img>
        </body>
    </html>
    """%(songs[0].title)
