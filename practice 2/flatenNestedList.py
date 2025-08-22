# Flatten a Nested List: Write a function flatten_list(nested_list) that takes a list of lists and returns a single, flat list.

# Example: [[1, 2], [3, 4], [5]] should become [1, 2, 3, 4, 5].

def flatten_list(nested_list):
   l=[]
   for element in nested_list:
      for item in element:
         l.append(item)
   return l



l = [[1, 2], [3, 4], [5]]
print(flatten_list(l))