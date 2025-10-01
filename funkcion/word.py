import os


def file(z):
    #    print(z)
    slova = []
    with open(z, "r", encoding="utf-8") as fill:
        fill = fill.readlines()
        for line in fill:
            if line.replace(" ", "") != "" and line.replace(" ", "") != "\n":
                slova.append(line.replace("\n", ""))
    return slova


def main():
    slova = file("C:\\Users\\matus\\PycharmProjects\\j\\KS\\KS.txt")
    for slovo in slova:
        print(slovo)


if __name__ == "__main__":
    main()
