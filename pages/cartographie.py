import geemap.foliumap as geemap
import pandas as pd
import streamlit as st 

Map = geemap.Map(center=(43.640212, 5.097115), zoom=14)

options = st.multiselect("Les catégories de Commerces", ['Magasins d’alimentation', 'Au restaurant', 'A La Ferme', 'Traiteurs' , 'Culture', 'Arts de la maison', 'Santé soins et soins alternatifs', 'Vêtements', 'Beauté', 'Services', 'Construction', 'Sport', 'Gîte'], ['Magasins d’alimentation', 'Au restaurant'])

if 'Au restaurant' in options :
  df_resto = pd.read_csv("pages/aigo_restaurants.csv")
  Map.add_markers_from_xy(df_resto, x="longitude", y="latitude", popup=["Nom", "Adresse"], icon_shape = "circle", border_color='blue', icon = "cutlery", layer_name="Au Restaurant")
if "Magasins d’alimentation" in options :
  st.markdown("Alim")
  df_alim = pd.read_csv("pages/aigo_alimentation.csv")
  Map.add_markers_from_xy(df_alim, x="longitude", y="latitude", popup=["Nom", "Adresse"], icon_shape = "circle", border_color='red', icon = "fork", layer_name="Magasins d’alimentation")

Map.add_basemap("Terrain")
Map.to_streamlit(height=700)
