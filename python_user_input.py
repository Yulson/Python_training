my_name = "Jose"
your_name = input("Enter your name: ")
print(f"Hello, {your_name}")

age = input("Enter your age: ")
print(f"You have lived for {age * 12} months.")

age = input("Enter your age again: ")
age_num = int(age)
print(f"You have lived {age_num * 12} months")

age = int(input("Enter your age: "))
months = age*12
print(f"You have lived for {months} months")

"""
Calculate the number of seconds
"""
age = int(input("Enter your age:"))
months = age * 12
days = age * 365
hours = age * 364 * 24
minutes = age * 364 * 24 * 60
seconds = age * 364 * 24 * 60 * 60
print(f"You have lived {seconds} seconds.")