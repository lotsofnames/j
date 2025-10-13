import os
import funkcion.slovo


def PIR():
    base = os.path.dirname(__file__)
    base = os.path.join(base, "PIR")
    # print(base)

    paths = os.path.join(base, "PIR.txt")
    # print(paths)

    name = "PIR Snímače"
    downlode = os.path.join(base, "PIR.docx")
    funkcion.slovo.main(base, paths, downlode, name)


PIR()
