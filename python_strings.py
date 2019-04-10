my_string = "Hello, world!"
escaped_quptes = "He said \"You are amazing!\" yesterday"


name = "Jose"
greeting = "Hello, " + name
print(greeting)

another_greeting = f"Hello, {name}"
print(another_greeting)

final_greeting = "How are you, {}"
formatted_greeting = final_greeting.format(name)
print(formatted_greeting)