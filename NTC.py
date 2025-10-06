import os
import funkcion.slovo


def NTC():
    base = os.path.dirname(__file__)
    base = os.path.join(base, "NTC")
    # print(base)

    paths = os.path.join(base, "NTC.txt")
    # print(paths)

    funkcion.slovo.main(base, paths)


NTC()
