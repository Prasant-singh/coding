# Merge Two Dictionaries: Write a function merge_dictionaries(d1, d2) that takes two dictionaries d1 and d2 and merges them into a single dictionary.
#  If a key exists in both, the value from d2 should be used.

def merge_dictionaries(d1, d2):
    merge=d1.copy()
    merge.update(d2)
    return merge

d1 = {"key1": "value1", "key2": "value2"}
d2 = {"key2": "new_value2", "key3": "value3"}
merged = merge_dictionaries(d1, d2)
print(merged)