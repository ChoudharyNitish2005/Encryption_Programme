# This is my python project on making a programme which will encode and decode a given messege. It can be used as secret language
mode = input ("To encode a messege type encode, and to decode type decode in small letters : ")
Words = input(f"type your text to {mode} : ").split()
import random
def encode():
    charpool = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'
    for index, word in enumerate(Words):
        if len(word) > 1:
            word = word[1:] + word[0]
        prefix = "".join(random.choices(charpool, k=3))
        suffix = "".join(random.choices(charpool, k=3))
        Words[index] = prefix + word + suffix
    print(f" ".join(Words))
def decode():
    for index, word in enumerate(Words):
        word = word[3:-3]
        if len(word) > 1:
            word = word[-1] + word[:-1]
        Words[index] = word
    print(f" ".join(Words))
if mode == "encode":
    encode()
elif mode == "decode":
    decode()