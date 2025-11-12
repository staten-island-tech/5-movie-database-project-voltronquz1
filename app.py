import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

# for index, item in enumerate(data):
#     print(index, ':', item["title"])
# choice=int(input("Give me a movie year in that database "))
# file two
# for i in data:
#     if i['year'] > choice:
#         print(i['title']) 

# file 3
# for i in data:
#     if i['year'] > choice < i['year']:
#         print(i["title"])
# file 4
# for i in data:
#     if i['year']==choice:
#         print(i['title'])

#  file 5
# counter=0
# choice=input("Give me a word to look for movie with that word: ")
# for i in data:
#     if  choice.lower() in i['title'].lower():
#         print(i['title'])
#         counter+=1
#     elif counter <=0:
#         print("There is nothing with that keyword give me something else")
#         input("Give me another word")
#         if  choice.lower() in i['title'].lower():
#             print(i['title'])
#              counter+=1
# file 6
# choice=input("Give me a word to look for a genre with that word: ")
# for i in data:
#     if choice.capitalize() in i['genres']:
#         print(i['title'])