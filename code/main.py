import pandas as pd
import seaborn as sns
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import sys
text  = " ".join(sys.stdin)
#print(text)
#text = open( '../l1.txt').read()
# Generate a word cloud image
wordcloud = WordCloud().generate(text)

# # Display the generated image:
# # the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig("../img/"+sys.argv[1]+".png")