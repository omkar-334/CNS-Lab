import re


def encrypt(text, key):
    text = list(text.lower().strip())
    length = len(text)

    for idx in range(length):
        if re.match("[a-z]", text[idx]):
            text[idx] = chr(ord(text[idx]) + key)
    return "".join(text)


def decrypt(text, key):
    text = list(text.lower().strip())
    length = len(text)

    for idx in range(length):
        if re.match("[a-z]", text[idx]):
            text[idx] = chr(ord(text[idx]) - key)
    return "".join(text)


text = "hello python"
key = 7

cipher = encrypt(text, key)
print(cipher)

text = decrypt(text, key)
print(text)
