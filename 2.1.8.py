def t9(string: str, n: str) -> str:
    res = []
    d = [[" ", ".,-", "абвг", "дежз", "ийкл", "мноп", "рсту", "фхцч", "шщъы", "ьэюя"][int(i)].lower() for i in n]
    for word in string.split():
        if all(char in mask for mask, char in zip(d, word.lower())):
            res.append(word)
    return ' '.join(res)
