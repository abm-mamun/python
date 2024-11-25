fav_movies = ["Fight Club", "Bullet Train", "Dune"]

print(len(fav_movies))

#adding new item to lists
fav_movies.append("Iron Man")

print(len(fav_movies))

print(fav_movies)

#adding new item to list in a specific position
fav_movies.insert(1, "Top Gun")

print(fav_movies)

#deleting new item from list in a specific position
del(fav_movies[2])

print(fav_movies)

del(fav_movies[0])
del(fav_movies[0])
del(fav_movies[0])

print(fav_movies)
