import streamlit
import os
from MS import MS
from KS import KS
from IS import IS
from OS import OS
from PIR import PIR
from SN import SN
from SP import SP
from US import US
from ZS import ZS
from SUV import SUV
from NTC import NTC

st = streamlit
base = os.path.dirname(__file__)
base = os.path.join(base, "QR","adres2.txt")
st.title("Obsah")
img_of = [
    "Indukčné snímače",
    "Kapacitné snímače",
    "Magnetické snímače",
    "Optické snímače",
    "PIR Snímače",
    "Senzor úniku vody",
    "Snímač nárazu",
    "Snímač teploty NTC",
    "Snímače plameňa",
    "Ultrazvukové snímače",
    "Zvukové snímače",
]
i=0
with open(base, "r") as f:
    for line in f:
        line = line.strip().replace("\n", "")
        st.link_button(
            img_of[i],
            line,
        )
        i=i+1



IS()
MS()
KS()
SUV()
KS()
OS()
PIR()
SN()
SP()
US()
ZS()
NTC()