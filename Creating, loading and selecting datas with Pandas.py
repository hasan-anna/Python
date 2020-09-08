#Review: CREATING, LOADING, AND SELECTING DATA WITH PANDAS

import codecademylib
import pandas as pd

#Part 1: reading the csv
orders = pd.read_csv('shoefly.csv')

#Part 2: inspecting the first five lines of data
print(orders.head(5))

#Part 3: selecting the column 'email'
emails = orders.email

#Part 4: Select multiple rows with logic 
frances_palmer = orders[(orders.first_name == 'Frances') & (orders.last_name == 'Palmer')]

#Part 5: Select multiple rows with logic 
comfy_shoes = orders[orders.shoe_type.isin(['clogs', 'boots', 'ballet flats'])]
