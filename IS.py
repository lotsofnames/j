import os
import funkcion.slovo


def IS():
    base = os.path.dirname(__file__)
    base = os.path.join(base, "IS")
    # print(base)

    paths = os.path.join(base, "IS.txt")
    # print(paths)

    funkcion.slovo.main(base, paths)


IS()
