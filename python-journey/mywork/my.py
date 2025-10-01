import pandas as pd

# Read the CSV file (replace 'medals.csv' with your actual CSV filename)

df = pd.read_csv("mywork/list_of_medilist.csv")
# Set the index to 'name'
df_keys = df.set_index("name")
# Convert to dictionary
# it will make the gold , silver etc keys:
result = df_keys.to_dict()
# it will make the key country names :
# orient tells the pandas to use the "index" as keys : orient = key
With_orient = df_keys.to_dict(orient="index") # index = names = countrys names
print(result)
print("\n" * 5)
print(With_orient)
print("\n"*5)
# for getting hold of a specific data in a row :
for index, row in df_keys.iterrows():
# we write index.lower because we converted the keys to index:
    if index.lower() == "china":
        print(row.total)

# for key , value in With_orient.items():
#     if key.lower() == "china":
#         print(value.total)
print(With_orient["China"]["total"])

