import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Die Alkocops", page_icon="🍺", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_rock = load_lottieurl("https://lottie.host/c27869d1-603f-4f6e-9b91-fc2cf17c128d/xnNh83q1DP.json")
lottie_bier = load_lottieurl("https://lottie.host/95df498a-2d7a-4abb-8eb3-a8542f8759f7/Mbflv91AhA.json")

img_band1 = Image.open("images/foto1.jpg")
img_band2 = Image.open("images/foto2.jpg")

# ---- HEADER SECTION ----
with st.container():
    st.write("---")
    text_column, image_column = st.columns(2)
    with text_column:
        st.subheader("¿Qué pasa cabrones?")
        st.title("Wir sind die Alkocops! 🍻")
        st.write(
            "Ob Wohnungsmarkt, Clubsterben oder Craftbier: Die Alkocops haben etwas dagegen. Laut ChatGPT sind ihre Lieder wohl eine ''sozialkritische Faust ins Gesicht'', aber bescheiden wie sie sind, konzentrieren sie sich lieber auf das Wesentliche: Dosenbier verhaften!"
        )
        st.write("[ 📸 Instagram >](https://www.instagram.com/alkocops/?hl=de)")
        st.write("[ 🎵 Spotify >](https://open.spotify.com/intl-de/artist/6UolTF33q9gCE3kDK6tuTU?si=up3DRDMuQs6PF3vsJ1ZHhQ)")
        st.write("[ 🏕 Bandcamp >](https://diealkocops.bandcamp.com/)")
        st.write("[ 🎥 YouTube >](https://www.youtube.com/@diealkocops6613)")
    with image_column:
        st.image(img_band2)
    
# ---- KONZERTE ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with right_column:
        st.header("Konzerte")
        st.subheader("2024:")
        st.write("23.03. Laut für Vielfalt! im SAK Lörrach (mit Skabooom et al.)")
        st.write("05.04. Schlosskeller Emmendingen (mit Wagner Brutal)")
        st.write("18.05. Sonnenkeller Balingen (mit The Snouts und Der Ganze Rest)")
    with left_column:
        st_lottie(lottie_rock, height=300, key="rock")

# ---- PROJECTS ----
# with st.container():
#     st.write("---")
#     st.header("My Projects")
#     st.write("##")
#     image_column, text_column = st.columns((1, 2))
#     with image_column:
#         st.image(img_lottie_animation)
#     with text_column:
#         st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
#         st.write(
#             """
#             Learn how to use Lottie Files in Streamlit!
#             Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do it!
#             In this tutorial, I'll show you exactly how to do it
#             """
#         )
#         st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)")
# with st.container():
#     image_column, text_column = st.columns((1, 2))
#     with image_column:
#         st.image(img_contact_form)
#     with text_column:
#         st.subheader("How To Add A Contact Form To Your Streamlit App")
#         st.write(
#             """
#             Want to add a contact form to your Streamlit website?
#             In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service ‘Form Submit’.
#             """
#         )
#         st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")

# ---- KONTAKT-FORMULAR ----
with st.container():
    st.write("---")
    st.header("Kontaktiere uns!")
    st.write("Wenn du Fragen, Anregungen oder Anfragen für Konzerte hast, gib' uns gerne Bescheid. Wir melden uns bei dir!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/laurent_kurzschenkel@hotmail.de" method="POST">
        <input type="hidden" name="_captcha" value="true">
        <input type="text" name="name" placeholder="Name" required>
        <input type="email" name="email" placeholder="E-Mail-Adresse" required>
        <textarea name="message" placeholder="Deine Nachricht" required></textarea>
        <button type="submit">Senden</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()