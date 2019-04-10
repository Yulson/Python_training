nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set()  
# This is an empty set, like {}

custom_friend_name = input("Input the name of your friend: ")
# Ask the user for the name of a friend

user_friends.add(custom_friend_name,)
# Add the name to the empty set

print(nearby_people.intersection(user_friends))
# Print out the intersection between both sets. This gives us a set with those friends that are nearby.
