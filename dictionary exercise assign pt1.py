# create dictionary
textdic = {}

# open file
infile = open("text.txt", "r")

# get the words from the file
for line in infile:

    for word in line.split():

        # strip the punctuation from the file
        word1 = word.strip(".")
        word2 = word1.strip(",")
        word3 = word2.lower()

        # if the word isnt a key, make it one
        if word3 not in textdic:
            textdic[word3] = 0

        # if the word is a key, add one to it
        if word3 in textdic:
            textdic[word3] += 1

# print the dictionary
print(textdic)
