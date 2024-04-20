import requests
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain
from PIL import Image


# --- Konfiguration ---
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

html_code = '''
<iframe style="border-radius:0px" src="https://open.spotify.com/embed/artist/6UolTF33q9gCE3kDK6tuTU?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
'''

# --- MENÜ ---
# selected = option_menu(
#     menu_title=None,
#     options=["Start", "Konzerte", "Texte"],
#     icons=["house", "volume-up", "book"],
#     menu_icon="cast",
#     default_index=0,
#     orientation="horizontal",
#     )

# # ---- INTRO ----
st.title("Die Alkocops 🍻👮‍♂️")
with st.container():
    text_column, image_column = st.columns(2)
    with text_column:
        st.subheader("¿Qué pasa cabrones?")
        st.title("Wir sind die Alkocops! 🍻")
        st.write("Ob Wohnungsmarkt, Clubsterben oder Craftbier: Die Alkocops haben etwas dagegen. Laut ChatGPT sind ihre Lieder wohl eine ''sozialkritische Faust ins Gesicht'', aber bescheiden wie sie sind, konzentrieren sie sich lieber auf das Wesentliche: Dosenbier verhaften!")
        st.write(" ")
        st.write("Die Alkocops sind Florian Silberblick, Huckleberry Gin, Marius Müller-Thurgau, Dr. Don Promillo und Toni Pilsetti.")
        st.write(" ")
        st.write("[ 📸 Instagram >](https://www.instagram.com/alkocops/?hl=de)")
        st.write("[ 🎵 Spotify >](https://open.spotify.com/intl-de/artist/6UolTF33q9gCE3kDK6tuTU?si=up3DRDMuQs6PF3vsJ1ZHhQ)")
        st.write("[ 🏕 Bandcamp >](https://diealkocops.bandcamp.com/)")
        st.write("[ 🎥 YouTube >](https://www.youtube.com/@diealkocops6613)")
        st.write(" ")
    with image_column:
        st.image(img_band2)

    # ---- SPOTIFY ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Flüssiges Gold")
        st.write("Goldfarben, naturtrüb und mit vollmundigem Geschmack ist das Album ''Flüssiges Gold'' der Alkocops eine ehrliche Erfrischung. Ein wahrhaft gutes Album kann nur entstehen, wenn man von allem nur das Beste nimmt. Kompromisslos.")
        st.write("Weil uns das Wohl anspruchsvoller Kenner am Herzen liegt. Und weil ''Flüssiges Gold'' immer das bleiben soll, was es akzeptiertermaßen ist: Eines der süffigsten Alben unserer Zeit.")
        st.write(" ")
    with right_column:
        st.write(html_code, unsafe_allow_html=True)

