# Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number 
# (as the 0th element) down to 0 (as the last element).

def countdown(num):
  for x in range(num, 0, -1):
    print (x)
  


# Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2

def print_and_return(arr):
  print (arr[0])
  return arr[1]


#   First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

def first_plus_length(arr):
  return arr[0] + len(arr)

#   Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater 
# than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]

def greater(arr):
  sub_arr = []
  if len(arr) == 0:
    return False
  for x in arr:
    if arr[x] > arr[1]:
      sub_arr.append(arr[x])
  print(sub_arr)
  print(len(sub_arr))


#   This Length, That Value - Write a function that accepts two integers as parameters: size and value. 
# The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def this_that(num1, num2):
  sub_arr = []
  if num1 == num2:
    print('Jinx')
  
    sub_arr.append(num2)
  return sub_arr