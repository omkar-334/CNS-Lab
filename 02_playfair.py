import string

all_letters = string.ascii_lowercase.replace("j", "")

key = input("Enter key - ")
text = input("Enter text - ")

key = list(key.lower().replace(" ", ""))
key = list(dict.fromkeys(key))

text = text.lower().replace(" ", "").replace("j", "i")
length = len(text)

others = [i for i in all_letters if i not in key]
matrix = key + others

keymatrix = [[None] * 5 for _ in range(5)]
for i in range(len(matrix)):
    row = i // 5
    col = i % 5
    keymatrix[row][col] = matrix[i]

i = 0
textlist = []
while True:
    if i == length - 1:
        textlist.append(text[i] + "z")
        break
    if text[i] == text[i + 1]:
        textlist.append(text[i] + "x")
        i -= 1
    else:
        textlist.append(text[i] + text[i + 1])
    i += 2
    if i - 1 == length:
        break


ciphertext = []
for pair in textlist:
    a, b = pair[0], pair[1]

    idxa, idxb = matrix.index(a), matrix.index(b)
    rowa = idxa // 5
    cola = idxa % 5

    rowb = idxb // 5
    colb = idxb % 5

    if rowa == rowb:
        cola += 1
        colb += 1
        cola %= 5
        colb %= 5
    elif cola == colb:
        rowa += 1
        rowb += 1
        rowa %= 5
        rowb %= 5
    else:
        cola, colb = colb, cola

    ciphertext.append(keymatrix[rowa][cola] + keymatrix[rowb][colb])

print(ciphertext)
