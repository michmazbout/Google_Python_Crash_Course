number = 15 # Initialize the variable
while number >= 5: # Complete the while loop condition
    print(number, end=" ")
    number -= 5 # Increment the variable

# Should print 15 10 5 

for number in range(5,-1,-1):
    print(number)

# Should print:
# 5
# 4
# 3
# 2
# 1



# 0def even_numbers(n):
    count = 0
    current_number = 0
    while current_number <= n: # Complete the while loop condition
        if current_number % 2 == 0:
            count += 1 # Increment the appropriate variable
        current_number += 1 # Increment the appropriate variable
    return count
    
print(even_numbers(25))   # Should print 13
print(even_numbers(144))  # Should print 73
print(even_numbers(1000)) # Should print 501
print(even_numbers(0))    # Should print 1


def rows_asterisks(rows):
    # Complete the outer loop range to control the number of rows
    for x in range(1,rows + 1): 
        # Complete the inner loop range to control the number of 
        # asterisks per row
        for y in range(1, x+1): 
            # Prints one asterisk and one space
            print("*", end=" ")
        # An empty print() function inserts a line break at the 
        # end of the row 
        print()


rows_asterisks(5)
# Should print the asterisk rows shown above


def divisible(max, divisor):
    count = 0 # Initialize an incremental variable
    for x in range(0,max): # Complete the for loop
        if x % divisor == 0:
            count += 1 # Increment the appropriate variable
    return count

print(divisible(100, 10)) # Should be 10
print(divisible(10, 3)) # Should be 4
print(divisible(144, 17)) # Should be 9


def odd_numbers(maximum):
    
    return_string = "" # Initializes variable as a string

    # Complete the for loop with a range that includes all 
    # odd numbers up to and including the "maximum" value.
    for odd in range(maximum+1): 

        # Complete the body of the loop by appending the odd number
        # followed by a space to the "return_string" variable.
        if odd%2 != 0:
            return_string = return_string+" "+str(odd)  

    # This .strip command will remove the final " " space 
    # at the end of the "return_string".
    return return_string.strip()


print(odd_numbers(6))  # Should be 1 3 5
print(odd_numbers(10)) # Should be 1 3 5 7 9
print(odd_numbers(1))  # Should be 1
print(odd_numbers(3))  # Should be 1 3
print(odd_numbers(0))  # No numbers displayed
