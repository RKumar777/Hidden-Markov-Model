# Hidden-Markov-Model
Learning Hidden Markov Model using forward backward algorithm for text analysis
The 2 files here perform different functions:
1. forwardbackward.py tries to implement the forward backward algorithm for efficient computation of the different parameters in the HMM model
2. learnhmm.py tries to learn the different paramters of the HMM model

The input file is a text file having one sentence per line which has been tokenized already in the following format:
<Word0> <Tag0> <Word1> <Tag1> ... <WordN> <TagN>
  
The learning, evaluation and decoding problems have been solved in the programs
The inputs/outputs for learnhmm.py are:
1. train input file
2. index to word.txt file which gives indices to different words and is a text input file
3. index to tag.txt file which gives indices to different tags and is a text input file
4. hmmprior outputs the prior parameters
5. hmmemit outputs the emmission probabilities
6. hmmtrans outputs the transmission probabilities

The inputs/outputs for forwardbackward.py are:
1. train input file
2. index to word.txt file which gives indices to different words and is a text input file
3. index to tag.txt file which gives indices to different tags and is a text input file
4. hmmprior outputs the prior parameters
5. hmmemit outputs the emmission probabilities
6. hmmtrans outputs the transmission probabilities
