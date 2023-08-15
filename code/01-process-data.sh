# !/bin/bash


# process text
echo "tokenising text"
# first argument is the language to use; second arg is the path to the python script; third arg is the path to where get the data from; 
# fourth arg is where to save the processed data

#python 0.1_tokenize_texts4mallet.py 0.1.1_abstracts_path.txt ../data/clean_data/UK/fine_scale/

python 0.1_tokenize_texts4mallet.py 0.1.3_abstractsinyear_path.txt ../data/clean_data/UK/splitdata/tokenized/