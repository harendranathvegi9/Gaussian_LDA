''' script to get top K words in each topic '''


import sys, collections
from operator import itemgetter

corpusFile = file(sys.argv[1]).read().strip().split()
topicAssignFile = file(sys.argv[2]).read().strip().split()
K = int(sys.argv[3])
vocab = file(sys.argv[4]).read().strip().split('\n')

assert(len(corpusFile) == len(topicAssignFile))

topicDic = collections.defaultdict(lambda:collections.defaultdict(lambda:0))

for a,b in zip(corpusFile, topicAssignFile):
    topicDic[b][a] += 1

#sort
for topic, words in topicDic.items():
    words = sorted(words.items(), key=itemgetter(1), reverse=True)
    print ' '.join([vocab[int(a)] for a, b in words[:K]])

#python topic-word-dist.py data/nips/corpus.train output_old/D50/I1/K20/GLDA/Feb_27_2016_11.41.15/table_assignments.txt 10
