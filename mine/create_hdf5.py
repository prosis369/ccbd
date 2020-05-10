# CHECK GOOGLE COLAB

import allennlp
from allennlp.commands.elmo import ElmoEmbedder
import numpy as np
import h5py

elmo = ElmoEmbedder()
file1 = open("/Users/rohitpentapati/PycharmProjects/ccbd/conllu_hindi.txt","r", encoding="utf8")
contents = file1.readlines()
#print(len(contents))

#i=1
words=[]
for sentence in contents:
    words=sentence.split(" ")
    #print(words)
    print(i)
    vectors = elmo.embed_sentence(words)
    print(vectors)
    #i+=1

matrix1 = np.random.random(size=(100,100))
with h5py.File("/Users/rohitpentapati/PycharmProjects/ccbd/hindi_dev.hdf5", "w") as hdf:
    hdf.create_dataset("dataset", data=matrix1)