import pandas as pd
import numpy as np

aqr = pd.read_excel(r'C:\Users\ianko\Downloads\updated-master-sheet.xlsx', sheet_name="acquisitions")
fr = pd.read_excel(r'C:\Users\ianko\Downloads\updated-master-sheet.xlsx', sheet_name="funding-rounds")
ipo = pd.read_excel(r'C:\Users\ianko\Downloads\updated-master-sheet.xlsx', sheet_name="ipos")
df = pd.DataFrame(data={'Startup' : np.array(["blablablablablabla"], dtype=object),
                       'First-Round' : np.array([0], dtype=int),
                       'Last-Round' : np.array([0], dtype=int),
                       'Total Funding' : np.array([0], dtype=int),
                       'IPO' : np.array([0], dtype=int),
                       'Acquisition' : np.array([0], dtype=int),
                     }
              )

for index, row in fr.iterrows():
    if (df['Startup'].iloc[-1] == row["Startup"]):
        df["Total Funding"].iloc[-1] = df['Total Funding'].iloc[-1] + row["Raised"]
        if (row["First Round?"] == 1):
            df["First-Round"].iloc[-1] = row["Raised"]
        if (row["Last Round?"] == 1):
            df["Last-Round"].iloc[-1] = row["Raised"]
    else:
        df2 = {'Startup': row["Startup"], 'First-Round': 0, 'Last-Round': 0, 'Total Funding': 0, 'IPO': 0, 'Acquisition': 0}
        df = df.append(df2, ignore_index = True)
        df["Total Funding"].iloc[-1] = df['Total Funding'].iloc[-1] + row["Raised"]
        print(row["First Round?"])
        if (row["First Round?"] == 1):
            df["First-Round"].iloc[-1] = row["Raised"]
        if (row["Last Round?"] == 1):
            df["Last-Round"].iloc[-1] = row["Raised"]     

for index, row in aqr.iterrows():
    indexes = np.where(df["Startup"] == row["Startup"])
    if (len(indexes[0]) != 0):
        df.at[int(indexes[0]), 'Acquisition'] = row["Raised"]  
    
for index, row in ipo.iterrows():
    comparison = []
    indexes = np.where(df["Startup"] == row["Startup"])
    if (len(indexes[0]) != 0):
        df.at[int(indexes[0]), 'IPO'] = row["Raised"]

print("Generating...")
df.to_excel(r'C:\Users\ianko\Downloads\finaldatasheet.xlsx') 
print("Done!")