import os

def file(z):
    base = os.path.dirname(__file__)  # cesta ku snimace.py
    path = os.path.join(base, z)  # cesta k súboru IS.txt
    slova=[]
    with open(z,"r",encoding="utf-8") as fill:
        fill = fill.readlines()
        for line in fill:
            if line.replace(" ", "") != ""and line.replace(" ", "") != "\n":
                slova.append(line.replace("\n",""))
    return slova
def main():
    slova = file("IS.txt")
    for slovo in slova:
        print(slovo)
if __name__ == '__main__':
    main()