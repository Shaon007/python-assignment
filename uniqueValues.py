def duplicateRemove(num):
  unique = []
  for i in num:
    if i not in unique:
      unique.append(i)
  return unique
inputList = input("Enter list of number:")
originalList = list(map(int, inputList.split()))
uniqueList = duplicateRemove(originalList)
uniqueCount = len(uniqueList)

print("Original list:", originalList)
print("Unique list:", uniqueList)
print("Number of unique values:", uniqueCount)
