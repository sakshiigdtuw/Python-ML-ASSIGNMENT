user_String = input("enter the string: ")
start = input("Enter the desired prefix in string: ")
end = input("Enter the desired suffix in string: ")


if user_String[0]==start or user_String[-1]==end:
   print("string have either the favourable prefix or suffix.")

else:
    print("string do not have required prefix or suffix")