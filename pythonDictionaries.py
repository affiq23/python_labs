#1. A hash table is a data structure that stores data in an array format, where each data value has an index.
#2. A mapping type in Python is a data structure that has a key and a value. The map()function returns a map object in the form map(fun, iter).

thisdict1 = {
  "number one": 10,
  "number two": 23,
  "number three": 2003
}
print(thisdict1)

thisdict2 = {
  "number one": [10,23,2003],
  "number two": ["array", "with", "strings"],
  "number three": [23.45, 2157.4, 2395.5]
}
print(thisdict2)

my_dict ={
    'key1':123,
    'key2':[12,23,33],
    'key3':['item0','item1','item2']
    }

print((my_dict['key3'][0]).upper())
my_dict['key1'] = 0



#break

stuff = {
    "animal": "dog",
    'numbers': 34
    }
print(stuff);

nest = { 'dict1': {'animals': 'cat'}, 
         'dict2': {'name': 'Bob', 'age': '25'}} 
print(nest['dict1']['animals'])

print(nest.keys())
print(nest.values())
print(nest.items())








