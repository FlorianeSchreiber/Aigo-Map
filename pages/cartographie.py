import streamlit as st
import geemap.foliumap as geemap

st.title("Interactive Map")

m = geemap.Map(center=(43.640212, 5.097115), zoom=12)
m.add_point((43.641371, 5.097306), popup='Espigaou')
m.to_streamlit(height=700)
