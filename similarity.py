# coding:utf-8
# measuring similarity

import numpy as np
import os
import scipy.misc
from glob import glob
import re
import time
import Image
import cv2

def numericalSort(value):
	numbers = re.compile(r'(\d+)')
	parts = numbers.split(value)
	parts[1::2] = map(int, parts[1::2])
	return parts

def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

pokemon = sorted(glob(os.path.join("./pokemon", "*.png")), key=numericalSort)

with open("similarity.txt", "w") as f:
	for i, poke in enumerate(pokemon):
		# if i > 2:
		# 	break
		img1 = cv2.imread(poke)
		img1 = np.array(img1)
		img1 = img1.flatten().astype(np.float32)
		name1, _ = os.path.splitext(os.path.basename(poke))
		cos = []
		cos.append([name1, 1])
		for j, poke2 in enumerate(pokemon):
			if i == j:
				continue
			else:
				img2 = cv2.imread(poke2)
				img2 = np.array(img2)
				img2 = img2.flatten().astype(np.float32)
				name2, _ = os.path.splitext(os.path.basename(poke2))
				cos.append([name2, cos_sim(img1, img2)])
				# print name2, cos_sim(img1, img2)
		cos = sorted(cos, key=lambda x:x[1], reverse=True)

		for index in cos:
			f.write("{0}".format(index[0]).rstrip('\r\n') + ' ')

		f.write('\n')

		print "*****finish {0}poke".format(i)


