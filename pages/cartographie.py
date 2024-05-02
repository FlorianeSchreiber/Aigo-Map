import geemap.foliumap as geemap
import pandas as pd

Map = geemap.Map(center=(43.640212, 5.097115), zoom=14)
df = pd.read_csv("aigo_pro.csv")
#df = df.drop(['sov_a3', 'region'], axis=1)
Map.add_markers_from_xy(df, x="longitude", y="latitude", popup=["Nom", "Adresse"], icon_shape = "circle", border_color='white', icon = "pizza-slice")
Map.to_streamlit(height=700)
