import geopandas as gpd
import matplotlib.pyplot as plt


# Step 1: Load the global shapefile into a GeoDataFrame
world_counties = gpd.read_file('./data/ne_10m_admin_1_states_provinces.shp')

# Step 2: Inspect the data to see the structure and find the correct column names (optional)
# print(world_counties.head())
print(world_counties.columns)
print('**********************************************')

# Step 3: Filter the GeoDataFrame for Swedish counties
# Natural Earth usually has a 'admin' column for the country and 'name' or 'name_en' for the admin region
sweden_counties = world_counties[world_counties['admin'] == 'Sweden']


# Step 2: Define the mappings from status to color and counties to status
categories = {
    'vaxx': 'yellow',
    'no_vaxx': 'purple',
    'restricted_vaxx': 'red',
    'teen_vaxx': 'green',
    'unknown': 'gray'
}

counties = {
    'Blekinge': 'vaxx',
    'Dalarna': 'unknown',
    'Gotland': 'unknown',
    'Gävleborg': 'unknown',
    'Halland': 'vaxx',
    'Jämtland': 'vaxx',
    'Jönköping': 'restricted_vaxx',
    'Kalmar': 'unknown',
    'Kronoberg': 'vaxx',
    'Norrbotten': 'restricted_vaxx',
    'Orebro': 'unknown',
    'Skåne': 'vaxx',
    'Stockholm': 'no_vaxx',
    'Södermanland': 'unknown',
    'Uppsala': 'teen_vaxx',
    'Värmland': 'unknown',
    'Västerbotten': 'restricted_vaxx',
    'Västernorrland': 'unknown',
    'Västmanland': 'restricted_vaxx',
    'Västra Götaland': 'teen_vaxx',
    'Östergötland': 'unknown'
}

# Step 3: Create a new column in the GeoDataFrame with the mapped vaccination status
sweden_counties['vaccination_status'] = sweden_counties['name'].map(counties)

# Step 4: Create another new column for colors based on vaccination status
sweden_counties['color'] = sweden_counties['vaccination_status'].map(categories)

# Step 5: Plot the map using the color mapping
fig, ax = plt.subplots(1, 1, figsize=(10, 12))
sweden_counties.plot(ax=ax, color=sweden_counties['color'], edgecolor='black')

# Add a custom legend
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], marker='o', color='w', label='Ja,från 12 år', markersize=15, markerfacecolor='green'),
    Line2D([0], [0], marker='o', color='w', label='Ja, vuxna', markersize=15, markerfacecolor='yellow'),
    Line2D([0], [0], marker='o', color='w', label='Vuxna endast med läkarintyg', markersize=15, markerfacecolor='red'),
    Line2D([0], [0], marker='o', color='w', label='Inte alls?', markersize=15, markerfacecolor='purple'),
    Line2D([0], [0], marker='o', color='w', label='Oklart', markersize=15, markerfacecolor='gray')
]
ax.legend(handles=legend_elements, loc='upper left')

plt.title('Vaccination utanför "riskgrupper"')
plt.show()
