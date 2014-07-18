import urllib
from bs4 import BeautifulSoup

htmltext = urllib.urlopen("http://www.melon.com/chart/index.htm").read()
soup = BeautifulSoup(htmltext, from_encoding="utf-8")
music_title = []

for tag in soup.select(".wrap_song_info"):
	music_title.append(tag.get_text())


	for author in music_title:
		print author.encode("UTF-8")

