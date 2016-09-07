import re
import numpy

def distance():
	#Get Words
	input = raw_input("Enter two words which you would like to check for association (ex: ball,player):\n")
	matches = re.match(r'(.*)(,)(.*)',input)
	word_one = matches.group(1)
	word_two = matches.group(3)
	#print "You entered: " + str(word_one) + " and " + str(word_two)

	#Read in File
	text = open('vectors.txt')
	myString = text.read()

	#Match blocks
	word_one = str(word_one)
	block_one = re.match(r'(.*\n)*'+re.escape(word_one)+'\s(.*)(\n)',myString)
	block_one = block_one.group(2)
	#print "Block one is: " + str(block_one)
	word_two = str(word_two)
	block_two = re.match(r'(.*\n)*'+re.escape(word_two)+'\s(.*)(\n)',myString)
	block_two = block_two.group(2)
	#print "Block two is: " + str(block_two)

	#Place blocks into lists, the convert lists to vectors
	vector_one = block_one.split()
	vector_one = numpy.asarray(vector_one)
	vector_one = vector_one.astype(float)
	vector_two = block_two.split()
	vector_two = numpy.asarray(vector_two)
	vector_two = vector_two.astype(float)

	#print vector_one
	#print vector_two

	#Calculate distance between two vectors
	distance = numpy.linalg.norm(vector_one-vector_two)
	print distance

#Loop
while(True):
	distance()