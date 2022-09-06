import pandas as pd
import os

# create new dataframe for output:
# for each Gene+Entry:
# show information (sequence kind, start position and end position) of the first seq that's characterized
new_df = pd.read_csv("uniprot-proteome_150622_for analysis.txt", sep='\t', usecols=["Gene names  (ordered locus )", "Entry"])
new_df["Sequence kind"] = 'NaN'
new_df["Position"] = 'NaN'

file_list = os.listdir("C:/Users/zoharga/Desktop/Zohar/041021 Ofir analysis - domain analysis/200622/")
for f in file_list:
    sq_kind = f.split(" - ")[0]
    # import current data file
    cur_df = pd.read_csv(f"C:/Users/zoharga/Desktop/Zohar/041021 Ofir analysis - domain analysis/200622/{f}")
    cur_df.columns.values[3] = "0"

    for e in cur_df["Entry"]:
        # if this entry wasn't seen before: -> update columns values
        if new_df.loc[new_df["Entry"] == e, "Sequence kind"].item() == 'NaN':
            new_df.loc[new_df["Entry"] == e, "Sequence kind"] = sq_kind
            new_df.loc[new_df["Entry"] == e, "Position"] = cur_df.loc[cur_df["Entry"] == e, "0"].item()
        # if this entry was seen before:
        else:
            # if the new characterized sequence start position < old sequence start position -> update columns values
            if new_df.loc[new_df["Entry"] == e, "Position"].item() > cur_df.loc[cur_df["Entry"] == e, "0"].item():
                new_df.loc[new_df["Entry"] == e, "Sequence kind"] = sq_kind
                new_df.loc[new_df["Entry"] == e, "Position"] = cur_df.loc[cur_df["Entry"] == e, "0"].item()
            # if the new characterized sequence start position = old sequence start position
            # -> add k to Sequence kind column, end position might be different so set as "?"
            elif new_df.loc[new_df["Entry"] == e, "Position"].item() == cur_df.loc[cur_df["Entry"] == e, "0"].item():
                new_df.loc[new_df["Entry"] == e, "Sequence kind"] = str(new_df.loc[new_df["Entry"] == e, "Sequence kind"].item()) +", " + sq_kind

# drop "NaN" from new_df
new_df = new_df[new_df["Sequence kind"] != "NaN"]
# save new_df to csv file
new_df.to_csv("first characterized seq.csv", index=False)



