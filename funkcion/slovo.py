# Indukčné snímače
import re
import sys
import pandas as pd
import streamlit
from funkcion.word import file
import os
import uuid
from pathlib import Path

st = streamlit


# st.link_button("Indukčné snímače","https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1")
def main(base, path, download=None, downloadName=None):
    slova = file(path)
    for slovo in slova:
        if slovo.startswith("#"):
            st.subheader(slovo.replace("#", ""))
        elif slovo.startswith("/"):
            image_path = os.path.join(base, f"{slovo.replace('/', '').strip()}.png")
            st.image(image_path)
        elif '"' in slovo:
            i = re.search(r'"(.+);(.+)"', slovo)
            if i:
                st.page_link(i.group(2), label=i.group(1))
                sub = slovo.replace(i.group(0), "")
                st.write(sub)
        elif "%Porovnanie PIR  a HF senzorov" in slovo:
            confusion_matrix = pd.DataFrame(
                {
                    "PIR Senzory": [
                        "Výhody",
                        "Nereaguje na pohyb za dverami alebo stenami",
                        "Viditeľný na svietidle, ľahko rozpoznateľný",
                        "Nižšia obstarávacia cena",
                        "Nízka spotreba (<0,1 W)",
                        "HF Senzory",
                        "Výhody",
                        "Skrytý pod sklom alebo krytom svietidla",
                        "Vysoká, reaguje na minimálne pohyby",
                        "Účinné aj v zimnom období",
                    ],
                    " ": [
                        "Nevýhody",
                        "Slabá citlivosť v zime",
                        "Viditeľný senzor môže ovplyvniť estetiku",
                        " ",
                        " ",
                        " ",
                        "Nevýhody",
                        "Reaguje na pohyb za dverami, sklom alebo inými ľahkými materiálmi",
                        "Vyššia cena",
                        "Vyššia spotreba (0,3 – 0,5 W)",
                    ],
                },
                index=None,
            )
            st.table(confusion_matrix)
        else:
            st.write(slovo)
    if download != None:
        if downloadName != None:
            with open(download, "rb") as f:
                st.download_button(
                    label="Download",
                    # v pripade  problemov zmen  f.read na  f alebo opacne
                    data=f,
                    file_name=f"{downloadName}.docx",
                    icon=":material/download:",
                    key=f"{downloadName}_{uuid.uuid4()}",
                )
        else:
            sys.exit("no file name(downloadName)")
