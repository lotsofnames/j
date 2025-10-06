# Indukčné snímače
import re
import sys

import streamlit
from funkcion.word import file
import os
from pathlib import Path

st = streamlit


# st.link_button("Indukčné snímače","https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1")
def main(base, path,download=None,downloadName=None):
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
        else:
            st.write(slovo)
    if download!=None:
        if downloadName!=None:
            with open(download, "rb") as f:
                st.download_button(
                    label="Download",
                    data=f,
                    file_name=f"{downloadName}.docx",
                    icon=":material/download:",
                )
        else:
            sys.exit("no file name(downloadName)")