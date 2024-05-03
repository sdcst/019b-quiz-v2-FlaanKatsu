"""
Write a program that uses a for loop.
Each iteration will ask the user to enter a name
Add the input to the provided list
"""
names = []
s1 = 0
while s1 == 0:
 try:
  n = int(input("Please enter the amount of names to enter: "))
  s1 = 1
 except:
  print("Error: you have not inputted an intager!")
  s1 = 0
if s1 == 1:
 for i in range (0,n):
  ya = input(f"Please enter name {i+1} of {n}: ")
  names.append(ya)
print(names)