import time

import streamlit as st


LANGUAGES = {
    "English": "en",
    "Čeština": "cs",
    "Українська": "uk",
}

TEXT = {
    "en": {
        "title": "Deutsch with Krishna",
        "subtitle": "Learn German numbers, greetings, colors, and days of the week.",
        "language": "Learning language",
        "topic": "Choose a topic",
        "topics": {
            "numbers": "Numbers",
            "greetings": "Greetings",
            "colors": "Colors",
            "days": "Days of the week",
        },
        "choose": "Choose an item to learn:",
        "number_prompt": "Enter a number from 0 to 199",
        "learn_number": "Learn this number",
        "number_rule": "For numbers from 21 to 99, say the units first, then **und** (and), then the tens. For example, 21 is **einundzwanzig**.",
        "hundreds_rule": "Numbers from 101 to 199 start with **einhundert**, followed by the remaining number. For example, 151 is **einhunderteinundfünfzig**.",
        "greeting_descriptions": [
            "A general greeting that can be used at any time of day.",
            "Used during the day.",
            "A formal way to say goodbye to someone you do not know well.",
            "An informal way to say goodbye to a friend.",
            "Used in the morning.",
            "Used in the evening.",
            "Used when going to bed.",
            "A traditional greeting used in some regions.",
        ],
        "color_descriptions": [
            "This is the color red.",
            "This is the color blue.",
            "This is the color green.",
            "This is the color yellow.",
            "This is the color black.",
            "This is the color white.",
            "This is the color orange.",
            "This is the color purple.",
        ],
        "day_descriptions": [
            "This is Monday.",
            "This is Tuesday.",
            "This is Wednesday.",
            "This is Thursday.",
            "This is Friday.",
            "This is Saturday.",
            "This is Sunday.",
        ],
    },
    "cs": {
        "title": "Němčina s Krišnou",
        "subtitle": "Uč se německá čísla, pozdravy, barvy a dny v týdnu.",
        "language": "Jazyk výuky",
        "topic": "Vyber si téma",
        "topics": {
            "numbers": "Čísla",
            "greetings": "Pozdravy",
            "colors": "Barvy",
            "days": "Dny v týdnu",
        },
        "choose": "Vyber si, co se chceš naučit:",
        "number_prompt": "Zadej číslo od 0 do 199",
        "learn_number": "Naučit se číslo",
        "number_rule": "Čísla od 21 do 99 se tvoří tak, že se nejprve řekne jednotka, potom **und** (a) a nakonec desítka. Například 21 je **einundzwanzig**.",
        "hundreds_rule": "Čísla od 101 do 199 začínají slovem **einhundert**, po kterém následuje zbytek čísla. Například 151 je **einhunderteinundfünfzig**.",
        "greeting_descriptions": [
            "Obecný pozdrav, který můžeš použít kdykoli během dne.",
            "Používá se během dne.",
            "Formální rozloučení s někým, koho dobře neznáš.",
            "Neformální rozloučení s kamarádem.",
            "Používá se ráno.",
            "Používá se večer.",
            "Používá se před spaním.",
            "Tradiční pozdrav používaný v některých regionech.",
        ],
        "color_descriptions": [
            "Tohle je červená barva.",
            "Tohle je modrá barva.",
            "Tohle je zelená barva.",
            "Tohle je žlutá barva.",
            "Tohle je černá barva.",
            "Tohle je bílá barva.",
            "Tohle je oranžová barva.",
            "Tohle je fialová barva.",
        ],
        "day_descriptions": [
            "Tohle je pondělí.",
            "Tohle je úterý.",
            "Tohle je středa.",
            "Tohle je čtvrtek.",
            "Tohle je pátek.",
            "Tohle je sobota.",
            "Tohle je neděle.",
        ],
    },
    "uk": {
        "title": "Німецька з Крішною",
        "subtitle": "Вивчай німецькі числа, привітання, кольори та дні тижня.",
        "language": "Мова навчання",
        "topic": "Обери тему",
        "topics": {
            "numbers": "Числа",
            "greetings": "Привітання",
            "colors": "Кольори",
            "days": "Дні тижня",
        },
        "choose": "Обери, що хочеш вивчити:",
        "number_prompt": "Введи число від 0 до 199",
        "learn_number": "Вивчити число",
        "number_rule": "Числа від 21 до 99 утворюються так: спочатку одиниці, потім **und** (і), а потім десятки. Наприклад, 21 — **einundzwanzig**.",
        "hundreds_rule": "Числа від 101 до 199 починаються зі слова **einhundert**, за яким іде решта числа. Наприклад, 151 — **einhunderteinundfünfzig**.",
        "greeting_descriptions": [
            "Загальне привітання, яке можна використовувати будь-коли протягом дня.",
            "Використовується вдень.",
            "Формальне прощання з людиною, яку ти мало знаєш.",
            "Неформальне прощання з другом.",
            "Використовується вранці.",
            "Використовується ввечері.",
            "Використовується перед сном.",
            "Традиційне привітання, яке використовують у деяких регіонах.",
        ],
        "color_descriptions": [
            "Це червоний колір.",
            "Це синій колір.",
            "Це зелений колір.",
            "Це жовтий колір.",
            "Це чорний колір.",
            "Це білий колір.",
            "Це помаранчевий колір.",
            "Це фіолетовий колір.",
        ],
        "day_descriptions": [
            "Це понеділок.",
            "Це вівторок.",
            "Це середа.",
            "Це четвер.",
            "Це п’ятниця.",
            "Це субота.",
            "Це неділя.",
        ],
    },
}

