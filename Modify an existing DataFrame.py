#Review: modify an existing DataFrame

import codecademylib
import pandas as pd

orders = pd.read_csv('shoefly.csv')

#1 Examine the first 5 rows of the data
print(orders.head(5))

#2 Add a new column by taking values from an existing column 
orders['shoe_source'] = orders.shoe_material.apply(lambda x: \
                        	'animal' if x == 'leather'else 'vegan')

#3 Add a new column by taking values from 2 existing columns 
orders['salutation'] = orders.apply(lambda row: \
                                    'Dear Mr. ' + row['last_name']
                                    if row['gender'] == 'male'
                                    else 'Dear Ms. ' + row['last_name'],
                                    axis=1)
