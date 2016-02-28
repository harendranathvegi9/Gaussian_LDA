MAX_PARALLEL=2
i=0
for k in 10 20 40 60 100; do 
    ./run_gaussian_lda.sh -n 60 -c data/nips/corpus.train -i vectors/vectors_nips.50.txt -d 50 -k $k &
    ./run_gaussian_lda.sh -n 60 -c data/20_news/corpus.train -i vectors/vectors_20news.50.txt -d 50 -k $k &    
    ((i++));
    if (($i % $MAX_PARALLEL == 0)); then
       wait;
    fi;
done;
