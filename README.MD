Find the assocation of words by running the GloVe tool (http://nlp.stanford.edu/projects/glove/) to train a dictionary of vectors, then run my scripts to calculate the euclidean distance.

Use the followings steps:

1. wget  http://nlp.stanford.edu/software/GloVe-1.2.zip
2. unzip GloVe-1.2.zip
3. cd GloVe-1.2
4. make
5. ./demo.sh
6. wget https://raw.githubusercontent.com/technopwnsauce/word-association/master/closest.py && wget https://raw.githubusercontent.com/technopwnsauce/word-association/master/distance.py
7. python closest.py
8. python distance.py