LESSONS = {
    "greetings": [
        "Hallo",
        "Guten Tag",
        "Auf Wiedersehen",
        "Tschüss",
        "Guten Morgen",
        "Guten Abend",
        "Gute Nacht",
        "Grüß Gott",
    ],
    "colors": ["Rot", "Blau", "Grün", "Gelb", "Schwarz", "Weiß", "Orange", "Lila"],
    "days": ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"],
}

UNITS = [
    "null",
    "eins",
    "zwei",
    "drei",
    "vier",
    "fünf",
    "sechs",
    "sieben",
    "acht",
    "neun",
    "zehn",
    "elf",
    "zwölf",
    "dreizehn",
    "vierzehn",
    "fünfzehn",
    "sechzehn",
    "siebzehn",
    "achtzehn",
    "neunzehn",
]
TENS = {
    2: "zwanzig",
    3: "dreißig",
    4: "vierzig",
    5: "fünfzig",
    6: "sechzig",
    7: "siebzig",
    8: "achtzig",
    9: "neunzig",
}


def german_number(number: int) -> str:
    """Return the German word for an integer from 0 through 199."""
    if number < 0 or number > 199:
        raise ValueError("number must be between 0 and 199")
    if number < 20:
        return UNITS[number]
    if number < 100:
        tens, units = divmod(number, 10)
        if units == 0:
            return TENS[tens]
        unit_word = "ein" if units == 1 else UNITS[units]
        return f"{unit_word}und{TENS[tens]}"
    if number == 100:
        return "hundert"
    return f"einhundert{german_number(number - 100)}"


st.set_page_config(page_title="Deutsch with Krishna", page_icon="🇩🇪")

theme_name = st.sidebar.radio(
    "Appearance / Vzhled / Вигляд",
    ("Light", "Dark"),
    horizontal=True,
)
theme = {
    "Light": {
        "mode": "light",
        "background": "#ffffff",
        "foreground": "#202124",
        "surface": "#f4f6f8",
        "border": "#d9dee5",
        "accent": "#4b6cb7",
        "accent_text": "#ffffff",
    },
    "Dark": {
        "mode": "dark",
        "background": "#0e1117",
        "foreground": "#fafafa",
        "surface": "#1c222b",
        "border": "#39414d",
        "accent": "#7796e8",
        "accent_text": "#10131a",
    },
}[theme_name]

