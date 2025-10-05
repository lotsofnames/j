import os
import funkcion.slovo

def SP():
    base = os.path.dirname(__file__)
    base = os.path.join(base, "SP")
    # print(base)

    paths = os.path.join(base, "SP.txt")
    # print(paths)


    funkcion.slovo.main(base, paths)
SP()