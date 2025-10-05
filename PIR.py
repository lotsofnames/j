import os
import funkcion.slovo

def PIR():
    base = os.path.dirname(__file__)
    base = os.path.join(base, "PIR")
    # print(base)

    paths = os.path.join(base, "PIR.txt")
    # print(paths)


    funkcion.slovo.main(base, paths)
PIR()