import streamlit as st
import geemap.foliumap as geemap

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
Les partenaires de l'Aïgo"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://scontent-mrs2-1.xx.fbcdn.net/v/t39.30808-6/408924114_658906496429375_3658879162690106456_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=5f2048&_nc_ohc=rGyJYg7z_P8Q7kNvgFCKYhV&_nc_ht=scontent-mrs2-1.xx&oh=00_AfDrMQuolQt11CRgzkdWWmTg4d2BdAAEHZBjwZTzpOf33g&oe=6639B4B5"
st.sidebar.image(logo)

# Customize page title
st.title("Les partenaires de l'Aïgo")

st.markdown(
    """
    """
)

st.header("Instructions")

markdown = """
1. For the [GitHub repository](https://github.com/giswqs/geemap-apps) or [use it as a template](https://github.com/new?template_name=geemap-apps&template_owner=giswqs) for your own project.
2. Customize the sidebar by changing the sidebar text and logo in each Python files.
3. Find your favorite emoji from https://emojipedia.org.
4. Add a new app to the `pages/` directory with an emoji in the file name, e.g., `1_🚀_Chart.py`.
"""

st.markdown(markdown)

m = geemap.Map()
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)
