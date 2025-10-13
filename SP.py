import os
import funkcion.slovo


def SP():
    base = os.path.dirname(__file__)
    base = os.path.join(base, "SP")
    # print(base)

    paths = os.path.join(base, "SP.txt")
    # print(paths)

    name = "Snímače plameňa"
    downlode = os.path.join(base, "SP.docx")
    funkcion.slovo.main(base, paths, downlode, name)


SP()
