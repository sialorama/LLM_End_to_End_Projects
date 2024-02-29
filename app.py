import streamlit as st
import google.generativeai as genai
from apikey import google_gemini_api_key, openai_api_key
from openai import OpenAI
from streamlit_carousel import carousel
genai.configure(api_key=google_gemini_api_key)
client = OpenAI(api_key=openai_api_key)

# dictionary for the carousel
single_image = dict(
    title="",
    text="",
    interval=None,
    img=""
)

# Set up the model
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_setting  = [
    {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    }
    ]

# setting up our model
model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_setting) 

#  set app to wide mode
st.set_page_config(layout="wide")

# title of our app
st.title('Uber Writer')

# create a subheader
st.subheader("Vous pouvez désormais créer vos blogs avec l'aide de l'IA.")
st.subheader("Uber Writer est votre nouveau support de productivité.")

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
    # prompt parts gived by user
    prompt_parts = [
        (f"Generate a comprehensive, engaging blog post relevant to the given title \"{blog_title}\" and keywords in the blog post\"{keywords} \".Make sure to incorporate these keywords in the blog post. The blog should be approximately {num_words} words.")
        ]

    # Submit button
    submit_button = st.button("Générer le blog")

if submit_button:
        
    response = model.generate_content(prompt_parts)
    # list of images created
    # images = []
    images_gallery=[]

    # loop to create the number of images selected by user
    for i in range (num_images):
        image_response = client.images.generate(
        model="dall-e-3",
        prompt= f"Générer un article sur le thème : {blog_title}",
        size="1024x1024",
        quality="standard",
        n=1,
        )
        new_image = single_image.copy() 
        new_image["title"] = f"Image {i+1}"
        new_image["text"] = f"{blog_title}"
        new_image["img"] = image_response.data[0].url
        images_gallery.append(new_image)

    st.title("Image(s) proposées :")
    carousel(items=images_gallery, width=1)
    
    st.title("Votre article :")
    st.write(response)