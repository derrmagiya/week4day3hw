# problem 1:
# Write a function that checks if a given string (case insensitive) is a palindrome. A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards, such as madam or racecar, the date and time 12/21/33 12:21, and the sentence: "A man, a plan, a canal – Panama".

#def is_palindrome(string):
    #processed_string = ''.join(c.lower() for c in string if c.isalnum())
    #return processed_string == processed_string[::-1]
#test_string = "A man, a plan, a canal – Panama"
#print(is_palindrome(test_string))

# Refactored
def is_palindrome(string):
    left = 0
    right = len(string) - 1

    while left < right:
        while left < right and not string[left].isalnum():
            left += 1
        while left < right and not string[right].isalnum():
            right -= 1

        if string[left].lower() != string[right].lower():
            return False

        left += 1
        right -= 1

    return True

test_string = "A man, a plan, a canal – Panama"
print(is_palindrome(test_string))

# problem 2:
# Terminal game move function
#In this game, the hero moves from left to right. The player rolls the dice and moves the number of spaces indicated by the dice two times.

#Create a function for the terminal game that takes the current position of the hero and the roll (1-6) and return the new position.

#Example:
#move(3, 6) should equal 15 

# def move(position, roll):
    #return position + roll * 2
#current_position = 3
#roll_value = 6

#new_position = move(current_position, roll_value)
#print(new_position)  

# Refactored

def move(position, roll):
    return position + (roll << 1)

current_position = 3
roll_value = 6

new_position = move(current_position, roll_value)
print(new_position)

# problem 4
# Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

#For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

# [10, 343445353, 3453445, 3453545353453] should return 3453455. 


#def sum_two_smallest_numbers(numbers):
    #sorted_numbers = sorted(numbers)
    
    #return sorted_numbers[0] + sorted_numbers[1]
#numbers = [19, 5, 42, 2, 77]
#result = sum_two_smallest_numbers(numbers)
#print(result)  
#numbers = [10, 343445353, 3453445, 3453545353453]
#result = sum_two_smallest_numbers(numbers)
#print(result)   

# Refactored

def sum_two_smallest_numbers(numbers):
    min1 = min(numbers)
    numbers.remove(min1)
    min2 = min(numbers)
    
    return min1 + min2

numbers = [19, 5, 42, 2, 77]
result = sum_two_smallest_numbers(numbers)
print(result)

numbers = [10, 343445353, 3453445, 3453545353453]
result = sum_two_smallest_numbers(numbers)
print(result)

   