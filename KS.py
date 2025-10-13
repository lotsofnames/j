import os
import funkcion.slovo


def KS():
    base = os.path.dirname(__file__)
    base = os.path.join(base, "KS")
    # print(base)

    paths = os.path.join(base, "KS.txt")
    # print(paths)
    name = "Kapacitné snímače"
    downlode = os.path.join(base, "KS.docx")
    funkcion.slovo.main(base, paths, downlode, name)


KS()
