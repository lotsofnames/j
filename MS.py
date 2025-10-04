import os
import funkcion.slovo

def MS():
    base = os.path.dirname(__file__)
    base = os.path.join(base, "MS")
    # print(base)

    paths = os.path.join(base, "MS.txt")
    # print(paths)


    funkcion.slovo.main(base, paths)
MS()