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
selected = option_menu(
    menu_title=None,
    options=["Start", "Konzerte", "Texte"],
    icons=["house", "volume-up", "book"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    )

# ---- INTRO ----
if selected == "Start":
    with st.container():
        st.write("---")
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

# ---- KONZERTE ---- 
if selected == "Konzerte":
    rain(
        emoji="🍻",
        font_size=54,
        falling_speed=5,
        animation_length="infinite",
    )
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with right_column:
            st_lottie(lottie_rock, height=600, key="rock")
            # Hier könnten auch Bilder, Videos oder der Canvas sein. 
        with left_column:
            st.header("Konzerte")
            st.subheader("2024:")
            st.write("18.05. // Sonnenkeller Balingen // The Snouts und Der Ganze Rest")
            st.write("05.04. // Schlosskeller Emmendingen // Wagner Brutal")
            st.write("23.03. // Laut für Vielfalt! im SAK Lörrach // Skabooom")
            st.write("09.03. // Schlosskeller Emmendingen // Nevermind")
            st.write(" ")
            st.subheader("2023:")
            st.write("15.12. // Crash Freiburg // ")
            st.write("09.08. // Café Atlantik Freiburg // Maid of Ace")
            st.write("22.04. // Battle to Exist in der Alten VHS Bonn // Die Manfreds")
            st.write(" ")
            st.subheader("2022:")
            st.write("19.11. // Schlosskeller Emmendingen // The Snouts & Skaboom")
            st.write("05.11. // DISTROY Festival in der KTS Freiburg // ")
            st.write("21.10. // Rockcafé Altdorf // KID-O")
            st.write("24.09. // Eimer Freiburg // Area South")
            st.write("08.07. // Reboot Festival im Eschholzpark Freiburg // ")
            st.write("26.06. // Freiburg stimmt ein im Artik Freiburg // ")
            st.write("18.06. // Cool Club Kinderweide in Königsfeld // Skabooom")
            st.write("14.05. // Album-Release-Party im JuZe Emmendingen // Skabooom")
            st.write(" ")
            st.subheader("2021:")
            st.write("16.10. // JuZe Denzlingen // Skabooom & Zirka")
            st.write("04.07. // Freiburg stimmt ein im Artik Freiburg // ")
            st.write(" ")
            st.subheader("2020:")
            st.write("09.05. // Corona-Livestream aus dem JuZe Emmendingen // ")
            st.write(" ")
            st.subheader("2019:")
            st.write("23.06. // KTS Freiburg // Heavy Kind & Vain")
            st.write("06.04. // Hinterhaus Emmendingen // ")        
            st.write("Irgendwann mal // White Rabbit Freiburg // ")
            st.write(" ")
            st.subheader("2018:")
            st.write("29.09. // Jugendzentrum Stühlinger // The Privateers")
            st.write("15.08. // White Rabbit Freiburg // ")
            st.write(" ")

# --- LYRICS ---
if selected == "Texte":
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Bierbike über die Alpen")
        st.write("Die Ellenbogen auf dem Tisch, die Hände fest am Glas.")
        st.write("Doch dieser Tisch, der hat vier Räder. Die Alkocops, sie geben Gas.")
        st.write("Das Dolce Vita soll es sein, man tritt in die Pedale,")
        st.write("Gen Italien lenkt man ein, es sprudelt aus der Zapfanlage.")
        st.write(" ")
        st.write("Mit dem Bierbike über die Alpen ")
        st.write("Rotzevoll nach Rimini")
        st.write("Mit dem Bierbike über die Alpen ")
        st.write("Rotzevoll nach Rimini")
        st.write("")
        st.write("Die Alkocops sind vollgetankt, und das auch ziemlich exzessiv.")
        st.write("Wie einst der große Hannibal bezwingen sie das Felsmassiv.")
        st.write("Seit dem ersten Kilometer träumen sie von Sangria,")
        st.write("Eimerweise einverleiben, ist doch sonnenklar.")
        st.write("")
        st.write("Mit dem Bierbike über die Alpen ")
        st.write("Rotzevoll nach Rimini")
        st.write("Mit dem Bierbike über die Alpen ")
        st.write("Rotzevoll nach Rimini")
        st.write("")
        st.write("Die Jungs sind motiviert und freuen sich auf das Meer,")
        st.write("Doch nach einem Kilometer ist ihr Tank schon wieder leer.")
        st.write("Die Waden schmerzen füchterlich, der Durst nicht aushaltbar.")
        st.write("Da erscheint ihnen Jesus und macht den Jungs was klar:")
        st.write("")
        st.write("Jesus: „Jungs, um euch zu besaufen müsst ihr nicht bis nach Rimini fahren.")
        st.write("Gutes Bier und Sangria gibt es an jeder Tankstelle.")
        st.write("Oder im Penny. Auf der Reeperbahn auch sonntags.“")
        st.write("")
        st.write("Mit dem Bierbike bis zur Tanke")
        st.write("Rotzevoll und Dosenbier")
        st.write("Mit dem Bierbike bis zur Tanke")
        st.write("Rotzevoll und Dosenbier")
        st.write("")
        st.write("")
        st.write("")
        st.subheader("Mit der Fußmaschine zur Tanke")
        st.write("Diesen Sommer gibt es die Empfehlung")
        st.write("Zu Urlaub in der heimischen Region,")
        st.write("Das ist für mich von Vorteil,")
        st.write("Denn die wichtigsten Urlaubsziele kenne ich schon:")
        st.write("Shell natürlich und Tankhof Grün")
        st.write("Und auf jeden Fall insbesondere Aral.")
        st.write("Sie verkaufen das Wasser des Urlaubs")
        st.write("Zur Befüllung vom knochentrockenen Kanal")
        st.write("")
        st.write("Mit der Fußmaschine zur Tanke, ")
        st.write("Dosenbier kaufen der Gedanke.")
        st.write("Gib' die Kaltschale jetzt endlich her,")
        st.write("Es dürstet mich - sehr!")
        st.write("Mit der Fußmaschine zur Tanke,")
        st.write("Billiges Dosenbier. Bitteschön, Danke. ")
        st.write("Komm mal her jetzt, ich hab' Kaltschalen bestellt,")
        st.write("Und nimm dafür mein rotes Kleingeld.")
        st.write("")
        st.write("An der Tanke kauf' ich sicher kein Craftbier")
        st.write("Und auch keinen Fall Club Mate,")
        st.write("Wenn der Tankwart mir das anbietet,")
        st.write("Würde ich ihn verprügeln!")
        st.write("Das ist a) nämlich viel zu teuer ")
        st.write("Und b) schmeckt's nach grindigem Kanal,")
        st.write("Im Gegensatz dazu überzeugt")
        st.write("Dosenbier im Geschmack total.")
        st.write("")
        st.write("")
        st.write("")
        st.subheader("FIFA")
        st.write("Zusammen chillt ihr in der Villa von eurem Oberlauch, ")
        st.write("Pinselt euch dabei gegenseitig den Bauch.")
        st.write("Durch die toten Hallen dringt ein fieses Lachen,")
        st.write("Thema der Sitzung heute: Wie kann man Fussball beschissen machen?")
        st.write("")
        st.write("UEFA, FIFA, was habt ihr geraucht?")
        st.write("Eure Symphatiepunkte habt ihr damit aufgebraucht!")
        st.write("Schiebung bei WM-Vergabe ist mir scheißegal,")
        st.write("Doch kein Bier im Stadion, das ist ein Skandal!")
        st.write("")
        st.write("Früher Profifussballspieler, jetzt ein Profihurensohn,")
        st.write("Ohne Fans kein Fussball. Undank ist der Weltenlohn")
        st.write("Auf der VIP-Tribüne zieht Waldi sich drei Weizen rein,")
        st.write("Wahre Fans verdursten, doch das interessiert keinen!")
        st.write("")
        st.write("UEFA, FIFA, was habt ihr geraucht?")
        st.write("Eure Symphatiepunkte habt ihr damit aufgebraucht!")
        st.write("Schiebung bei WM-Vergabe ist mir scheißegal,")
        st.write("Doch kein Bier im Stadion, das ist ein Skandal!")
        st.write("")
        st.write("")
        st.write("")

