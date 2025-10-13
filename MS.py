import os
import funkcion.slovo


def MS():
    base = os.path.dirname(__file__)
    base = os.path.join(base, "MS")
    # print(base)

    paths = os.path.join(base, "MS.txt")
    # print(paths)

    name = "Magnetické snímače"
    downlode = os.path.join(base, "MS.docx")
    funkcion.slovo.main(base, paths, downlode, name)


MS()
