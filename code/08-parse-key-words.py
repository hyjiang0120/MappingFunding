import pandas as pd
import xml.etree.ElementTree as ET

diagnostics = '../results/fine_scale/split_mallet_models/2022-2024/50-topic-files/1-50-topics-diagnostics.xml'

tree = ET.parse(diagnostics)
root = tree.getroot()

len(root)
# 50

element = root[0]
element.tag
element.text
element.attrib
element.get('id')

df = []

for child in root:
    info = {"Topic": child.attrib["id"]}

    for (i, grandchild) in enumerate(child):
        info[str(i) + "_word"] = grandchild.text

    df.append(info)

df = pd.DataFrame(df)

df.to_csv("../results/fine_scale/split_mallet_models/2022-2024/50-topic-files/1-50-keywords.csv", index=False)
