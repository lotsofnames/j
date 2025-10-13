import qrcode

web = []
with open("adres.txt", "r") as f:
    for line in f:
        line = line.strip().replace("\n", "")
        web.append(line)

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
