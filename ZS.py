import os
import funkcion.slovo

def ZS():
    base = os.path.dirname(__file__)
    base = os.path.join(base, "ZS")
    # print(base)

    paths = os.path.join(base, "ZS.txt")
    # print(paths)


    funkcion.slovo.main(base, paths)
ZS()