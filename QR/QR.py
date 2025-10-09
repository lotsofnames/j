import qrcode

web = [
    "https://lotsofnames-j-is-k3unmc.streamlit.app/#indukcne-snimace",
    "https://lotsofnames-j-ks-sem2e3.streamlit.app/#kapacitne-snimace",
    "https://lotsofnames-j-ms-yuipbp.streamlit.app/#magneticke-snimace",
    "https://lotsofnames-j-os-kihfbl.streamlit.app/#opticke-snimace",
    "https://lotsofnames-j-pir-xcsgla.streamlit.app/#pir-snimace",
    "https://zq73gtflpyeysronrzwzhs.streamlit.app/#senzor-uniku-vody",
    "https://lotsofnames-j-sn-lyfriu.streamlit.app/#snimac-narazu",
    "https://lotsofnames-j-ntc-mljdaj.streamlit.app/#snimac-teploty-ntc",
    "https://lotsofnames-j-sp-efgppi.streamlit.app/#snimace-plamena",
    "https://lotsofnames-j-us-ogirnx.streamlit.app/#ultrazvukove-snimace",
    "https://lotsofnames-j-zs-tsjazt.streamlit.app/#zvukove-snimace",
]
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
for i in range(len(web)):
    img = qrcode.make(web[i])
    type(img)  # qrcode.image.pil.PilImage
    img.save(img_of[i] + ".png")
