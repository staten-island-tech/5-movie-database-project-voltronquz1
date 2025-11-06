import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

for index, item in enumerate(data):
    print(index, ':', item["title"])
choice=input("Give me a movie year in that database ")
for movie in data:
    if movie('year') > choice:
        print(movie('title'))
for movie in data:
    if movie('year')