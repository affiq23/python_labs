grammer_dict = {}

print ("Welcome to Madlib Generator: \n")

line1 = ("There are many (adjective) ways to choose a/an (noun) to read \n")
print(line1)

adjective = input("\t Enter an adjective: ")
noun = input("\t Enter a noun: ")

grammer_dict['adjective'] = adjective
grammer_dict['noun'] = noun

line2 = ("First, you could ask for recommendation from your friends and (Plural noun) \n")
print(line2)

plural_noun = input("\t Enter a plural noun: ")
grammer_dict['plural noun'] = plural_noun

line3 = ("Just don't ask Aunt (Person in Room (Female) \n ")
print(line3)

person = input("\t Enter a female: ")
grammer_dict['female'] = person

print("Now i will write your madlib to a file...\n Processing...")

with open('example_file.txt', 'w') as my_file:
    line1 = line1.replace("(adjective)", grammer_dict['adjective']).replace("(noun)", grammer_dict['noun'])
    my_file.write(line1)

    line2 = line2.replace("(Plural noun)", grammer_dict['plural noun'])
    my_file.write(line2)

    line3 = line3.replace("(Person in Room (Female) \n ", grammer_dict['female'])
    my_file.write(line3)

    my_file.close()

print("Done! \nNow you can go to your desktop and check out the file titled 'example_file'")