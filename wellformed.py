def wellformed(s):
    matching_pairs = {')': '(', ']': '[', '}': '{', '>': '<'}
    stack = []

    for char in s:
        if char == '#':
            break
        if char in matching_pairs.values():  # Opening characters
            stack.append(char)
        elif char in matching_pairs.keys():  # Closing characters
            if stack == [] or matching_pairs[char] != stack.pop():
                return False

    return stack == []

print(wellformed("({{ABC}}"))
print(wellformed("({[<>fdf]fdf}fdfg)#comment"))
print(wellformed(""))
