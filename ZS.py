import os
import funkcion.slovo


def ZS():
    base = os.path.dirname(__file__)
    base = os.path.join(base, "ZS")
    # print(base)

    paths = os.path.join(base, "ZS.txt")
    # print(paths)

    name = "Zvukové snímače"
    downlode = os.path.join(base, "ZS.docx")
    funkcion.slovo.main(base, paths, downlode, name)


ZS()
