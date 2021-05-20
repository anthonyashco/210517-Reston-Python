l = 4
h = 5
t = "p0tato"
key = [
    " #  ##   ## ##  ### ###  ## # # ###  ## # # #   # # ###  #  ##   #  ##   ## ### # # # # # # # # # # ### ### ",
    "# # # # #   # # #   #   #   # #  #    # # # #   ### # # # # # # # # # # #    #  # # # # # # # # # #   #   # ",
    "### ##  #   # # ##  ##  # # ###  #    # ##  #   ### # # # # ##  # # ##   #   #  # # # # ###  #   #   #   ## ",
    "# # # # #   # # #   #   # # # #  #  # # # # #   # # # # # # #    ## # #   #  #  # # # # ### # #  #  #       ",
    "# # ##   ## ##  ### #    ## # # ###  #  # # ### # # # #  #  #     # # # ##   #  ###  #  # # # #  #  ###  #  ",
]
alph = "abcdefghijklmnopqrstuvwxyz"


def grabber(char, row):
    index = 26
    for i, c in enumerate(range(len(alph))):
        if alph[c] == t[char].lower():
            index = i
            break
    index = index * l
    return key[row][index:index + l]


for i in range(h):
    text = ""
    for j in range(len(t)):
        text = text + grabber(j, i)
    print(text)