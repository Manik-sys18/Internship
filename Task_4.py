import pandas as pd    #Imported pandas library to read the CSV file
from tabulate import tabulate # 

df = pd.read_csv("student_scores.csv") #Read the CSV file named "student_scores.csv" and store it in a DataFrame called df.

print(tabulate(df.head(), headers='keys', tablefmt='psql')) # The first five rows of the DataFrame are printed in a tabular format using the tabulate library.
print(tabulate(df.tail(), headers='keys', tablefmt='psql')) # The last five rows of the DataFrame are printed in a tabular format using the tabulate library.
print(df.shape) # The shape of the DataFrame is printed.
print(df.columns) # The column names of the DataFrame are printed.
print(df.describe()) # A summary statistics of the DataFrame is printed.
print(df.info()) # Information about the DataFrame, including the number of non-null entries and data types, is printed.
print(tabulate(df, headers = 'keys', tablefmt = 'psql', showindex = 'False')) # The entire DataFrame is printed in a tabular format using the tabulate library.
print("Dataset Loaded Successfully!")