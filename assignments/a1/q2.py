# q2.py

#
# Full Name: Paige Brooks
#  SFU ID #:301426363
# SFU Email: pab9@sfu.ca
#

# ... put your answer to question 2 here ...
#conversion from feet to meters
conversion = 0.3048

#user input
feet =float(input("How many feet? "))

#convert to meters
meters = feet * conversion

#printresult using f-string for one decimal place
print(f" {feet:.1} is about {meters:.1f} meters.")
