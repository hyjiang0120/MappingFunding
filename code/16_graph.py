import pandas as pd
import plotly.express as px
import os

# Read the data from the file
file_path = '../results/fine_scale/split_mallet_models/2013-2015/50-topic-files/funding_result.csv'
data = pd.read_csv(file_path, sep='\t', header=None, names=['Category', 'Topic', 'Value'])

# Create the sunburst chart using Plotly Express
fig = px.sunburst(data, path=['Category', 'Topic'], values='Value')

# Save the plot as a PNG file in the specified directory
output_dir = '../results/fine_scale/split_mallet_models/2013-2015/50-topic-files'
output_file = os.path.join(output_dir, 'funding_sunburst_chart.png')
fig.write_image(output_file)
