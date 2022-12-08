#tuples
print('TUPLES' +'\n')

thisTup = (1, 3, 5, 7, 9)

newTup = (23, 'apple', 45.42, True, "hi")

print('index() returns the index of a given element in the tuple, and count() returns how times a specified element is used' + '\n')


print('first tuple:', thisTup)
print('multiple items tuple:', newTup)
# noinspection PyInterpreter
print('2nd index first tuple:', thisTup[2])
print('2nd index second tuple:x', newTup[2])
print()



#sets
print('SETS' + '\n')

thisSet = {10, 23, 12, 28, 2003}

print('a dictionary stores data values like a map, with a key:value pair, and a set is a collection of data types that cannot be changed and cannot store duplicate elements' + '\n')

uniqueEle = set([10, 34, 34, 23, 10, 54, 65, 65, 12, 12])

#none is used as a null value

print('first set', thisSet)
print('second set', uniqueEle)
print()

#files
print('FILES' + '\n')
print('file is in stored in documents')

f = open("text.txt", "r")
print(f.read())


