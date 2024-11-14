import pandas as pd
import seaborn as sns
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import lyricsgenius as lg

K = 1  # Number of songs to retrieve
name = "Metallica"
def search_lyrics(artist: str) -> str:
    """
    This function retrieves the lyrics of the most popular song by a given artist,
    generates a word cloud image from the lyrics, and saves it as a PNG file.
    It then returns an HTML string that displays the saved image.

    Parameters:
    artist (str): The name of the artist whose song's lyrics will be retrieved.

    Returns:
    str: An HTML string containing the title of the song and an image tag pointing to the saved PNG file.
    """
    # Create a Genius object
    genius = lg.Genius('4XlLAe5wuw8CZQsIrMpf5HjMu2su7SKwKDK-FLLSE6Qvdlx2NYpQoUwFHhnM_Fyr',  # Client access token from Genius Client API page
                             skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"],
                             remove_section_headers=True)
    # Get the songs
    songs = (genius.search_artist(artist, max_songs=K, sort='popularity')).songs
    # Songs objects
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
