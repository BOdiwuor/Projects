#Create a function named twice_as_large() that has two parameters named num1 and num2.

#Return True if num1 is more than double num2. Return False otherwise.


def twice_as_large(num1, num2):
  if num2*2 < num1:
    return True
  else:
    return False

print(twice_as_large(10, 5))
# should print False
print(twice_as_large(11, 5))
# should print True