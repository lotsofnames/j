import os
import funkcion.slovo


def OS():
    base = os.path.dirname(__file__)
    base = os.path.join(base, "OS")
    # print(base)

    paths = os.path.join(base, "OS.txt")
    # print(paths)
    name = "Optické snímače"
    downlode = os.path.join(base, "OS.docx")
    funkcion.slovo.main(base, paths, downlode, name)


OS()
