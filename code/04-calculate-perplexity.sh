# !/bin/bash

# training topic model with Mallet 

# carry out 3 repetitions with seeds set to 'r' below (i.e 1, 2, 3)
 for r in {1..3}
  do
    echo split data into training and validation sets
    # check out what the Mallet 'slipt' argument do (and all its features) by typing 'mallet split --help' on the terminal
    mallet split --input ../data/clean_data/UK/splitdata/mallet/2022_2024_mallet-tokens.mallet --random-seed $r --training-portion 0.7 --training-file ../data/clean_data/UK/fine_scale/$r-training.mallet --testing-file ../data/clean_data/UK/fine_scale/$r-testing.mallet
    
    # 
    mallet run cc.mallet.util.DocumentLengths --input ../data/clean_data/UK/fine_scale/$r-testing.mallet > ../results/fine_scale/split_mallet_models/$r-doc-lengths.txt

    # k is the number of topics; in this case from 50 to 400 topics in 25 increments 
    for i in {50..401..25}
      do

        echo number of topics: $i
        echo round: $r
        
        # create folder (if it does not exist) to store all files that will be created
        mkdir -p ../results/fine_scale/split_mallet_models/$i-topic-files

        echo training model

        # if file does not exist proceed to train model
        if [ ! -f ../results/fine_scale/split_mallet_models/$i-topic-files/$r-$i-topics-state.gz ]; then
          # train model 
          # check out what the Mallet 'train-topics' argument do (and all its features) by typing 'mallet train-topics --help' on the terminal
          mallet train-topics --input ../data/clean_data/UK/fine_scale/$r-training.mallet --random-seed $r --num-topics $i --num-threads 40 --optimize-interval 100 --optimize-burn-in 20# !/bin/bash

# training topic model with Mallet 

# carry out 3 repetitions with seeds set to 'r' below (i.e 1, 2, 3)
 for r in {1..2}
  do
    echo split data into training and validation sets
    # check out what the Mallet 'slipt' argument do (and all its features) by typing 'mallet split --help' on the terminal
    mallet split --input ../data/clean_data/UK/fine_scale/splitdata/mallet/2022_2024_mallet-tokens.mallet --random-seed $r --training-portion 0.7 --training-file ../data/clean_data/UK/fine_scale/splitdata/$r-training.mallet --testing-file ../data/clean_data/UK/fine_scale/splitdata/$r-testing.mallet
    
    # 
    mallet run cc.mallet.util.DocumentLengths --input ../data/clean_data/UK/fine_scale/splitdata/$r-testing.mallet > results/fine_scale/filter_mallet_models/$r-doc-lengths.txt

    # k is the number of topics; in this case from 50 to 400 topics in 25 increments 
    for i in $(seq 50 25 401)
      do

        echo number of topics: $i
        echo round: $r
        
        # create folder (if it does not exist) to store all files that will be created
        mkdir -p ../results/fine_scale/filter_mallet_models/$i-topic-files

        echo training model

        # if file does not exist proceed to train model
        if [ ! -f ../results/fine_scale/filter_mallet_models/$i-topic-files/$r-$i-topics-state.gz ]; then
          # train model 
          # check out what the Mallet 'train-topics' argument do (and all its features) by typing 'mallet train-topics --help' on the terminal
          mallet train-topics --input ../data/clean_data/UK/fine_scale/splitdata/$r-training.mallet --random-seed $r --num-topics $i --num-threads 40 --optimize-interval 100 --optimize-burn-in 200 --output-state ../results/fine_scale/filter_mallet_models/$i-topic-files/$r-$i-topics-state.gz --diagnostics-file ../results/fine_scale/filter_mallet_models/$i-topic-files/$r-$i-topics-diagnostics.xml --evaluator-filename ../results/fine_scale/filter_mallet_models/$i-topic-files/$r-$i-topics-evaluator --inferencer-filename ../results/fine_scale/filter_mallet_models/$i-topic-files/$r-$i-topics-inferencer

          # evaluate model (gets perplexity value)
          echo evaluating model
          mallet evaluate-topics --input ../data/clean_data/UK/fine_scale/splitdata/$r-testing.mallet --evaluator ../results/fine_scale/filter_mallet_models/$i-topic-files/$r-$i-topics-evaluator --output-prob ../results/fine_scale/filter_mallet_models/$i-topic-files/$r-$i-topics-log-probability
        fi
      done
done
