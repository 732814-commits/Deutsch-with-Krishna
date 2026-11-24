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
        "subtitle": "Learn German numbers, greetings, colors, days of the week, W-questions, and verb forms.",
        "language": "Learning language",
        "topic": "Choose a topic",
        "topics": {
            "numbers": "Numbers",
            "greetings": "Greetings",
            "colors": "Colors",
            "days": "Days of the week",
            "questions": "W-questions",
            "verbs": "Verb forms",
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
        "question_descriptions": [
            "Where? (location)",
            "What?",
            "Who?",
            "Where from?",
            "Which? (masculine, feminine, or neuter form)",
            "How?",
            "Why?",
            "When?",
        ],
        "question_map_prompt": "First decide what you want to ask about:",
        "common_questions_title": "Common questions",
        "common_questions_intro": "Notice how the verb ending changes with the person:",
        "du_questions": "Talking to **you** (du)",
        "er_sie_questions": "Talking about **him or her** (er / sie)",
        "verb_example": "Regular verb example",
        "verb_forms_intro": "The infinitive **wohnen** means “to live.” Remove **-en**, then add the ending for each person:",
        "verb_persons": ["I", "you (singular)", "he / she / it", "we", "you (plural)", "they / you (formal)"],
        "verb_table_headers": ["Pronoun", "Meaning", "Verb form"],
        "question_group_labels": {
            "person": "A person",
            "thing": "A thing",
            "place": "A place",
            "time": "Time",
            "manner": "The way something happens",
            "reason": "A reason",
            "choice": "A choice",
        },
    },
    "cs": {
        "title": "Němčina s Krišnou",
        "subtitle": "Uč se německá čísla, pozdravy, barvy, dny v týdnu, otázky s W a časování sloves.",
        "language": "Jazyk výuky",
        "topic": "Vyber si téma",
        "topics": {
            "numbers": "Čísla",
            "greetings": "Pozdravy",
            "colors": "Barvy",
            "days": "Dny v týdnu",
            "questions": "Otázky s W",
            "verbs": "Časování sloves",
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
        "question_descriptions": [
            "Kde? (místo)",
            "Co?",
            "Kdo?",
            "Odkud?",
            "Který? Která? Které?",
            "Jak?",
            "Proč?",
            "Kdy?",
        ],
        "question_map_prompt": "Nejprve si vyber, na co se chceš zeptat:",
        "common_questions_title": "Běžné otázky",
        "common_questions_intro": "Všimni si, jak se mění koncovka slovesa podle osoby:",
        "du_questions": "Otázky na **tebe** (du)",
        "er_sie_questions": "Otázky o **něm nebo o ní** (er / sie)",
        "verb_example": "Příklad pravidelného slovesa",
        "verb_forms_intro": "Infinitiv **wohnen** znamená „bydlet“. Odstraň **-en** a přidej koncovku podle osoby:",
        "verb_persons": ["já", "ty (jednotné číslo)", "on / ona / ono", "my", "vy (množné číslo)", "oni / ony / Vy (vykání)"],
        "verb_table_headers": ["Zájmeno", "Význam", "Tvar slovesa"],
        "question_group_labels": {
            "person": "Osoba",
            "thing": "Věc",
            "place": "Místo",
            "time": "Čas",
            "manner": "Způsob",
            "reason": "Důvod",
            "choice": "Výběr",
        },
    },
    "uk": {
        "title": "Німецька з Крішною",
        "subtitle": "Вивчай німецькі числа, привітання, кольори, дні тижня, W-питання та дієвідмінювання.",
        "language": "Мова навчання",
        "topic": "Обери тему",
        "topics": {
            "numbers": "Числа",
            "greetings": "Привітання",
            "colors": "Кольори",
            "days": "Дні тижня",
            "questions": "W-питання",
            "verbs": "Форми дієслів",
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
        "question_descriptions": [
            "Де? (місце)",
            "Що?",
            "Хто?",
            "Звідки?",
            "Який? Яка? Яке?",
            "Як?",
            "Чому?",
            "Коли?",
        ],
        "question_map_prompt": "Спочатку обери, про що хочеш запитати:",
        "common_questions_title": "Поширені запитання",
        "common_questions_intro": "Зверни увагу, як змінюється закінчення дієслова залежно від особи:",
        "du_questions": "Запитання до **тебе** (du)",
        "er_sie_questions": "Запитання про **нього або неї** (er / sie)",
        "verb_example": "Приклад правильного дієслова",
        "verb_forms_intro": "Інфінітив **wohnen** означає «жити». Відкинь **-en** і додай закінчення для кожної особи:",
        "verb_persons": ["я", "ти (однина)", "він / вона / воно", "ми", "ви (множина)", "вони / Ви (ввічливо)"],
        "verb_table_headers": ["Займенник", "Значення", "Форма дієслова"],
        "question_group_labels": {
            "person": "Людина",
            "thing": "Річ",
            "place": "Місце",
            "time": "Час",
            "manner": "Спосіб дії",
            "reason": "Причина",
            "choice": "Вибір",
        },
    },
}
VERB_FORMS = [
    ("ich", "wohne"),
    ("du", "wohnst"),
    ("er / sie / es", "wohnt"),
    ("wir", "wohnen"),
    ("ihr", "wohnt"),
    ("sie / Sie", "wohnen"),
]

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
    "questions": [
        "Wo",
        "Was",
        "Wer",
        "Woher",
        "Welcher / Welche / Welches",
        "Wie",
        "Warum",
        "Wann",
    ],
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
QUESTION_GROUPS = {
    "person": [2],
    "thing": [1],
    "place": [0, 3],
    "time": [7],
    "manner": [5],
    "reason": [6],
    "choice": [4],
}
COMMON_QUESTIONS = {
    "du": [
        ("Wie heißt du?", "What's your name?", "Jak se jmenuješ?", "Як тебе звати?"),
        ("Wo wohnst du?", "Where do you live?", "Kde bydlíš?", "Де ти живеш?"),
        ("Woher kommst du?", "Where are you from?", "Odkud pocházíš?", "Звідки ти?"),
        ("Wie alt bist du?", "How old are you?", "Kolik ti je let?", "Скільки тобі років?"),
        ("Was machst du gern?", "What do you like doing?", "Co rád/a děláš?", "Що ти любиш робити?"),
        ("Welche Musik hörst du gern?", "What music do you like listening to?", "Jakou hudbu rád/a posloucháš?", "Яку музику ти любиш слухати?"),
    ],
    "er_sie": [
        ("Wie heißt er?", "What's his name?", "Jak se jmenuje?", "Як його звати?"),
        ("Wo wohnt sie?", "Where does she live?", "Kde bydlí?", "Де вона живе?"),
        ("Was macht er gern?", "What does he like doing?", "Co rád dělá?", "Що він любить робити?"),
    ],
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
elif topic_key == "questions":
    st.write(text["question_map_prompt"])
    columns = st.columns(2)
    for group_index, (group, question_indexes) in enumerate(QUESTION_GROUPS.items()):
        with columns[group_index % len(columns)].container(border=True):
            st.subheader(text["question_group_labels"][group])
            for question_index in question_indexes:
                st.markdown(
                    f"**{text['question_descriptions'][question_index]}**  \n"
                    f"↓  \n"
                    f"**{LESSONS['questions'][question_index]}**"
                )
    st.subheader(text["common_questions_title"])
    st.write(text["common_questions_intro"])
    columns = st.columns(2)
    for column, group, label in (
        (columns[0], "du", text["du_questions"]),
        (columns[1], "er_sie", text["er_sie_questions"]),
    ):
        with column.container(border=True):
            st.markdown(label)
            for german, english, czech, ukrainian in COMMON_QUESTIONS[group]:
                translation = {"en": english, "cs": czech, "uk": ukrainian}[language]
                st.markdown(f"**{german}**  \n{translation}")
elif topic_key == "verbs":
    st.subheader(text["verb_example"])
    st.write(text["verb_forms_intro"])
    st.markdown("### wohnen")
    st.table(
        {
            text["verb_table_headers"][0]: [form[0] for form in VERB_FORMS],
            text["verb_table_headers"][1]: text["verb_persons"],
            text["verb_table_headers"][2]: [form[1] for form in VERB_FORMS],
        }
    )
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