# List Comprehension: Given a list of words, use a list comprehension to create a new list containing the length of each word.
words = ["hello", "world", "python", "list", "comprehension"]

lenght=[len(word) for word in words]
print(lenght)