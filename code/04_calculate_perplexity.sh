#!/bin/bash

# Training topic model with Mallet

# Perform 3 repetitions with seeds set to 'r' (i.e. 1, 2, 3)
for r in {1..3}; do
  echo "Split data into training and testing sets"

  # Split the data into training and testing sets
  #mallet split --input ../data/clean_data/UK/splitdata/mallet/2019_2021_mallet-tokens.mallet --random-seed $r --training-portion 0.7 --training-file ../data/clean_data/UK/splitdata/mallet/$r-training.mallet --testing-file ../data/clean_data/UK/splitdata/mallet/$r-testing.mallet
  mallet split --input ../data/clean_data/UK/splitdata/mallet/2022_2024_mallet-tokens.mallet --random-seed $r --training-portion 0.7 --training-file ../data/clean_data/UK/splitdata/mallet/$r-training.mallet --testing-file ../data/clean_data/UK/splitdata/mallet/$r-testing.mallet

  echo "Calculating document lengths"
  mallet run cc.mallet.util.DocumentLengths --input ../data/clean_data/UK/splitdata/mallet/$r-testing.mallet >../results/fine_scale/split_mallet_models/$r-doc-lengths.txt

  # Iterate over the number of topics (50 to 400 in increments of 25)
  for k in $(seq 50 25 401); do
    echo "Number of topics: $k"
    echo "Round: $r"

    # Create a folder (if it does not exist) to store all the files
    mkdir -p ../results/fine_scale/split_mallet_models/$k-topic-files

    # Train the topic model if the state file does not exist
    if [ ! -f ../results/fine_scale/split_mallet_models/$k-topic-files/$r-$k-topics-state.gz ]; then
      echo "Training model"

      # Train the model
      mallet train-topics --input ../data/clean_data/UK/splitdata/mallet/$r-training.mallet --random-seed $r --num-topics $k --num-threads 40 --optimize-interval 100 --optimize-burn-in 200 --output-state ../results/fine_scale/split_mallet_models/$k-topic-files/$r-$k-topics-state.gz --diagnostics-file ../results/fine_scale/split_mallet_models/$k-topic-files/$r-$k-topics-diagnostics.xml --evaluator-filename ../results/fine_scale/split_mallet_models/$k-topic-files/$r-$k-topics-evaluator --inferencer-filename ../results/fine_scale/split_mallet_models/$k-topic-files/$r-$k-topics-inferencer

      echo "Evaluating model"
      # Evaluate the model to get the perplexity value
      mallet evaluate-topics --input ../data/clean_data/UK/splitdata/mallet/$r-testing.mallet --evaluator ../results/fine_scale/split_mallet_models/$k-topic-files/$r-$k-topics-evaluator --output-prob ../results/fine_scale/split_mallet_models/$k-topic-files/$r-$k-topics-log-probability
    fi
  done
done
