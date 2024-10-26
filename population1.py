import numpy as np
import matplotlib.pyplot as plt

# Load data, skipping the first row
file_data = [line.replace("\n", "").split("\t") for line in open("data/pupulation_data/population.txt").readlines()[1:]]

annual_data = {}

# Process data
for entry in file_data:
    year = int(entry[0])
    city_men = int(entry[2])
    city_women = int(entry[3])
    village_men = int(entry[4])
    village_women = int(entry[5])

    # Sum population in cities and rural areas
    city_population = city_men + city_women
    village_population = village_men + village_women

    # Summing for each year
    if year not in annual_data:
        annual_data[year] = {'city': 0, 'village': 0}

    annual_data[year]['city'] += city_population
    annual_data[year]['village'] += village_population

# Prepare data for plotting
years = sorted(annual_data.keys())
city_to_village_ratio = [annual_data[year]['city'] / annual_data[year]['village'] for year in years]

# Plotting the graph
plt.plot(years, city_to_village_ratio, marker='.')
plt.title('City to Village Population Ratio Over the Years')
plt.xlabel('Year')
plt.ylabel('City to Village Population Ratio')
plt.grid(True)

# Show plot
plt.show()




