# Unique Elements: Given a list with duplicate elements, write a function remove_duplicates(lst) that returns a new list with only the unique elements.
#  The order of the unique elements should be preserved.

def remove_duplicates(lst):
    l=[]

    for element in lst:
        if element not in l:
            l.append(element)
    return l

lst = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(lst))