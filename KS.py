import os
import funkcion.slovo


def KS():
    base = os.path.dirname(__file__)
    base = os.path.join(base, "KS")
    # print(base)

    paths = os.path.join(base, "KS.txt")
    # print(paths)

    funkcion.slovo.main(base, paths)


KS()
