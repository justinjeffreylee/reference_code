rename columns names with year appended

df_08.rename(columns=lambda x: x[:10] + "_2008", inplace=True)
