alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(text,shift,direction):
    cipher=""
    if direction=="decode":
        shift*=-1
    for letter in text:
        index=alphabet.index(letter)
        if index+shift<26:
            new_index=index+shift
            cipher+=alphabet[new_index]
        else:
            new_index=index+shift-26
            cipher+=alphabet[new_index]

    print(cipher)

stop=False

while not stop:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text,shift,direction)
    devam=input("Stop or continue?").lower()
    if devam=="stop":
        stop=True
        print("See you later")
