from bs4 import BeautifulSoup
import codecs

name = "korea"
play_list1 = codecs.open("./" + name + ".html")
# play_list2 = codecs.open("./" + name + "2.html")
moody_list = open(name + ".txt", "w")

song_map = {}

soup = BeautifulSoup(play_list1.read(), "html.parser")
for row in soup.find_all("tr"):
    col = row.find("td")
    if (col):
        title = col.find_next_sibling("td")

        if (title):
            title_string = title.find("span")
            artist = title.find_next_sibling("td").find_next_sibling("td").find("span").find("a")
            try:
                song_map[title_string.contents[1]] = artist.contents[0]        
            except:
                print("left them alone..")
            
# soup = BeautifulSoup(play_list2.read(), "html.parser")
# for row in soup.find_all("tr"):
#     col = row.find("td")
#     if (col):
#         title = col.find_next_sibling("td")

#         if (title):
#             title_string = title.find("span")
#             artist = title.find_next_sibling("td").find_next_sibling("td").find("span").find("a")
#             try:
#                 song_map[title_string.contents[1]] = artist.contents[0]        
#             except:
#                 print("left them alone..")
        
for k, v in song_map.items():
    moody_list.write(k + " - " + v + "\n")

moody_list.close()