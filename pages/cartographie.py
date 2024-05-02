import streamlit as st
import geemap.foliumap as geemap

st.title("Interactive Map")

col1, col2 = st.columns([4, 1])
options = list(geemap.basemaps.keys())
index = options.index("OpenTopoMap")

with col2:

    basemap = st.selectbox("Select a basemap:", options, index)


with col1:

    m = geemap.Map(center=(43.640212, 5.097115), zoom=12)
    m.add_basemap(basemap)
    m.to_streamlit(height=700)
