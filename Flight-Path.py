import streamlit as st
import cartopy.crs as ccrs
import cartopy.feature as cs
import matplotlib.pyplot as plt

st.title("Flight path between 2 cities")
st.subheader("Choose any 2 cities")

cities = {
    'New York': [40.7128, -74.0059],
    'London': [51.5074, -0.1278],
    'Tokyo': [35.6895,139.6917],
    'Sydney': [-33.8688,151.2093],
    'Cape Town': [-33.9249,18.4241],
    'Rio de Janeiro': [-22.9068,-43.1729],
    'Paris': [48.8566,2.3522],
    'Moscow': [55.7558,37.6173],
    'Mumbai': [19.0760,72.8777]


}

city_name=cities.keys()
city_list=list(city_name)

city1=st.selectbox("Choose any city:",city_list)
city2=st.selectbox("Choose any other city:",city_list)

if st.button("Generate flight path"):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.set_extent([-180, 180, -90, 90], crs=ccrs.PlateCarree())
    ax.add_feature(cs.OCEAN, facecolor='lightblue')
    ax.add_feature(cs.LAND, facecolor='lightgreen')
    ax.add_feature(cs.BORDERS, facecolor='black')
    ax.add_feature(cs.COASTLINE, facecolor='black')

    for city, (lat, lon) in cities.items():
        ax.plot(lon, lat, marker='o', color='red', markersize=4, transform=ccrs.PlateCarree())
        ax.text(lon + 5, lat, city, color='blue', transform=ccrs.PlateCarree(), fontsize='7')

    lat_ct, lon_ct = cities[city1]
    lat_s, lon_s = cities[city2]

    ax.plot([lon_ct, lon_s], [lat_ct, lat_s], color='blue', linewidth=3, transform=ccrs.Geodetic())
    ax.set_title("Flight path between the 2 cities")

    st.pyplot(fig)
