import operator

def find_most_frequent_word(words: list[str]) -> (str, int):
    frequency = {}
    max_value = 0
    for index, word in enumerate(words):
        frequency[word] = frequency.get(word, 0) + 1
        word_frequency = frequency.get(word)
        if word_frequency > max_value:
            max_value = word_frequency
    result = []
    for key, value in frequency.items():
        if value == max_value:
            result.append((key, value))
    result = sorted(result, key=operator.itemgetter(0))
    return result[0]