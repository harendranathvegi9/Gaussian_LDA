''' script to get top K words in each topic '''


import sys, collections
from operator import itemgetter

corpusFile = file(sys.argv[1]).read().strip().split()
topicAssignFile = file(sys.argv[2]).read().strip().split()
K = int(sys.argv[3])

assert(len(corpusFile) == len(topicAssignFile))

topicDic = collections.defaultdict(lambda:collections.defaultdict(lambda:0))

for a,b in zip(corpusFile, topicAssignFile):
    topicDic[b][a] += 1

#sort
for topic, words in topicDic.items():
    words = sorted(words, key=itemgetter(1), reverse=True)
    print ' 'join([a for a, b in words[:K]])

