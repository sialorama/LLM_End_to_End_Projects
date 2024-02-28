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