import matplotlib.pyplot as plt


def plot_population2():
    # Load data
    file_data = [line.replace("\n", "").split("\t") for line in open("data/pupulation_data/population.txt").readlines()[1:]]

    # Initialize variables to store data
    annual_data = {}

    # Process data
    for entry in file_data:
        year = int(entry[0])
        city_men = int(entry[2])
        city_women = int(entry[3])
        village_men = int(entry[4])
        village_women = int(entry[5])

        # Sum population for cities and rural areas for the given year
        if year not in annual_data:
            annual_data[year] = {'city': {'men': 0, 'women': 0}, 'village': {'men': 0, 'women': 0}}

        annual_data[year]['city']['men'] += city_men
        annual_data[year]['city']['women'] += city_women
        annual_data[year]['village']['men'] += village_men
        annual_data[year]['village']['women'] += village_women

    # Ask the user for the year
    target_year = int(input("Enter the year for which you want to display data (data is available for 2013-2050): "))


    # Check if data for the given year exists
    if target_year in annual_data:
        # Retrieve data for the selected year
        data = annual_data[target_year]

        # Prepare data for pie charts
        labels = ['Men', 'Women']
        city_values = [data['city']['men'], data['city']['women']]
        village_values = [data['village']['men'], data['village']['women']]

        # Drawing pie charts
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

        # Pie chart for cities
        ax1.pie(city_values, labels=labels, autopct='%1.1f%%', startangle=90, colors=['g', 'b'])
        ax1.set_title(f'Gender distribution in cities - {target_year}')

        # Pie chart for villages
        ax2.pie(village_values, labels=labels, autopct='%1.1f%%', startangle=90, colors=['g', 'b'])
        ax2.set_title(f'Gender distribution in villages - {target_year}')

        # Show charts
        plt.show()
    else:
        print(f'Data for the year {target_year} is not available.')
