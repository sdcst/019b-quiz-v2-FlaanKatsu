#!python3
# Write a program that uses a for loop to ask the user to enter
# in 5 numbers.  The program will determine the sum of the 5 numbers
# and calculate the average
# You must use only 1 input statement in your program
na = 0
for i in range(0,5):
 try:
  n = float(input(f"Please enter in 5 numbers (number {i+1} of 5): "))
 except:
  print("error: you did not enter a valid number!")
 na = na + n
nan = na/5
print(f"The average of the numbers you have inputted is {nan}.")
