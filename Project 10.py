#Project: A/B Testing for ShoeFly.com

import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

#1 Examine the first few rows
print(ad_clicks.head(10))

#2 Which ad platform is getting most of the views?
ad_clicks.groupby('utm_source').user_id.count().reset_index()

#3 Create a new column which is True if ad_click_timestamp is not null and False otherwise.
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestampis.null()

#4 The percent of people who clicked on ads from each utm_source
clicks_by_source = ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()

#5 Pivot/Reorganize the table 
clicks_by_source_pivot = clicks_by_source.pivot(
  columns = 'is_click',
  index = 'utm_source',
  values = 'user_id'
  )\
  .reset_index()

#6 Percent of people who clicked? Total Who Clicked / (Total Who Clicked + Total Who Did Not Click)
clicks_pivot['percent_clicked'] = \
   clicks_pivot[True] / \
   (clicks_pivot[True] + 
    clicks_pivot[False])

print('percent_clicked')


#7 The column 'experimental_group' tells whether the user was shown Ad A or Ad B. Were approximately the same number of people shown both adds?
print(ad_clicks.groupby('experimental_group').user_id\
 .count()\
 .reset_index()
)

#8 Using the column 'is_click', check if a greater percentage of users clicked on Ad A or Ad B. 
print(ad_clicks.groupby(['experimental_group','is_click']).user_id\
  .count()\
  .reset_index()\
  .pivot(
  columns = 'is_click',
  index = 'experimental_group',
  values = 'user_id'
  )\
  .reset_index()
)

#8 Create two DataFrames: 'a_clicks' and 'b_clicks', which contain only the results for A group and B group. 
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A'] 
print('A')

b_clicks = ad_clicks[ad_clicks.experimental_group == 'B'] 
print('B')


