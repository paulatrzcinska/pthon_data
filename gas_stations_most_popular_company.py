import matplotlib.pyplot as plt
import mplcursors
from gas_stations_read_data import roads, gas_stations, road_categories, companies


def plot_gas_stations_most_popular_company(selected_company):
    # Create dictionary with road categories
    road_categories_dictionary = {}
    for item in roads:
        road_category = item[3]
        if road_category in road_categories:
            road_categories_dictionary[item[0]] = road_categories[road_category]

    # Append road category to the list of gas stations
    for item in gas_stations:
        road_id = item[1]
        if road_id in road_categories_dictionary:
            item.append(road_categories_dictionary[road_id])

    company_category_counts = {}

    for item in gas_stations:
        company_id = item[2]
        road_category = item[3]

        company_name = companies.get(int(company_id))

        # Initialize nested dictionary if company_id is new
        if company_name not in company_category_counts:
            company_category_counts[company_name] = {}

        # Increment count for the road category within the company
        if road_category in company_category_counts[company_name]:
            company_category_counts[company_name][road_category] += 1
        else:
            company_category_counts[company_name][road_category] = 1

    if selected_company in company_category_counts:
        category_counts = company_category_counts[selected_company]
        labels = list(category_counts.keys())
        sizes = list(category_counts.values())

        plt.figure()
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title(f'Gas Stations by Road Category for {selected_company}')
        plt.axis('equal')  # Equal aspect ratio to ensure pie chart is circular
        plt.show()
