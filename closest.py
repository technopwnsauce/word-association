import re
import numpy

def distance():
	#Get word to be checked
	input = raw_input("Enter a word to find its closest associated word (ex: duck):\n")
	word_one = input
	print "You entered: " + str(word_one)

	#Read in File
	text = open('vectors.txt')
	myString = text.read()

	#Parse word to be checked
	word_one = str(word_one)
	block_one = re.match(r'(.*\n)*'+re.escape(word_one)+'\s(.*)(\n)',myString)
	block_one = block_one.group(2)
	#print "Block one is: " + str(block_one)
	vector_one = block_one.split()
	vector_one = numpy.asarray(vector_one)
	vector_one = vector_one.astype(float)

	#Gather all words
	words = re.sub(r'[^a-zA-z\n]*',"",myString)
	words = words.split()

	print "Number of pairs to check : " + str(len(words)-1) + "..."

	#Loop through each possible pair of words
	distance = 1000
	result = "null"
	length = len(words)

	for x in range (0,length):
		if(x%1000==0):
			print str(x) + " pairs checked..."
			print "Current closest word is: " + str(result)
		word_two = words[x]
		#Skip checking word with itself (the distance will of course be zero)
		if word_one == word_two:
			continue
		#Match blocks
		word_two = str(word_two)
		block_two = re.match(r'(.*\n)*'+re.escape(word_two)+'\s(.*)(\n)',myString)
		block_two = block_two.group(2)

		#Place blocks into lists, the convert lists to vectors
		vector_two = block_two.split()
		vector_two = numpy.asarray(vector_two)
		vector_two = vector_two.astype(float)

		#Calculate distance between two vectors
		temp_distance = numpy.linalg.norm(vector_one-vector_two)
		if(temp_distance < distance):
			distance = temp_distance
			result = word_two

	print "Closest associated word to " + word_one + " is " + word_two + " with a distance of " + distance

distance()