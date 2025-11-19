import streamlit as st
import os
from streamlit import title
port = int(os.environ.get("PORT", 8501))  # 8501 je default u Streamlit, ale Azure môže dať inú hodnotu
pg = st.navigation(
    {
        "obsah": [
            st.Page("IS.py", title="Indukčné snímače"),
            st.Page("KS.py", title="Kapacitné snímače"),
            st.Page("MS.py", title="Magnetické snímače"),
            st.Page("NTC.py", title="Snímač teploty NTC"),
            st.Page("OS.py", title="Optické snímače"),
            st.Page("PIR.py", title="Snímač PIR"),
            st.Page("SN.py", title="Snímač nárazu"),
            st.Page("SP.py", title="Snímače plameňa"),
            st.Page("SUV.py", title="Senzor úniku vody"),
            st.Page("US.py", title="Ultrazvukové snímače"),
            st.Page("ZS.py", title="Zvukové snímače"),
        ]
    }
)
pg.run()
