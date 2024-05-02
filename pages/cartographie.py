import geemap.foliumap as geemap
import pandas as pd
import streamlit as st 

Map = geemap.Map(center=(43.640212, 5.097115), zoom=14)

col1, col2 = st.columns([4, 1])
options = list(geemap.basemaps.keys())
index = options.index("OpenTopoMap")

with col2:

    basemap = st.selectbox("Select a basemap:", options, index)


with col1:
    df = pd.read_csv("pages/aigo_pro.csv")
    Map.add_markers_from_xy(df, x="longitude", y="latitude", popup=["Nom", "Adresse"], icon_shape = "circle", border_color='white', icon = "pizza-slice")
    Map.add_basemap(basemap)
    Map.to_streamlit(height=700)
