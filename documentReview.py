
file = open("QuickSPython.txt","r")

frequent_word = ""
frequency = 0
words = []

for line in file:

	line_word = line.lower().replace(',','').replace('.','').split(" ");
	

	for w in line_word:
		words.append(w);
		

for i in range(0, len(words)):
	

	count = 1;
	

	for j in range(i+1, len(words)):
		if(words[i] == words[j]):
			count = count + 1;

	if(count > frequency):
		frequency = count;
		frequent_word = words[i];

print("Most repeated word: " + frequent_word)
print("Frequency: " + str(frequency))


from collections import Counter


with open("QuickSPython.txt") as input_file:
    #build a counter from each word in the file
    count = Counter(word for line in input_file
                         for word in line.split())

print(count.most_common(20))

infile = "QuickSPython.txt"
outfile = "cleaned_file.txt"

delete_list = ["for", "and", "nor", "but", "or", "yet", "so"]
with open(infile) as fin, open(outfile, "w+") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(word, "")
        fout.write(line)

file.close();
