import os
import funkcion.slovo

def US():
    base = os.path.dirname(__file__)
    base = os.path.join(base, "US")
    # print(base)

    paths = os.path.join(base, "US.txt")
    # print(paths)


    funkcion.slovo.main(base, paths)
US()