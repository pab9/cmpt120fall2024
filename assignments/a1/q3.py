# q3.py

#
# Full Name: Paige Brooks
#  SFU ID #: 301426363
# SFU Email: pab9@sfu.ca
#

# ... put your answer to question 3 here ...

#user input
message = input("What do you want your sign to say? ")
box_character = input("What character do you want for the box? ")

# calculate box dimensions
width = len(message) + 4 #adds 2 for spaces and borders

#print borders
print(box_character * width)
print(f"{box_character} {message} {box_character}")
print(box_character * width)
