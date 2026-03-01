''' Enter movies into a list '''

movies = []

for i in range(3):
    movie = input("Enter a favourite movie: ")
    movies.append(movie)

for j in range(len(movies)):
    print(f"{j+1} : {movies[j]}")
