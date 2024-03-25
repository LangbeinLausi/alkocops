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
lottie_vinyl = load_lottieurl("https://lottie.host/6592ef39-bb59-47c6-8561-ffc732191a9e/bxry2ZUP2n.json")

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
        st.write(" ")
        st.write(" ")
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
        st.write("18.05. // Sonnenkeller Balingen // The Snouts und Der Ganze Rest")
        st.write("05.04. // Schlosskeller Emmendingen // Wagner Brutal")
        st.write("23.03. // Laut für Vielfalt! im SAK Lörrach // Skabooom")
        st.write("09.03. // Schlosskeller Emmendingen // Nevermind")
        st.subheader("2023:")
        st.write("15.12. // Crash Freiburg // ")
        st.write("09.08. // Café Atlantik Freiburg // Maid of Ace")
        st.write("22.04. // Battle to Exist in der Alten VHS Bonn // Die Manfreds")
        st.write("15.12. // Crash Freiburg // ")
        st.subheader("2022:")
        st.write("19.11. // Schlosskeller Emmendingen // The Snouts & Skaboom")
        st.write("05.11. // DISTROY Festival in der KTS Freiburg // ")
        st.write("21.10. // Rockcafé Altdorf // KID-O")
        st.write("24.09. // Eimer Freiburg // Area South")
        st.write("08.07. // Reboot Festival im Eschholzpark Freiburg // ")
        st.write("26.06. // Freiburg stimmt ein im Artik Freiburg // ")
        st.write("18.06. // Cool Club Kinderweide in Königsfeld // Skabooom")
        st.write("14.05. // Album-Release-Party im JuZe Emmendingen // Skabooom")
        st.subheader("2021:")
        st.write("16.10. // JuZe Denzlingen // Skabooom & Zirka")
        st.write("04.07. // Freiburg stimm ein im Artik Freiburg // ")
        st.subheader("2020:")
        st.write("09.05. // Corona-Livestream aus dem JuZe Emmendingen // ")
        st.subheader("2019:")
        st.write("23.06. // KTS Freiburg // Heavy Kind & Vain")
        st.write("06.04. // Hinterhaus Emmendingen // Heavy Kind & Vain")
    with left_column:
        st_lottie(lottie_rock, height=300, key="rock")
        st_lottie(lottie_bier, height=300, key="beer")
        st_lottie(lottie_vinyl, height=300, key="vinyl")

# # ---- KONTAKT-FORMULAR ----
# with st.container():
#     st.write("---")
#     st.header("Kontaktiere uns!")
#     st.write("Wenn du Fragen, Anregungen oder Anfragen für Konzerte hast, gib' uns gerne Bescheid. Wir melden uns bei dir!")
#     st.write("##")

#     # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
#     contact_form = """
#     <form action="https://formsubmit.co/laurent_kurzschenkel@hotmail.de" method="POST">
#         <input type="hidden" name="_captcha" value="true">
#         <input type="text" name="name" placeholder="Name" required>
#         <input type="email" name="email" placeholder="E-Mail-Adresse" required>
#         <textarea name="message" placeholder="Deine Nachricht" required></textarea>
#         <button type="submit">Senden</button>
#     </form>
#     """
#     left_column, right_column = st.columns(2)
#     with left_column:
#         st.markdown(contact_form, unsafe_allow_html=True)
#     with right_column:
#         st.empty()