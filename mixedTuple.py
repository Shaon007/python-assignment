tuple1 = (10, "Python", 3.5, True)
num, text, decimal, flag = tuple1

print("Number:", num)
print("Text:", text)
print("Decimal:", decimal)
print("Boolean:", flag)

tuple2 = (20, "Python", 4.5, False)

print("Comparisons:")
print("tuple1 == tuple2 :", tuple1 == tuple2)
print("tuple1 != tuple2 :", tuple1 != tuple2)
print("tuple1 > tuple2  :", tuple1 > tuple2)
print("tuple1 < tuple2  :", tuple1 < tuple2)

# Difference between List and Tuple
# LIST:
# Mutable (can be changed after creation)
# Uses square brackets []
# Slower but flexible
#Ex:
my_list = [1, 2, 3]
my_list.append(4) #allowed

# TUPLE:
# Immutable (cannot be changed after creation)
# Uses parentheses ()
# Faster and memory efficient
# Ex:
my_tuple = (1, 2, 3) #not allowed
