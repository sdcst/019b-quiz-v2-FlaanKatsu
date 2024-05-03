#!python3
"""
Fix this program.
It should ask the user to enter in 10 numbers and see
if the number is positive or negative
"""
for n in range(10):
 a = float(input("Please input a number: "))
 if a > 0:
  print('that is a positive number')
 elif a < 0:
  print('that is a negative number')
 elif a == 0:
  print("error: your number is zero!")