'''
Create a function hasSortedDigits which accepts a single integer parameter and returns true or false,
according to whether the digits (to base 10) in the parameter are sorted in strictly ascending order, starting at the lowest-valued digit.

For example:

Test	Result
print(hasSortedDigits(123));	False
print(hasSortedDigits(321));	True
print(hasSortedDigits(6544));	False
'''
def hasSortedDigits(num):
    num_str = str(num)
    for i in range(len(num_str)-1):
        if int(num_str[i]) <= int(num_str[i+1]):
            return False
    return True

# Test cases
print(hasSortedDigits(123))  # False
print(hasSortedDigits(321))  # True
print(hasSortedDigits(6544))  # False

# Test cases
print(hasSortedDigits(123))  # Output: False
print(hasSortedDigits(321))  # Output: True
print(hasSortedDigits(6544))  # Output: False
print(hasSortedDigits(0))    # Output: True
print(hasSortedDigits(1111))  # Output: True
print(hasSortedDigits(987654321))  # Output: True
#print(hasSortedDigits(-123)) # Output: False (since -123 is not sorted ascending)