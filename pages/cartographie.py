import geemap.foliumap as geemap
import pandas as pd
import streamlit as st 

Map = geemap.Map(center=(43.640212, 5.097115), zoom=14)

options = st.multiselect("Les catégories de Commerces", ['Magasins d’alimentation', 'Au restaurant', 'A La Ferme', 'Traiteurs' , 'Culture', 'Arts de la maison', 'Santé soins et soins alternatifs', 'Vêtements', 'Beauté', 'Services', 'Construction', 'Sport', 'Gîte'], ['Magasins d’alimentation', 'Au restaurant'])

df = pd.read_csv("pages/aigo_pro.csv")
Map.add_markers_from_xy(df, x="longitude", y="latitude", popup=["Nom", "Adresse"], icon_shape = "circle", border_color='blue', icon = "pizza-slice", layer_name="Restaurants")
Map.add_basemap("Terrain")
Map.to_streamlit(height=700)
