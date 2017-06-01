# -*- coding: utf-8 -*-

from gensim.models import word2vec
import csv
import types
import numpy as np
import sys

def make_table():
	poke_dict = {}
	with open("pokemon.csv","rU") as csvfile:
		data = csv.reader(csvfile, delimiter=',')

		# data = csv.reader(open("pokemon.csv","rU"))
		poke_dict = {}
		for row in data:
			poke_dict[row[0]] = row[1]
	# print str(poke_dict).decode('string-escape')
	return poke_dict

def main():
	poke_dict = make_table()

	argv = sys.argv
	argc = len(argv)
	if (argc != 2):
		print 'Error!!---Usage: python %s data.txt' %argv[0]
		quit()
	x = argv[1]

	data = word2vec.Text8Corpus(x)
	model = word2vec.Word2Vec(data, size=1024, min_count=1)

	out=model.most_similar(positive=[u"246"])
	print "similary pokemon with 246(ヨーギラス)"
	for x in out:
		print x[0],poke_dict[x[0]],x[1]

	# out = model.wv.most_similar_cosmul(positive=['152', '004'], negative=['001'])
	# print "analogy 152 + 004 - 001 = ?"
	# for x in out:
	# 	print x[0],x[1]

	vec = []
	for poke in poke_dict.keys():
		vec.append([poke, model.wv[poke].astype(object)])

	# print vec[0]
	vec = sorted(vec, key=lambda x:x[0], reverse=False)
	# print vec[0]
	only_vec = []
	for index in vec:
		only_vec.append(index[1])

	np.save("poke_vec.npy", only_vec)

if __name__ == '__main__':
	main()