# Anagram Checker: Write a function is_anagram(s1, s2) that takes two strings and 
# returns True if they are anagrams of each other (contain the same characters with the same frequency), and False otherwise.

# Example: "listen" and "silent" are anagrams.

def is_anagram(s1, s2):
   d1 = {}
   d2 = {}

   for word in s1:
      if word in d1:
         d1[word] += 1
      else:
        d1[word] = 1

   for word in s2:
      if word in d2:
         d2[word] += 1
      else:
         d2[word] = 1

   if d1 == d2:
      return True
   else:
      return False

s1="listen"
s2="silent"

print(is_anagram(s1, s2))