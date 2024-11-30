def recurse(stateA, stateB, move_count, max_it):
    # Base case: If A = 1, we've reached the terminal state
    if stateA == 1:
        return 1

    # If we've reached the maximum number of iterations, return 0
    if move_count >= max_it:
        return 0

    # Initialize the number of ways to reach the terminal state
    ways = 0

    # Transitions for A:
    if stateA == 0:
        # A = 0 can transition to A = 1
        move_count = move_count + 1
        ways += recurse(1, stateB, move_count, max_it)

    # Transitions for B:
    if stateB == 0:
        # B = 0 -> B = 1
        ways += recurse(stateA, 1, move_count + 1, max_it)
    elif stateB == 1:
        # B = 1 -> B = 0 or B = 2
        ways += recurse(stateA, 0, move_count + 1, max_it)
        ways += recurse(stateA, 2, move_count + 1, max_it)
    elif stateB == 2:
        # B = 2 -> B = 1 or B = 3
        ways += recurse(stateA, 1, move_count + 1, max_it)
        ways += recurse(stateA, 3, move_count + 1, max_it)
    elif stateB == 3:
        # B = 3 -> B = 2 or B = 4
        ways += recurse(stateA, 2, move_count + 1, max_it)
        ways += recurse(stateA, 4, move_count + 1, max_it)
    elif stateB == 4:
        # B = 4 -> B = 3
        ways += recurse(stateA, 3, move_count + 1, max_it)

    return ways


# Test cases

print(recurse(0, 2, 0, 2))  # Expected result: 2
