#query using numbers

month_1 = pd.DataFrame(spp_df.query('month==1'))

#query using bloody text strings
df_08 = df_08.query('cert_region == "CA"')

#who the hell decided you needed double quotes to query text, because you don't do it here
df_08['cert_region'] == 'CA'