import sys

dirName = sys.argv[1]

#create the two files for nips and 20news
head -n 11266 $dirName/table_assignments.txt >$dirName/table_assignments.txt.20news;
tail -n 1566 $dirName/table_assignments.txt >$dirName/table_assignments.txt.nips;

#prep the files
python topic-word-dist.py data/nips/corpus.train $dirName/table_assignments.txt.nips 20 data/nips/vocab.txt >./topic_interpretability/data/nips_topics.txt;
python topic-word-dist.py data/20_news/corpus.train $dirName/table_assignments.txt.20news 20 >./topic_interpretability/data/20news_topics.txt;

#calculate the OC
./topic_interpretability/run-oc.sh ./topic_interpretability/data/nips_topics.txt;
cat ./topic_interpretability/results/topics-oc.txt;
mv ./topic_interpretability/results/topics-oc.txt ./topic_interpretability/results/topics-oc.nips.txt;
./topic_interpretability/run-oc.sh ./topic_interpretability/data/20news_topics.txt;
cat ./topic_interpretability/results/topics-oc.txt;
mv ./topic_interpretability/results/topics-oc.txt ./topic_interpretability/results/topics-oc.20news.txt;
