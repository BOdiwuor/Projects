#Create a function called divisible_by_ten() that has one parameter named num.

#The function should return True if num is divisible by 10, and False otherwise. Consider using modulo operator % to check for divisibility.


# Write your divisible_by_ten() function here:
#We know a number is divisible by another number of the remainder is 0. 0 needs to be part of the if condition to return the correct values.

def divisible_by_ten(num):
  if (num % 10 == 0):
    return True
  else:
    return False


print(divisible_by_ten(20))
# should print True
print(divisible_by_ten(25))
# should print False