import folium 
import pandas as pd


stores_data = {
    'City': ['New York', 'Los Angeles', 'Chicago'],
    'Lat': [40.7128, 34.0522, 41.8781],
    'Lon': [-74.0060, -118.2437, -87.6298]
}

demand_data = {
    'City': ['Houston', 'Phoenix'],
    'Lat': [29.7604, 33.4484],
    'Lon': [-95.3698, -112.0740]
}

df_stores = pd.DataFrame(stores_data)
df_demand = pd.DataFrame(demand_data)


m = folium.Map(location=[39.8283, -98.5795], zoom_start=4)


for idx, row in df_stores.iterrows():
    folium.Marker([row['Lat'], row['Lon']], popup=f"Existing Store: {row['City']}", icon=folium.Icon(color='blue')).add_to(m)


for idx, row in df_demand.iterrows():
    folium.CircleMarker(
        location=[row['Lat'], row['Lon']],
        radius=15,
        popup=f"High Demand / Expansion Area: {row['City']}",
        color='red',
        fill=True,
        fill_color='red'
    ).add_to(m)


m.save('geospatial_map.html')
print("Successfully map geospatial_map.html as saved")