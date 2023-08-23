# Revealing Temporal Trends in UK STEM Funding using AI

This repository contains code and resources for the project "Revealing Temporal Trends in UK STEM Funding using AI". The project aims to uncover and analyze temporal trends in STEM (Science, Technology, Engineering, and Mathematics) funding in the UK. The analysis involves data preprocessing, topic analysis using the Mallet Latent Dirichlet Allocation (LDA) tool, and further analysis of LDA-generated results using Python.

## step 1 01-process-data.sh
To preprocess the raw text data and convert it into a format suitable for the MALLET topic modeling tool for subsequent topic analysis, which including removing stop words, lemmatization, etc., and finally saving the processed data as a file for topic modeling analysis.

## 02_filter-tokens.py
Read specific required columns from metadata, including "ProjectId", "Abstract"

## 03-import-data-mallet.sh
importing data with Mallet

## 04_calculate_perplexity.sh
Training and evaluating the Mallet topic model through multiple iterations with different number of topics and random seeds, and save the model state, diagnostic information and evaluation results

### 05-infer-topics.sh
Use the previously trained topic inferencer (inferencer) to perform topic inference on the entire data set (topic inference)

### 06-concat-proj-metadata.py
Organize and process project metadata, including cleansing funding amounts, merging data, calculating project funding totals, filtering top funding projects, and saving processed data

## 08-parse-key-words.py
Extracts topic keyword information from an XML file and organizes it into a readable tabular form.

### 11_splitsbatract.py
According to the start date of the project, the corresponding summary information is organized by year and saved in different files

### 12_split_metadata.py
Segment metadata into CSV files of different years based on project start date for more efficient data processing and analysis

## 13_topic_amount.py
Extract the funding amount from the project metadata, merge it with the topic data, calculate the total funding amount for each topic

### 14_count_project_number.py
Extract the most significant theme of each item in each theme from the data file, and count the number of items under each theme

### 15_merge_result.py
data merge

### 16_graph.py
Create a Sunburst Chart base on the data

### 17_column_graph.py
Use Seaborn to draw a heat map

### 18_count_funding.py
Extract the corresponding project information and fund data from the metadata file, and add the fund amount to the corresponding column in the DataFrame according to the index of the maximum value

### 19_count_funding_result.py
Read the result file of previously generated funding amounts, calculate the sum of each project funding

### Project Report
The latex code for dissertation.