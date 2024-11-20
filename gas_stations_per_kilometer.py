import matplotlib.pyplot as plt
from gas_stations_read_data import roads, gas_stations, road_categories


def plot_gas_stations_per_kilometer():
    # Merging data
    for item in roads:
        road_category = item[3]
        if road_category in road_categories:
            item[3] = road_categories[road_category]

    gas_stations_per_road_count = {}

    # count stations per road
    for item in gas_stations:
        road_id = int(item[1])

        if road_id in gas_stations_per_road_count:
            gas_stations_per_road_count[road_id] += 1
        else:
            gas_stations_per_road_count[road_id] = 1

    # count number of stations per 100km
    number_of_stations_per_kilometer_per_road = []

    for item in roads:
        road_id = int(item[0])
        kilometers = int(item[2])
        road_name = item[1]
        gas_stations_count = gas_stations_per_road_count.get(road_id, 0)

        gas_station_per_100_kilometers = round(gas_stations_count / kilometers * 100, 5) if kilometers > 0 else 0
        number_of_stations_per_kilometer_per_road.append([road_id, road_name, gas_station_per_100_kilometers])

    # find max value per 100km
    max_value = 0.0
    for item in number_of_stations_per_kilometer_per_road:
        if item[2] > max_value:
            max_value = item[2]

    # create ranges list
    interval = 1
    ranges = list(range(0, int(max_value) + 2, interval))

    # prepare empty ranges dictionary
    range_counts = {}
    for item in ranges:
        range_counts[f"{item}-{item+1}"] = 0

    # fill dictionary with number of roads for range
    for item in number_of_stations_per_kilometer_per_road:
        density = item[2]

        for r in ranges:
            if r <= density < r + interval:
                range_counts[f"{r}-{r+1}"] += 1

    ranges_plot = list(range_counts.keys())
    values_plot = list(range_counts.values())

    plt.figure(figsize=(10, 6))
    plt.bar(ranges_plot, values_plot)

    for i in range(len(ranges_plot)):
        plt.text(i, values_plot[i], values_plot[i], ha = 'center')

    plt.xlabel('Number of stations per 100km')
    plt.ylabel('Number of roads')
    plt.title('Number of roads depending on gas stations density')

    plt.tight_layout()
    plt.show()

