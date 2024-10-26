# Reading data from files and saving to data structures
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

# Exported data structures
__all__ = ['roads', 'gas_stations', 'road_categories', 'companies']