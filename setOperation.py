def setOp(list1=None, list2=None):

    if list1 is None:
        list1 = []
    if list2 is None:
        list2 = []
    unionSet = list1.copy()
    for item in list2:
        if item not in unionSet:
            unionSet.append(item)

    intersectionSet= []
    for item in list1:
        if item in list2 and item not in intersectionSet:
            intersectionSet.append(item)

    differenceSet = []
    for item in list1:
        if item not in list2:
            differenceSet.append(item)

    return unionSet, intersectionSet, differenceSet

input1 = input("Enter list A: ")
input2 = input("Enter list B: ")

A = list(map(int, input1.split())) if input1 else []
B = list(map(int, input2.split())) if input2 else []

u, i, d = setOp(A, B)

print("List A:", A)
print("List B:", B)
print("Union:", u)
print("Intersection:", i)
print("Difference:", d)
