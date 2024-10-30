import pandas as pd

file_path = './data/raceresults.csv'
race_data = pd.read_csv(file_path)

# Display the first 10 rows in the notebook
race_data.head(10)