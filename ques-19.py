import string

str = "hello ! kitty , how  are  you ?"

noPunctuation = " "
for i in str:
  if i not in string.punctuation:
    noPunctuation = noPunctuation + i 
print(noPunctuation)