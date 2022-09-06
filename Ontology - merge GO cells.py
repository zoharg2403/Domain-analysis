import pandas as pd

# load full data file (.xslx)
data = pd.read_excel('Ontology.xlsx', header=None)

# get unique values
unique_colA = data[0].unique()
unique_colB = data[1].unique()

# according to col A (index = 0)
new_dataframe = pd.DataFrame()
for a in unique_colA:
    sorted_dataframe = data[data[0] == a]
    sorted_dataframe = sorted_dataframe.reset_index(drop=True)
    new_value = sorted_dataframe[2][0]
    for s in sorted_dataframe[2][1:]:
        new_value = new_value + ', ' + str(s)
    new_dataframe = new_dataframe.append({0: a, 1: new_value}, ignore_index=True)

new_dataframe.to_csv('output file - according to col A.csv', index=False, header=False)


