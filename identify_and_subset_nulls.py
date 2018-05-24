# count number of rows in this column that have a null value
df.columnname.isnull().sum()

# subset rows with null values
df[df.columnname.isnull()]
