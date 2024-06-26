import geemap.foliumap as geemap
import pandas as pd
import streamlit as st 

st.set_page_config(layout="wide")

Map = geemap.Map(center=(43.640212, 5.097115), zoom=14)

options = st.multiselect("Les catégories de Commerces", ['Magasins d’alimentation', 'Au restaurant', 'A La Ferme', 'Traiteurs' , 'Culture', 'Arts de la maison', 'Santé soins et soins alternatifs', 'Vêtements', 'Beauté', 'Services', 'Construction', 'Sport', 'Gîte'], ['Magasins d’alimentation', 'Au restaurant'])

if 'Au restaurant' in options :
  df_resto = pd.read_csv("pages/aigo_restaurants.csv")
  Map.add_markers_from_xy(df_resto, x="longitude", y="latitude", popup=["Nom", "Adresse"], icon_shape = "circle", border_color='black', border_width=1, icon = "cutlery", layer_name="Au Restaurant", background_color = "#7a7a99")
if "Magasins d’alimentation" in options :
  df_alim = pd.read_csv("pages/aigo_alimentation.csv")
  Map.add_markers_from_xy(df_alim, x="longitude", y="latitude", popup=["Nom", "Adresse"], icon_shape = "circle", border_color='black', border_width=1, icon = "basket-shopping", layer_name="Magasins d’alimentation", background_color = "#997A7A")
Map.add_basemap("Terrain")
Map.to_streamlit()
