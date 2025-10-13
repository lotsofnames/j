import os
import funkcion.slovo


def SUV():
    base = os.path.dirname(__file__)
    base = os.path.join(base, "SUV")
    # print(base)

    paths = os.path.join(base, "SUV.txt")
    # print(paths)
    name = "Senzor úniku vody"
    downlode = os.path.join(base, "SUV.docx")
    funkcion.slovo.main(base, paths, downlode, name)


SUV()
