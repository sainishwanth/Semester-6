def reverse_string(string):
    char_list = list(string)
    left = 0
    right = len(char_list) - 1
    while left < right:
        if not char_list[left].isalnum():
            left += 1
        elif not char_list[right].isalnum():
            right -= 1
        else:
            char_list[left], char_list[right] = char_list[right], char_list[left]
            left += 1
            right -= 1
    return ''.join(char_list)
