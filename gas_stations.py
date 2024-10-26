import matplotlib.pyplot as plt
import mplcursors

file_roads = [item.replace("\n", "").split("\t") for item in open("data/gas_station_data/drogi.txt").readlines()]
file_road_categories = [item.replace("\n", "").split("\t") for item in
                        open("data/gas_station_data/kategorie.txt").readlines()]
file_companies = [item.replace("\n", "").split("\t") for item in open("data/gas_station_data/sieci.txt").readlines()]
file_gas_stations = [item.replace("\n", "").split("\t") for item in
                     open("data/gas_station_data/stacje.txt").readlines()]

roads = []
gas_stations = []
road_categories = {}
companies = {}

# Saving data from files into data structures
for item in file_roads[1:]:
    roads.append(item)

for item in file_gas_stations[1:]:
    gas_stations.append(item)

for item in file_road_categories[1:]:
    road_category_id = item[0]
    road_category_name = item[1]
    road_categories[road_category_id] = road_category_name

for item in file_companies[1:]:
    company_id = int(item[0])
    company_name = item[1]
    companies[company_id] = company_name

# Merging data

for item in roads:
    road_category = item[3]
    if road_category in road_categories:
        item[3] = road_categories[road_category]

# Top 20 roads with the biggest number of gas stations per kilometer

gas_stations_per_road_count = {}

for item in gas_stations:
    road_id = int(item[1])

    if road_id in gas_stations_per_road_count:
        gas_stations_per_road_count[road_id] += 1
    else:
        gas_stations_per_road_count[road_id] = 1

number_of_stations_per_kilometer_per_road = []

for item in roads:
    road_id = int(item[0])
    kilometers = int(item[2])
    road_name = item[1]
    gas_stations_count = gas_stations_per_road_count.get(road_id, 0)

    gas_station_per_100_kilometers = round(gas_stations_count / kilometers * 100, 5) if kilometers > 0 else 0
    number_of_stations_per_kilometer_per_road.append([road_id, road_name, gas_station_per_100_kilometers])

number_of_stations_per_kilometer_per_road.sort(key=lambda x: x[2], reverse=True)
top_20_stations_per_kilometer = number_of_stations_per_kilometer_per_road[:200]

road_names = [item[1] for item in top_20_stations_per_kilometer]
stations_per_kilometer = [item[2] for item in top_20_stations_per_kilometer]

plt.figure(figsize=(14, 5))
bars = plt.bar(range(len(road_names)), stations_per_kilometer)

plt.xlabel("Road Name")
plt.ylabel("Stations per 100 kilometers")
plt.title("Top 200 Roads by stations per 100 kilometers")

plt.xticks([])

cursor = mplcursors.cursor(bars, hover=True)


@cursor.connect("add")
def on_add(sel):
    # Show the road name and the stations per kilometer on hover
    sel.annotation.set_text(
        f"{road_names[sel.target.index]}\n{stations_per_kilometer[sel.target.index]:.2f} stations/km")


plt.tight_layout()
plt.show()
