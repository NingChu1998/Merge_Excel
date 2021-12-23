# pip install pandas ==1.1.5
# pip install openpyxl

import pandas as pd
import os

# Step 1 Copy your files to current testing folder
# Step 2 Get your current path 
dir_path = os.path.dirname(os.path.realpath(__file__))
# Step 3 Prepare to build a 2-dimensional table of rows and columns
combined = pd.DataFrame()
# Step 4 Read files + add data
for filename in os.listdir(dir_path):
	if filename.lower().endswith((".xlsx")):
			# Step 5 Pick yout starting row (ex: start from row = 4)
			df = pd.read_excel(filename, engine="openpyxl", skiprows=3)
			combined = combined.append(df,ignore_index=True)
# Step 6 save as excel file
combined.to_excel("combined.xlsx")