def search(b):
    # Loop over all possible digits for A, B, and C (distinct digits)
    for A in range(10):
        for B in range(10):
            for C in range(10):
                # Ensure that A, B, and C are distinct
                if A != B and A != C and B != C:
                    # Calculate the decimal value of ABC
                    ABC_10 = 100 * A + 10 * B + C
                    # Calculate the value of CBA in base b
                    CBA_b = C * (b ** 2) + B * b + A

                    # Check if they are equal
                    if ABC_10 == CBA_b:
                        return True

    return False


# Test cases
print(search(10))  # False
print(search(11))  # False
print(search(14))  # True
print(search(15))  # False
