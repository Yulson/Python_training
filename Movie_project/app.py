"""
Is to create a movie storage application, that will allow users to manage their movie collection and  nd any movie they want.
Here’s the three main features:
• First, the application must allow to add new movies to the collection;
• The application must allow users to view all the movies in their collection;
• The application must also allow users to find any particular movie by any of its attrib- utes (more info in the next page...)
"""
"""
List of tasks:
1. Allow user to chose from the menu: add new movie, view all the movies in collection, find a particular movie.
2. User should be able to add a movie
3. User should be able to view the complete list of all added movies
4. User should be able to find a particular movie by name.
5. User should be able to quit the menu.
"""
"""
movies = []
movie = {
     'name' = ... (str),
     'genre' = ... (str),
     'year' = ... (int)
     'rating' = ... (int)
}
"""
movies = []

def menu():
    user_input = input("Enter a to add a movie, l to see your movies, f to find a movie, and q - to quite: ")

    while user_input != 'q':
      if user_input == 'a':
        add_movie()
      elif user_input == 'f':
        find_movie()
      elif user_input == 'l':
        show_movies()
      else:
          print("Unknown command. Please, try again.")
      user_input = input("Enter a to add a movie, l to see your movies, f to find a movie, and q - to quite: ")



def add_movie():
    name = input("Enter a movie name: ")
    genre = input("Enter a movie genre: ")
    year = int(input("Enter a year of production: "))
    rating = int(input("Enter your rate from 0 to 10: "))

    movies.append({
        'name': name,
        'genre': genre,
        'year': year,
        'rating': rating
    })


def show_movies():
    for movie in movies:
        show_movie_details(movie)


def show_movie_details(movie):
    print(f"Name: {movie['name']}")
    print(f"Genre: {movie['genre']}")
    print(f"Release year: {movie['year']}")
    print(f"Rating: {movie['rating']}")
    print("==============")

def find_movie():
    find_by = input("What property of the movie are you looking for? ")
    looking_for = input("What are you searching for ")
    found = []

    for movie in movies:
        if movie[find_by] == looking_for:
            found.append(movie)
    print(found)
    return found

menu()

