def first_character(string):
    # Complete the return statement using a string operation.
    return string[0] 


print(first_character("Hello, World")) # Should print H
print(first_character("Python is awesome")) # Should print P
print(first_character("Keep going")) # Should print K


def alpha_length(string):
    character = ""
    count_alpha = 0
    # Complete the for loop sequence to iterate over "string".
    for i in string: 
        # Complete the if-statement using a string method. 
        if i.isalpha():
            count_alpha += 1  
    return count_alpha
 
print(alpha_length("This has 1 number in it")) # Should print 17
print(alpha_length("Thisisallletters")) # Should print 16
print(alpha_length("This one has punctuation!")) # Should print 21


def sort_distance(distances):
    distances = sorted(distances, reverse = True)
    return distances


print(sort_distance([2,4,0,15,8,9]))
# Should print [15, 9, 8, 4, 2, 0]

def increments(start, end):
    return [ i+2 for i in range(start,end+1) ] # Create the required list comprehension.


print(increments(2, 3)) # Should be [4, 5]
print(increments(1, 5)) # Should be [3, 4, 5, 6, 7]
print(increments(0, 10)) # Should be [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def countries(countries_dict):
    result = ""
    # Complete the for loop to iterate through the key and value items 
    # in the dictionary.
    for keys, values in countries_dict.items():
        # Use a string method to format the required string.
        result += str(values)+"\n"
    return result

print(countries({"Africa": ["Kenya", "Egypt", "Nigeria"], "Asia":["China", "India", "Thailand"], "South America": ["Ecuador", "Bolivia", "Brazil"]}))

# Should print:
# ['Kenya', 'Egypt', 'Nigeria']
# ['China', 'India', 'Thailand']
# ['Ecuador', 'Bolivia', 'Brazil']


def check_guests(guest_list, guest):
  return guest_list[guest] # Print the valuefor the s given key


guest_list = { "Adam":3, "Camila":3, "David":5, "Jamal":3, "Charley":2, "Titus":1, "Raj":6, "Noemi":1, "Sakira":3, "Chidi":5}


print(check_guests(guest_list, "Adam")) # Should print 3
print(check_guests(guest_list, "Sakira")) # Should print 3
print(check_guests(guest_list, "Charley")) # Should print 2




def setup_gradebook(old_gradebook):
  # Use a dictionary method to create a new copy of the "old_gradebook".
  new_gradebook = old_gradebook.copy() 
    # Complete the for loop to iterate over the new gradebook. 
  for i, j in new_gradebook.items():
      # Use a dictionary operation to reset the grade values to 0.
      new_gradebook[i]=0
  return new_gradebook

fall_gradebook = {"James": 93, "Felicity": 98, "Barakaa": 80}
print(setup_gradebook(fall_gradebook))
# Should output {'James': 0, 'Felicity': 0, 'Barakaa': 0}


speed_limits = {"street": 35, "highway": 65, "school": 15}
speed_limits["highway"]

len("")