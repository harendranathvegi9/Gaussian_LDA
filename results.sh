dirName=$1
tag=$2

#create the two files for nips and 20news
head -n 11266 $dirName/table_assignments.txt >$dirName/table_assignments.txt.20news && 
tail -n 1566 $dirName/table_assignments.txt >$dirName/table_assignments.txt.nips && 

#prep the files
python topic-word-dist.py data/nips/corpus.train $dirName/table_assignments.txt.nips 20 data/nips/vocab.txt >./topic_interpretability/data/nips_topics.txt && 
python topic-word-dist.py data/20_news/corpus.train $dirName/table_assignments.txt.20news 20 data/20_news/vocab.txt>./topic_interpretability/data/20news_topics.txt &&

#calculate the OC
cd topic_interpretability;
./run-oc.sh ./data/nips_topics.txt;
cat ./results/topics-oc.txt;
mv ./results/topics-oc.txt ./results/topics-oc.nips.$tag.txt;
./run-oc.sh ./data/20news_topics.txt;
cat ./results/topics-oc.txt;
mv ./results/topics-oc.txt ./results/topics-oc.20news.$tag.txt;
cd ..;
