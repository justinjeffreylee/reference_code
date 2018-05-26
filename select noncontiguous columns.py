"# import\n",
    "import numpy as np\n",
    "\n",
    "# create the standard errors dataframe\n",
    "df_SE = df.iloc[:, np.r_[:2, 12:22]]\n",
    "\n",
    "# view the first few rows to confirm this was successful\n",
    "df_SE.head()"
