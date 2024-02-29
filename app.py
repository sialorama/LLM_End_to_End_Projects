import streamlit as st

#  set app to wide mode
st.set_page_config(layout="wide")

# title of our app
st.title('Uber Writer')

# create a subheader
st.subheader("Vous pouvez désormais créer vos blogs avec l'aide de l'IA.")
st.subheader("Uber Writer est votre nouveau support de productivité.")
Blog = """
 
"What Is Generative IA? How Does Generative IA Works?"

Generative AI, short for Generative Artificial Intelligence, refers to a class of algorithms and models that are designed to generate new content or data that is similar to, but not exactly the same as, the data it was trained on. These algorithms are particularly adept at creating new content such as images, text, audio, and even video.

Here's a general overview of how generative AI works:

Training Data: Generative AI models are trained on large datasets of examples relevant to the type of content they are meant to generate. For instance, a text generation model might be trained on a corpus of books, articles, or internet text, while an image generation model might be trained on a dataset of images.

Learning Patterns: During the training process, the model learns the underlying patterns and structures present in the training data. This is typically accomplished through techniques such as deep learning, where neural networks are used to model complex relationships in the data.

Generating New Content: Once trained, the generative AI model can be used to generate new content by sampling from the learned patterns. For example, a text generation model might be given a prompt and asked to continue writing from there, while an image generation model might be asked to generate a new image based on certain input parameters.

Evaluation and Refinement: The generated content is often evaluated by humans or by other algorithms to assess its quality and relevance. Based on this feedback, the generative AI model can be refined and improved through further training iterations.

Controlled Generation: Some generative AI models allow for fine-grained control over the generated output. This can be achieved through techniques such as conditional generation, where additional input parameters are provided to influence the generated content in specific ways.

Overall, generative AI holds great potential for a wide range of applications, including creative tasks such as art generation and storytelling, as well as practical tasks such as data augmentation and content creation for marketing purposes. However, it also raises important ethical considerations, particularly regarding the potential misuse of generated content for deceptive or malicious purposes.
"""
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

    prompt_parts = [
        (f"Generate a comprehensive, engaging blog post relevant to the given title \"{blog_title}\" and keywords in the blog post\"    \".Make sure to incorporate these keywords in the blog post. The blog should be approximately 500 words.")
    ]
    # Submit button
    submit_button = st.button("Générer le blog")

if submit_button:
    # st.image("https://oaidalleapiproduscus.blob.core.windows.net/private/org-")


    st.write(Blog)