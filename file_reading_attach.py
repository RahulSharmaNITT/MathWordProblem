import nltk
essays = "Rahul has 3 marbles. Amit gave him 2 more. How many marbles does Rahul have now?"
tokens = nltk.word_tokenize(essays)
tagged = nltk.pos_tag(tokens)
nouns = [word for word,pos in tagged \
	if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS')]
downcased = [x.lower() for x in nouns]
joined = " ".join(downcased).encode('utf-8')
into_string = str(nouns)

output = open("output.txt", "wb")
output.write(joined)
output.close()
