import imdb

moviesDB = imdb.IMDb()


#print(dir(moviesDB))
# ----------------------------------------
# Search for a movie title
movies = moviesDB.search_movie('inception')

# print('Searching for "inception":')
# for movie in movies:
#     title = movie['title']
#     year = movie['year']
#     print(f'{title} - {year}')


#print(movies[0].keys())
    


# ----------------------------------------
# List movie info
id = movies[0].getID()
movie = moviesDB.get_movie(id)

title = movie['title']
year = movie['year']
rating = movie['rating']
directors = movie['directors']
casting = movie['cast']

# print('Movie info:')
# print(f'{title} - {year}')
# print(f'rating: {rating}')

# direcStr = ' '.join(map(str,directors))
# print(f'directors: {direcStr}')

# actors = ', '.join(map(str, casting))
# print(f'actors: {actors}')


#print(movie.keys())
# ----------------------------------------
# List actor info
id = casting[0].getID()
person = moviesDB.get_person(id)
bio = moviesDB.get_person_biography(id)

name = person['name']
birthDate = person['birth date']
height = person['height']
trivia = person['trivia']
titleRefs = bio['titlesRefs']

# print(f'name: {name}')
# print(f'birth date: {birthDate}')
# print(f'height: {height}')
# print(f'trivia: {trivia[0]}')

# titleRefsStr = ', '.join(map(str, titleRefs))
# print(f'bio title refs: {titleRefsStr}')


#print(dir(casting[0]))
#print(person.keys())


#print(bio.keys())
#print(bio['titlesRefs'].keys())
# ----------------------------------------
#Get top/bottom 10 movies
top = moviesDB.get_top250_movies()
bottom = moviesDB.get_bottom100_movies()

print('Top 10 movies:')
for movie in top[0:9]:
	print(movie)
print()

print('Bottom 10 movies:')
for movie in bottom[0:9]:
	print(movie)

