#   Skill Group 1:
#            Use variables to store values
#            Use basic arithmetic operators with variables to create expressions
#            Use explicit conversion to change a data type from float to string

# The following lines assign the variable to the left of the = 
# assignment operator with the values and arithmetic expressions 
# on the right side of the = assignment operator.
hotel_room = 100
tax = hotel_room * 0.08
total = hotel_room + tax
room_guests = 4
share_per_person = total/room_guests


# This line outputs the result of the final calculation stored
# in the variable "share_per_person"
print("Each person needs to pay: " + str(share_per_person)) # change a data type


#   Skill Group 2:
#               Output multiple string variables on a single line to form a sentence
#               Use the plus (+) connector or a comma to connect strings in a print() function
#               Create spaces between variables in  a print() function

# The following 5 lines assign strings to a list of variables.
salutation = "Dr."
first_name = "Prisha"
middle_name = "Jai"
last_name = "Agarwal"
suffix = "Ph.D."
 
print(salutation + " " + first_name + " " + middle_name + " " + last_name + ", " + suffix) 
# The comma as a string ", " adds the conventional use of a comma plus a 
# space to separate the last name from the suffix.
 
# Alternatively, you could use commas in place of the + connector:
print(salutation, first_name, middle_name, last_name,",", suffix)
# However, you will find that this produces a space before a comma within a string.



#   Skill Group 3:
#               Resolve TypeError caused by a data type mismatch issue
#               Use an explicit conversion function


# The following code causes a type error between a string 
# and an integer:
# print("5 * 3 = " + (5*3)) 


# Resolution: 
print("5 * 3 = " + str(5*3))
#
# To avoid a type error between the string and the integer within the
# print() function, you can make an explicit data type conversion by
# using the str() function to convert the integer to a string.  