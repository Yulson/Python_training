lottery_numbers = {13, 21, 22, 5, 8}

players = [ 
  {
    'name': 'John',
    'numbers': {13, 27, 21, 29, 14, 8} 
  },
  {
    'name': 'Piter',
    'numbers': {21, 27, 28, 29, 30, 1}
  }
]

mathcing_num_one = lottery_numbers.intersection(players[0]['numbers'])

matching_num_two = lottery_numbers.intersection(players[1]['numbers'])

len1 = str(len(mathcing_num_one))

len2 = str(len(matching_num_two))

print('Player ' + players[0]['name'] + ' got ' + len1 + ' numbers right.')

print('Player ' + players[1]['name'] + ' got ' + len2 + 'numbers right.')


"""
A player looks like this:

{
    'name': 'PLAYER_NAME',
    'numbers': {1, 2, 3, 4, 5}
}

Define a list with two players (you can come up with their names and numbers).
"""
#players = []

"""
For each of the two players, print out a string like this: "Player PLAYER_NAME got 3 numbers right.".
Of course, replace PLAYER_NAME by their name, and the 3 by the amount of numbers they matched with lottery_numbers. We still cannot use f-strings in this exercise.
You'll have to access each player's name and numbers, and calculate the intersection of their numbers with lottery_numbers.
Then construct a string and print it out.

Remember: the string must contain the player's name and the amount of numbers they got right!
"""
