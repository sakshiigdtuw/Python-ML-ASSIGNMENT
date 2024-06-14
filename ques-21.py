lst = [1,7,8,3,4,2,8]
elm = int(input("Enter the element: "))
def countRepeat(lst,elm):
  count =0
  for i in lst:
    if i == elm:
      count += 1
  return count

result = countRepeat(lst,elm)
print(result)
