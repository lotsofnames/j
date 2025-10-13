import os
import funkcion.slovo


def SN():
    base = os.path.dirname(__file__)
    base = os.path.join(base, "SN")
    # print(base)

    paths = os.path.join(base, "SN.txt")
    # print(paths)

    name = "Snímač nárazu"
    downlode = os.path.join(base, "SN.docx")
    funkcion.slovo.main(base, paths, downlode, name)


SN()
