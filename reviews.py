# add your code here

# add imports to script

import pandas as pd
import zipfile

# open zipped file as dataframe

#with zipfile.ZipFile('data/winemag-data-130k-v2.csv.zip', 'r') as zip_ref:
   # zip_ref.extract('winemag-data-130k-v2.csv.zip', '/data')

df = pd.read_csv('data/winemag-data-130k-v2.csv.zip', index_col=0)

wine_df = df
wine_df['count'] = 1



review_av = df.groupby('country').agg({'count': 'sum', 'points': 'mean'}).reset_index()
review_av['points'] = review_av['points'].round(1)
sorted_reviews = review_av.sort_values(by='count', ascending=False)

sorted_reviews.to_csv('data/reviews-per-country.csv', index=False)



# reviews = df.loc[:, ['country', 'count', 'points']]

# column_list = df.columns.tolist()


#print(df.groupby(['country']).points.agg(['mean']))


df['Count'] = df.country.value_counts()

print(review_av) 