import imdb

hr = imdb.IMDb()                                          # Create an object of class IMDb

movie_Name = input("Enter the Movie Name")
movies = hr.search_movie(str(movie_Name))                 # Search the given Movie

index = movies[0].getID()                                 # Get the ID of the given Movie for searching
movie = hr.get_movie(index)                               # Search the movie with the ID

title = movie['title']
year_of_release = movie['year']
cast = movie['cast']

list_of_cast = ','.join(map(str,cast))

print("Title: ", title)
print("Year of Release: ",year_of_release)
print("Cast: ", list_of_cast)
