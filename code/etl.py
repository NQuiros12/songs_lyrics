import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import sys
#Extract the name of the file from the arguments
file_name = sys.argv[1]

lines = []
with open('../data/'+file_name) as f:
    words = f.read().replace(",","").replace(")","").replace("(","").split(" ")
words = list(map( lambda x : x.split("\n"),words))
words = [item for word in words for item in word]

#Build the stopwords list
stop = []
with open('stop.txt') as f:
    stop = f.read().split("\n")

#Eliminar los articulos de la lista
stop_words = ["a","en","las","el","de","lo", "un","te","la","que","es"]
words_clean = [word for word in words if word not in stop_words]
words_clean
text = " ".join(words_clean)
print(text)