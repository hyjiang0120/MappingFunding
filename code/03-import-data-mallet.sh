# !/bin/bash

echo filtering data
# call helper script to filter minimum number of tokens
# first argument below is the language of the script being called; second argument is the path to where the script is located; thrid argument is where to get the
# input data from; fourth argument is where to save the filtered data to. 
python 02_filter-tokens.py ../data/clean_data/UK/splitdata/tokenized/2016_2018_titles-abstracts-tokenized.csv ../data/clean_data/UK/splitdata/filter/

# importing data with Mallet
# this command uses the filtered data as input
# first argument below is Mallet; second arg is the Mallet function to use; the third to the sixth arguments are options from the mallet argument itself. You can look at all the 
# options and what they mean by typing "mallet bulk-load --help" on the terminal.
echo importing data
#mallet bulk-load --input ../data/clean_data/UK/fine_scale/titles-abstracts-tokenized-filtered.csv --keep-sequence TRUE --prune-count 20 --prune-doc-frequency 0.8 --output ../data/clean_data/UK/fine_scale/mallet-tokens.mallet --line-regex "^(\S*)[\s,]*(\S*)[\s,]*(.*)$"

mallet bulk-load --input ../data/clean_data/UK/splitdata/filter/2022_2024_titles-abstracts-tokenized.csv --keep-sequence TRUE --prune-count 20 --prune-doc-frequency 0.8 --output ../data/clean_data/UK/splitdata/mallet/2022_2024_mallet-tokens.mallet --line-regex "^(\S*)[\s,]*(\S*)[\s,]*(.*)$"

#mallet bulk-load --input ../data/clean_data/UK/fine_scale/splitdata/filter/2019_2023_abstracts_tokenized_filter.csv --keep-sequence TRUE --prune-count 20 --prune-doc-frequency 0.8 --output ../data/clean_data/UK/fine_scale/splitdata/mallet/2019_2023_mallet-tokens.mallet --line-regex "^(\S*)[\s,]*(\S*)[\s,]*(.*)$"