st.markdown(
    f"""
    <style>
    :root {{ color-scheme: {theme["mode"]}; }}
    .stApp,
    [data-testid="stSidebar"] {{
        background-color: {theme["background"]};
        color: {theme["foreground"]};
    }}
    .stApp, .stApp p, .stApp label, .stApp h1, .stApp h2, .stApp h3,
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {{
        color: {theme["foreground"]};
    }}
    [data-testid="stHeader"] {{
        background-color: {theme["background"]};
    }}
    [data-testid="stSidebarCollapseButton"],
    [data-testid="stSidebarExpandButton"],
    [data-testid="stSidebar"] button[kind="header"] {{
        background-color: {theme["surface"]};
        color: {theme["foreground"]};
        border: 1px solid {theme["border"]};
    }}
    [data-testid="stSidebarCollapseButton"] svg,
    [data-testid="stSidebarExpandButton"] svg,
    [data-testid="stSidebar"] button[kind="header"] svg {{
        color: {theme["foreground"]};
        fill: currentColor;
    }}
    [data-baseweb="select"] > div,
    [data-testid="stNumberInput"] input,
    [data-testid="stTextInput"] input {{
        background-color: {theme["surface"]};
        color: {theme["foreground"]};
        border-color: {theme["border"]};
    }}
    .stButton button {{
        background-color: {theme["surface"]};
        color: {theme["foreground"]};
        border-color: {theme["border"]};
    }}
    .stButton button[kind="primary"] {{
        background-color: {theme["accent"]};
        color: {theme["accent_text"]};
        border-color: {theme["accent"]};
    }}
    [data-testid="stAlert"] {{
        background-color: {theme["surface"]};
        color: {theme["foreground"]};
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

if "startup_animation_shown" not in st.session_state:
    intro = st.empty()
    for title in (
        "Deutsch with Krishna",
        "Німецька з Крішною",
        "Němčina s Krišnou",
    ):
        intro.markdown(
            "<div style='position: fixed; inset: 0; z-index: 999999; "
            "display: flex; align-items: center; justify-content: center; "
            f"background: {theme['background']}; "
            f"color: {theme['foreground']};'>"
            f"<h1 style='text-align: center; margin: 0'>{title}</h1>"
            "</div>",
            unsafe_allow_html=True,
        )
        time.sleep(0.8)
    intro.empty()
    st.session_state["startup_animation_shown"] = True

language_name = st.sidebar.selectbox("Language / Jazyk / Мова", list(LANGUAGES))
language = LANGUAGES[language_name]
text = TEXT[language]

st.title(text["title"])
st.write(text["subtitle"])
st.sidebar.subheader(text["language"])
st.sidebar.caption(language_name)

topic_key = st.sidebar.radio(
    text["topic"],
    options=list(text["topics"]),
    format_func=lambda topic: text["topics"][topic],
)
st.header(text["topics"][topic_key])

if topic_key == "numbers":
    number = st.number_input(
        text["number_prompt"],
        min_value=0,
        max_value=199,
        step=1,
        key="number_input",
    )
    if st.button(text["learn_number"], type="primary", key="learn_number"):
        st.session_state["lesson"] = {
            "language": language,
            "topic": topic_key,
            "number": int(number),
        }

    lesson = st.session_state.get("lesson", {})
    if lesson.get("language") == language and lesson.get("topic") == topic_key:
        learned_number = lesson["number"]
        st.success(f"{learned_number} = **{german_number(learned_number)}**")
        if 20 < learned_number < 100:
            st.info(text["number_rule"])
        elif 100 < learned_number < 200:
            st.info(text["hundreds_rule"])
else:
    st.write(text["choose"])
    words = LESSONS[topic_key]
    columns = st.columns(2)
    for index, word in enumerate(words):
        if columns[index % len(columns)].button(
            f"{index + 1}. {word}",
            key=f"{topic_key}_{index}",
            use_container_width=True,
        ):
            st.session_state["lesson"] = {
                "language": language,
                "topic": topic_key,
                "index": index,
            }

    lesson = st.session_state.get("lesson", {})
    if lesson.get("language") == language and lesson.get("topic") == topic_key:
        selected_index = lesson["index"]
        description_key = {
            "greetings": "greeting_descriptions",
            "colors": "color_descriptions",
            "days": "day_descriptions",
        }[topic_key]
        st.success(words[selected_index])
        st.write(text[description_key][selected_index])