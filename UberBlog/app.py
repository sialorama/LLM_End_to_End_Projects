import streamlit as st

#  set app to wide mode
st.set_page_config(layout="wide")

# title of our app
st.title('Uber Writer')

# create a subheader
st.subheader("Vous pouvez désormais créer des blogs parfaits avec l'aide de l'IA, Uber Writer est votre nouveau compagnon rédactionnel.")

# Sidebar for user input

with st.sidebar:
    st.title("Insérez les détails de votre blog")
    st.subheader("Saisissez les détails du blog que vous voulez créer")
    # Blog title
    blog_title = st.text_input("Titre du blog")
    # Keywords input
    keywords = st. text_area("Mots clés (séparés d'une virgule)")
    # Number of words
    num_words = st.slider("Nombre de mots", min_value=250, max_value=1000, step=250)
    # Number pf images
    num_images = st.number_input("Nombre d'images", min_value=1, max_value=5, step=1)
    # Submit button
    submit_button = st.button("Générer le blog")

