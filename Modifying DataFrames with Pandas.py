#Project:Petal Power Inventory

import codecademylib
import pandas as pd

inventory = pd.read_csv('inventory.csv')

#1 Inspect the first 10 rows
inventory.head(10)

staten_island = inventory.head(10)

#2 Select the column 'product_description'
product_request = inventory.product_description

#3 Select 2 rows with logic 
seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')]

#4 Add column with lambda funtion 
inventory['in_stock'] = inventory.apply(lambda row: True 
    if row['quantity'] > 0 else False, index=1)

#5 Multiply 2 columns (using lambda funtion)
#inventory['total_value'] = inventory['price'] * inventory['quantity']
inventory['total_value'] = inventory.apply(lambda row: row.price * row.quantity, axis = 1)

#6 Add column that is the combination of 2 exiating ones 
combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)

# 7 Add column 
inventory['full_description'] = inventory.apply(combine_lambda, axis=1)                         

print(inventory.head(10))    

