import os
import funkcion.slovo


def SUV():
    base = os.path.dirname(__file__)
    base = os.path.join(base, "SUV")
    # print(base)

    paths = os.path.join(base, "SUV.txt")
    # print(paths)

    funkcion.slovo.main(base, paths)


SUV()
