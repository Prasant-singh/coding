# count_word_frequency("Hello world! Hello Python.") should return {'hello': 2, 'world': 1, 'python': 1}.

def count_word_frequency(text):
    words=text.lower().split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    print(word_count)



count_word_frequency("Hello world! Hello Python.")