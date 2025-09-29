import sys

k = 5
l = [
    [1, 2, 3, 4, 8],
    [5, 1, 2, 3, 4],
    [4, 5, 1, 2, 3],
    [7, 4, 5, 1, 2],
    [2, 7, 4, 5, 1],
]
x = 0
y = 0
for p in range(k):
    for plus in range(k):
        i = l[x][y]
        print(i)
        for kon in range(k):
            konX = kon + x
            konY = kon + y
            if konX >= k or konY >= k:
                break
            if l[konX][konY] == i:
                pass
            else:
                sys.exit("kopa smetia")
        # print("dokanale diagonalne")
        x = x + 1
    y = y + 1
    x = 0
print("dokanale diagonalne")
