import requests
from bs4 import BeautifulSoup
URL= "https://www.azlyrics.com/lyrics/tylerthecreator/foreword.html"
#URL ="https://www.azlyrics.com/lyrics/tylerthecreator/911mrlonely.html"
#URL ="https://www.azlyrics.com/lyrics/radiohead/highdry.html"
URL = "https://www.azlyrics.com/lyrics/eltonjohn/rocketmanithinkitsgoingtobealonglongtime.html"
class_div = "Lyrics__Container-sc-1ynbvzw-6 YYrds"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")


results = soup.find_all("div",class_="ringtone")
print("vacio") if results is None else print("")
lyrics_raw = results[0].find_next_sibling("div")
print(lyrics_raw.get_text())