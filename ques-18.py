
str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")
if sorted(str1) == sorted(str2):
  print(f"{str1} and {str2} are anagram")
else:
  print(f"{str1} and {str2} are not anagram")



