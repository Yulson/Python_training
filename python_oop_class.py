# Define a Movie class that has two properties: name and director


# You should be able to create Movie objects like this one:
#my_movie = Movie('The Matrix', 'Wachowski')

class Movie:
    def __init__(self, new_name, new_director):
      self.name = new_name
      self.director = new_director

    def print_info(self):
      print('<<{}>> by {}'.format(self.name, self.director))

 # let's try to add a method `print_info()` here:


my_movie = Movie('The Matrix', 'Wachowski')


