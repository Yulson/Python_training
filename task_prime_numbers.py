
cars = ["ok", "ok", "ok", "fault", "ok", "ok"]
for car_status in cars:
  if car_status == "fault":
    print("Stop production!")
    break
  print(f"Car status is {car_status}")
#Go through the list of cars, and print the status. If the car is broaken, print "Stop production" and terminate the cycle.
print("!!!!!!!!!!!!!!!!!!!!!!")

cars = ["ok", "ok","faulty","ok","ok"]
for car_status in cars:
  if car_status == "faulty":
    print(f"WARNING! The car status is {car_status}")
    continue
  print (f"Car status is {car_status}")

#See the difference between break and continue in cycle

print("!!!!!!!!!!!!!!!!!!!!!!")
for num in range(2,27): #[0, 1, 2, 3, ... 26, 27]
  for x in range(2,num): #[], [1], [1, 2], [1, 2, 3]
      if num % 2 == 0:
        print(f"Number {num} is not primer")
        break
  else:
      print(f"Number {num} is primer")

#Check the range of integers and print out if the integer is a prime number.