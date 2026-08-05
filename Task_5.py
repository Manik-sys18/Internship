import pandas as pd

df = pd.read_csv("student_scores.csv") #Read the CSV file named "student_scores.csv" and store it in a DataFrame called df.
# Since the spaces are not considered as NaN values, we will replace it with NaN using the replace method of the dataframe.
print(df.replace(r'^\s*$', float('nan'), regex=True, inplace=True))
print(df.isnull().sum()) # The number of missing values in each column of the DataFrame is printed.
print(df.fillna(0)) # The missing values in the DataFrame are filled with 0.
print(df.duplicated().sum()) # The number of duplicate rows in the DataFrame is printed.
print(df.drop_duplicates(inplace=True)) # The duplicate rows in the DataFrame are dropped.
print(df.describe()) # A summary statistics of the DataFrame is printed.
print("Clean Dataset Prepared!")