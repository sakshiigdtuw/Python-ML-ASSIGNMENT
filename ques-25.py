Samplefile = open("C:/Users/chaud/OneDrive/Desktop/Internship and training/ASSIGNMENT-01/textFile.txt","r")
copyFile = open("C:/Users/chaud/OneDrive/Desktop/Internship and training/ASSIGNMENT-01/q25.txt","w")
for i in Samplefile:
  copyFile.write(i)

print("Content copy of  textFile.txt in q25.txt file")
