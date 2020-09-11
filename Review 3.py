import codecademylib
import pandas as pd

user_visits = pd.read_csv('page_visits.csv')

# Examine the first few rows of the DataFrame
print(user_visits.head(10))

# How many visits came from each of the different sources
click_source = user_visits.groupby('utm_source').id.count().reset_index()
print(click_source)

#Calculate the number of visits to company's site from each utm_source for each month.
click_source_by_month = user_visits.groupby(['utm_source', 'month']).id.count().reset_index()

#Reorganise the table for a better understanding 
click_source_by_month_pivot = click_source_by_month.pivot(
	columns = 'month',
	index = 'utm_source',
	values = 'id').reset_index()

print(click_source_by_month_pivot)



