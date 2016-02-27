''' File to convert word vectors to proper format '''

import sys

vectorFile = sys.argv[1]
vocabFile = sys.argv[2]
outFile = sys.argv[3]

dim = -1

f = open(vectorFile, 'r').read().lower().strip().split('\n')
vectors = {}
for line in f:
    line = line.split()
    vectors[line[0]] = [float(q) for q in line[1:]]
    if dim == -1:
        dim = len(line) - 1

vocab = open(vocabFile).read().lower().strip().split('\n')

#write the vectors in the same order as vocab
g = open(outFile, 'w')
zeroVector = [0.0] * dim

for w in vocab:
    if w in vectors:
        vec = vectors[w]
    else:
        vec = zeroVector
    
    g.write(' '.join([str(q) for q in vec]) + '\n')

g.close()






