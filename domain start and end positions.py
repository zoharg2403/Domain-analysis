import pandas as pd

# load full data file
data = pd.read_csv("uniprot-proteome_150622_for analysis.txt", sep='\t')

# get col names
cols = list(data.columns)[2:]

for c in cols:
    print(c)
    cur_df = data[['Gene names  (ordered locus )', 'Entry', c]].copy()
    cur_df.dropna(inplace=True)
    # add start and end position to cur_df from columns index 3
    range = cur_df[c].str.split(';', expand=True, n=1)[0]
    if range.str.count('(\d+)').mean() == 1:
        range = range.str.extractall('(\d+)')
        range.set_index(cur_df.index, inplace=True)
        cur_df = pd.concat([cur_df, range], axis=1)
    else:
        range = range.str.extractall('(\d+)').unstack()
        cur_df = pd.concat([cur_df, range], axis=1)
    # cur_df.drop(columns=c, inplace=True)
    # save to .csv
    cur_df.to_csv("C:/Users/zoharga/Desktop/Zohar/041021 Ofir analysis - domain analysis/200622/" + f"{c} - start and end positions.csv", index=0)
