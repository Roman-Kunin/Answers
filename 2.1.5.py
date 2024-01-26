def is_palindrome(word: str) -> bool:
    x = set(r'!\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~')
    word = [i for i in word.lower().replace(' ', '') if i not in x]
    return word == word[::-1]
