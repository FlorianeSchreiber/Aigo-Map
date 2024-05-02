import streamlit as st
import geemap.foliumap as geemap
from st_pages import Page, show_pages, add_page_title
st.set_page_config(layout="wide")

show_pages(
    [
        Page("app.py", "Bonjour", "🏠"),
        Page("pages/cartographie.py", " Carte", ":world_map:"),
    ]
)


# Customize the sidebar
markdown = """
Les partenaires de l'Aïgo"""

st.sidebar.title("A Propos")
st.sidebar.info(markdown)
logo = "https://scontent-mrs2-1.xx.fbcdn.net/v/t39.30808-6/408924114_658906496429375_3658879162690106456_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=5f2048&_nc_ohc=rGyJYg7z_P8Q7kNvgFCKYhV&_nc_ht=scontent-mrs2-1.xx&oh=00_AfDrMQuolQt11CRgzkdWWmTg4d2BdAAEHZBjwZTzpOf33g&oe=6639B4B5"
st.sidebar.image(logo)

# Customize page title
st.title("Les partenaires de l'Aïgo")

st.markdown(
    """
    """
)

st.header("A Salon-de-Provence")

markdown_marche = """
Sur les marchés salonais 
- L’Ami du pain (Alban)= boulanger itinérant 
- Matthieu Fillacier = paysan boulanger (comptoir) 
- Aznar Valentin = producteur maraîcher 
- Catherine Ponçon = producteur maraicher Bio (comptoir) 
- EARL légumerie BIO du Lubéron = conserves BIO 
- Olivier Tronc = producteur fruitier 
- Pascal Gibellin = producteur maraîcher 
- Robert Rolland = producteur de pommes 
- La ferme d‘Eygaline = éleveur de volailles 
- GAEC Faudon = produits de la ferme 
- La ferme de l’Authentique = élevage de chèvres, fromage et œufs 
- La poule de Crau = éleveur de volailles 
- Le champ des potions = Malika Porot, plantes aromatiques et médicinales
"""

markdown_alimentation = """
Les Magasins d’alimentation
- Chocolaterie Nostradamus = chocolatier, glacier et confiseur 
- Boulangerie Demoiselles = boulanger et biscuiterie 
- La Mavinon = boulanger, pâtissier 
- Pâtisserie Stéphanie Jean = pâtissier 
- Brasserie Sapristi = brasserie & producteur de bières salonaises 
- Daniel Egéa = producteur fruitier 
- De la Vigne à l’Olivier = caviste 
- EARL Roustan = huile d’olive & vins 
- La Vie Claire = épicerie Bio 
- Le mas des bories = producteur oléicole 
- Ma saison AB = producteur fruits & légumes 
- Maison Bourgeon = boutique de thés (comptoir) 
- Maison Severy = boucher, charcutier, traiteur 
- Fromagerie de l’Horloge = crémier & fromager """

col1, col2 = st.columns([1, 1])

with col1 :
    st.markdown(markdown_marche)

with col2: 
    st.markdown(markdown_alimentation)
