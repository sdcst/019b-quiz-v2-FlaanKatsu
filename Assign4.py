#!python3
"""
Billy is inviting people to his party.  He is accepting requests
from his friends, but only wants to send 1 invitation out per
person. He decides to store names in a list, and only add the
ones that are not already there.  Can you help a brother out?

Your program should keep asking the user to enter in a name 
(first and last).  If the name is not on the list, add it,
otherwise say "That name is already on the list".

if the user enters in a blank line, then stop the input.
Sort the list of names (it will be sorted by first name)
and print out all of the names on the list.  Also print out
the number of names on the list so he knows how many 
invitations to send.

This program will require you to incorporate everything we
have learned so far.
"""
friends = []
done = 0
while done == 0:
 inF = str(input("Please input a name(full name): "))
 if inF in friends:
  print("error: Friend is already on your list!")
 elif inF == "":
  done = 1
 else:
  friends.append(inF)
if done == 1:
 friends.sort()
 nFriends = len(friends)
 print("The friends to invite are ", end="")
 for i in range(0,nFriends-1):
  print(f"{friends[i]}, ", end="")
 print(f"and {friends[i+1]}", end="")
 print(f", for a a total of {nFriends} friends.")