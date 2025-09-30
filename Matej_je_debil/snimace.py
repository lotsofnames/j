#Indukčné snímače
from word import file
import streamlit
st=streamlit
#st.link_button("Indukčné snímače","https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1")

slova=file("IS.txt")
for slovo in slova:
    if slovo.startswith("#"):
        st.subheader(slovo.replace("#", ""))
    elif slovo.startswith("/"):
        st.image(f"{slovo.replace("/","").strip()}.png")
    else:
        st.write(slovo)