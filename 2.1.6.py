def sort_words_by_length(string: str) -> list:
    return sorted(string.split(), key=lambda word: (len(word), word), reverse=False)
