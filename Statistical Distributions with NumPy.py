#Project: Election Results
#Election has occurred, compare the survey responses to the actual results.

import codecademylib
import numpy as np
from matplotlib import pyplot as plt

#Telephone survey response list 
survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']

#How many people answered ‘Ceballos’
total_ceballos = sum([1 for n in survey_responses if n == 'Ceballos'])
print(total_ceballos)

#Percentage of people that voted for Ceballos
percentage_ceballos = 100 * total_ceballos/len(survey_responses)
#Outcome 33
print(percentage_ceballos)
#Outcome 47%

#54% of the 10.000 population voted for Ceballos but prediction was 47%
possible_surveys = np.random.binomial(len(survey_responses), 0.54, size = 10000)/float(len(survey_responses))

plt.hist(possible_surveys, range=(0,1), bins=20)
plt.show()
#Outcome, wide spread of data between 40% and 70% and more concentrated between 50% and 55%. 

#What is the probability for Ceballos to receive less than 50% vote in the surveys?
ceballos_loss_surveys = np.mean (possible_surveys < 0.5)
print(ceballos_loss_surveys)
#Outcome 0.2139 = 21%

plt.close()

#What if the survey sample size gets bigger? 7000 
large_survey = np.random.binomial(7000, 0.54, size = 10000)/float(7000)

plt.hist(large_survey, range=(0,1), bins=20)

plt.show(large_survey)
#Outcome, data concentrated at 54% (more accurate prediction) 

#What is the probability for Ceballos to receive less than 50% vote in the nsurveys with bigger sample size?
ceballos_loss_new = np.mean(large_survey < 0.5)
print(ceballos_loss_new)
#Outcome 0.0 = no chance to get less than 50% vote for Ceballos
