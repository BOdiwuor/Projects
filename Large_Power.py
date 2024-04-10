#Create a function named large_power() that takes two parameters named base and exponent.

#If base raised to the exponent is greater than 5000, return True, otherwise return False


def large_power(base, exponent):
  if base ** exponent > 5000:
    return True # prevents from creating an extra variable
  else:
    return False


print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False