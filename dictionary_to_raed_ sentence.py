#

def count_letters(text):
    result = {}  # initilize the dictionary
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

# testing
print(count_letters("tenant"))
