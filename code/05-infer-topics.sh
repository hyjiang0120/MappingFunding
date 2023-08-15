#!/bin/bash

# infer topics on whole dataset
for r in 1

do
    for k in 50

    do
        echo $k
        mallet infer-topics --inferencer ../results/fine_scale/split_mallet_models/$k-topic-files/$r-$k-topics-inferencer --input ../data/clean_data/UK/splitdata/mallet/2022_2024_mallet-tokens.mallet --output-doc-topics ../results/fine_scale/split_mallet_models/$k-topic-files/$r-$k-topics-doc.txt
    done
done





