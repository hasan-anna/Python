# Prject: A/B Testing for ShoeFly.com
# An online shoe store, ShoeFly.com is performing an A/B Test. They have two different versions of an ad, which they have placed on different social media platforms. They want to know how the two ads are performing on each platform on each day of the week. Analyze the data using aggregate measures.

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
clicks_pivot = clicks_by_source.pivot(
  columns = 'is_click',
  index = 'utm_source',
  values = 'user_id').reset_index()

#6 Percent of people who clicked? Total Who Clicked / (Total Who Clicked + Total Who Did Not Click)
clicks_pivot['percent_clicked'] = \
   clicks_pivot[True] / \
   (clicks_pivot[True] + 
    clicks_pivot[False])

print('percent_clicked')


