#Indukčné snímače
import streamlit
st=streamlit
#st.link_button("Indukčné snímače","https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1")
def file(z):
    slova=[]
    with open(z,"r",encoding="utf-8") as fill:
        fill = fill.readlines()
        for line in fill:
            if line.replace(" ", "") != ""and line.replace(" ", "") != "\n":
                slova.append(line.replace("\n",""))
    return slova
slova=file("IS.txt")
for slovo in slova:
    if slovo.startswith("#"):
        st.subheader(slovo.replace("#", ""))
    elif slovo.startswith("/"):
        st.image(f"{slovo.replace("/","").strip()}.png")
    else:
        st.write(slovo)