import geemap.foliumap as geemap
import pandas as pd

Map = geemap.Map(center=(43.640212, 5.097115), zoom=14)
df = pd.read_csv("aigo_pro.csv")
Map.add_markers_from_xy(df, x="longitude", y="latitude", popup=["Nom", "Adresse"], icon_shape = "circle", border_color='white', icon = "pizza-slice")
Map.to_streamlit(height=700)
