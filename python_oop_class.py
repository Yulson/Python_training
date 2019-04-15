my_student = {
  'name': 'Rolf Smith',
  'grades': [70, 88, 90, 99]
}

def avarage_grade(student):
  return sum(student['grades']) / len(student['grades'])

print(avarage_grade(my_student)) 

# Define a Movie class that has two properties: name and director


# You should be able to create Movie objects like this one:
#my_movie = Movie('The Matrix', 'Wachowski')

class Movie:
    def __init__(self, new_name, new_director):
      self.name = new_name
      self.director = new_director


# We have a class called Club, and it is initialized like this (no need to change):
class Club:
    def __init__(self, name):
        self.name = name
        self.players = []

    # define a method that allows us to access the i-th player in the club directly via indexing.
    # for example, if some_club is an object of Club class,
    # we can access the i-th player in some_club like this (you may assume i is always valid):
    # some_club[i]

    def __getitem__(self,i):
       return self.players[i]

    # define a method that returns a readable string representation of this object for the user.
    # The return value should be in such format (beware of the spacing):
    # Club {club_name} with {count_of_players} players
    # the club_name and count_of_players should be replaced by the according value of current object

    def __str__(self):
        return 'Club {} with {} players'.format(self.name, len(self))

    # define a method that returns a string representation of this object,
    # which can be used to recreate this object.
    # The return value should be in such format (beware of the spacing):
    # Club {club_name}: {list_of_players}
    # the club_name and list_of_players should be replaced by the according value of current object 
    def __repr__(self):
        return 'Club {}: {}' .format(self.name, self.players)
    



club_one = Club('Dnipro')
club_two = Club('Obolon')

club_one.players.append('Alex')
club_one.players.append('Oleg')

print(club_one.players)
print(club_one.players[1])
print(club_one)
print(club_one.__str__)
