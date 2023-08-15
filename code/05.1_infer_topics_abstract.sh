#!/bin/bash

# infer topics on whole dataset
for r in 1
do
    for k in 50
    do
        echo $k
        mallet infer-topics --inferencer ../results/fine_scale/mallet_models/$k-topic-files/$r-$k-topics-inferencer --input ../data/clean_data/UK/fine_scale/splitdata/mallet/1973_1977_mallet-tokens.mallet --output-doc-topics ../data/clean_data/UK/fine_scale/splitdata/mallet_models/1973_1977_$r-$k-topics-doc.txt
        mallet infer-topics --inferencer ../results/fine_scale/mallet_models/$k-topic-files/$r-$k-topics-inferencer --input ../data/clean_data/UK/fine_scale/splitdata/mallet/1978_1983_mallet-tokens.mallet --output-doc-topics ../data/clean_data/UK/fine_scale/splitdata/mallet_models/1978_1983_$r-$k-topics-doc.txt
        mallet infer-topics --inferencer ../results/fine_scale/mallet_models/$k-topic-files/$r-$k-topics-inferencer --input ../data/clean_data/UK/fine_scale/splitdata/mallet/1984_1988_mallet-tokens.mallet --output-doc-topics ../data/clean_data/UK/fine_scale/splitdata/mallet_models/1984_1988_$r-$k-topics-doc.txt

        mallet infer-topics --inferencer ../results/fine_scale/mallet_models/$k-topic-files/$r-$k-topics-inferencer --input ../data/clean_data/UK/fine_scale/splitdata/mallet/1989_1993_mallet-tokens.mallet --output-doc-topics ../data/clean_data/UK/fine_scale/splitdata/mallet_models/1989_1993_$r-$k-topics-doc.txt

        mallet infer-topics --inferencer ../results/fine_scale/mallet_models/$k-topic-files/$r-$k-topics-inferencer --input ../data/clean_data/UK/fine_scale/splitdata/mallet/1994_1998_mallet-tokens.mallet --output-doc-topics ../data/clean_data/UK/fine_scale/splitdata/mallet_models/1994_1998_$r-$k-topics-doc.txt

        mallet infer-topics --inferencer ../results/fine_scale/mallet_models/$k-topic-files/$r-$k-topics-inferencer --input ../data/clean_data/UK/fine_scale/splitdata/mallet/1999_2003_mallet-tokens.mallet --output-doc-topics ../data/clean_data/UK/fine_scale/splitdata/mallet_models/1999_2003_$r-$k-topics-doc.txt

        mallet infer-topics --inferencer ../results/fine_scale/mallet_models/$k-topic-files/$r-$k-topics-inferencer --input ../data/clean_data/UK/fine_scale/splitdata/mallet/2004_2008_mallet-tokens.mallet --output-doc-topics ../data/clean_data/UK/fine_scale/splitdata/mallet_models/2004_2008_$r-$k-topics-doc.txt
        mallet infer-topics --inferencer ../results/fine_scale/mallet_models/$k-topic-files/$r-$k-topics-inferencer --input ../data/clean_data/UK/fine_scale/splitdata/mallet/2009_2013_mallet-tokens.mallet --output-doc-topics ../data/clean_data/UK/fine_scale/splitdata/mallet_models/2009_2013_$r-$k-topics-doc.txt
        mallet infer-topics --inferencer ../results/fine_scale/mallet_models/$k-topic-files/$r-$k-topics-inferencer --input ../data/clean_data/UK/fine_scale/splitdata/mallet/2014_2018_mallet-tokens.mallet --output-doc-topics ../data/clean_data/UK/fine_scale/splitdata/mallet_models/2014_2018_$r-$k-topics-doc.txt
        mallet infer-topics --inferencer ../results/fine_scale/mallet_models/$k-topic-files/$r-$k-topics-inferencer --input ../data/clean_data/UK/fine_scale/splitdata/mallet/2019_2023_mallet-tokens.mallet --output-doc-topics ../data/clean_data/UK/fine_scale/splitdata/mallet_models/2019_2023_$r-$k-topics-doc.txt


    done
done
