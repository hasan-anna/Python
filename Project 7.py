#Project: CrunchieMunchies(CM), demonstrate that CM is more healthy is comparison to other cereal brands (60 calories per serving).

import numpy as np

#CSV file has nutritional data on several competitors 
calorie_stats = np.genfromtxt('cereal.csv', delimiter = ',')

#Calculate average
average_calories = np.mean(calorie_stats)
print(average_calories)
#Output 106

#Sort out data 
calorie_stats_sorted = np.sort(calorie_stats)
print(calorie_stats_sorted)

#Calculate median 
median_calories = np.median(calorie_stats)
print(median_calories)
#Output 110

#Calculate different percentiles until we find the lowest percentile that is greater than 60. 
print np.percentile(calorie_stats, 25)      #Output 100
print np.percentile(calorie_stats, 12)      #Output 90
print np.percentile(calorie_stats, 7)       #Output 83
print np.percentile(calorie_stats, 4)       #Output 70
nth_percentile = 4

#Calculate percentage for values bigger than 60
more_calories = np.mean(calorie_stats > 60)
print(more_calories)
#Output 96%

#Calculate standard deviation 
calorie_std = np.std(calorie_stats)
print(calorie_std)
#Output 19

#Data analysis: 1. CM has less calories compare to his competitors.
#1.1 Being in the 4th percentile means that 96% of other cereals have more calories. 
#2. From the mean and std we know that the spread between one std is between 87 and 125 calories. 
#2.1 60 calories are below 87 so not in the standard deviation. This means that there is a significant difference. 