import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import sys
#Extract the name of the file from the arguments
#file_name = sys.argv[1]

lines = []

for line in sys.stdin:
    lines.append(line
    .replace(",","")
    .replace(")","")
    .replace("(","")
    .replace("[","")
    .replace("]","").split(" "))
words = [item for word in lines for item in word]
words = list(map( lambda x : x.replace("\n",""),words))
#Build the stopwords list
stop = []
with open('stop.txt') as f:
    stop = f.read().split("\n")

# #Eliminar los articulos de la lista
words_clean = [word for word in words if word not in stop]
words_clean
text = " ".join(words_clean)
print(text)