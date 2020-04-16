import pandas as pd 
from matplotlib import pyplot as plt

sample_data = pd.read_csv('ExampleFile.csv')

plt.plot(sample_data.Time(days),sample_data.Non-infected/sample_data.Total-population.iloc[0])
plt.plot(sample_data.Time(days),sample_data.Infected/sample_data.Total-population.iloc[0])
plt.plot(sample_data.Time(days),sample_data.Isolated from the network/sample_data.Total-population.iloc[0])


plt.xlabel('Time(days)')
plt.ylabel('Fraction of population')
plt.legend(["Non-infected","Infected","Isolated from the network"])
plt.title('Algorithm implemented without manual input of params')

plt.show()
