#replace all spaces in columns names with '_' and lowercase 

df_08.rename(columns=lambda x: x.strip().lower().replace(" ", "_"), inplace=True)
