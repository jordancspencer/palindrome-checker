def is_palindrome(word):
    return word == word[::-1]

def check_all_palindromes(word_list):
    for word in word_list:
        if not is_palindrome(word):
            return False
    return True

# Example usage
words = ['racecar', 'noon', 'civic']
print(check_all_palindromes(words))  # Output: True

words = ['racecar', 'shoe', 'moon']
print(check_all_palindromes(words))  # Output: False
