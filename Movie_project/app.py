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


def menu()
    user_input = input("Pdint a - to add a movie, v - to view the entire list of movies, f - to find a particular movie and q - to quite :")
    while user_input != 'q':
      if user_input == 'a':
        add_movie()
      elif: user_input == 'f'
        find_movie()
      elif: user_input == 'v'
        view_movies_list()
        