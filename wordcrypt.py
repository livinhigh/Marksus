alphabets = 'abcdefghijklmnopqrstuvwxyz'


def dictVerify(dcipher, shift):
    filename = 'C:\\Users\\jagat\\PycharmProjects\\Marksus\\dictionary\\%s.txt' % dcipher[0]
    with open(filename, 'r') as file:
        for line in file.readlines():
                if dcipher in line and len(line)-1 == len(dcipher):
                    print("The Encrypted Word is : %s" % dcipher)
                    print("Shift is : ", shift)
    return

def wordshift(cipherword):
    for i in range(len(alphabets)):
        translated = ''
        for char in cipherword:
            if char in alphabets:
                pos = alphabets.find(char)
                pos = pos - i

                if pos < 0:
                    pos = pos + len(alphabets)

                translated = translated + alphabets[pos]

            else:
                translated = translated + char
        dictVerify(translated,i)


def encrypt():
    text = input("Enter Text: ")
    shift = int(input("Enter Shift: "))
    result = ""
    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            result += chr((ord(char) + shift - 65) % 26 + 65)

        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)

    print("Cipher: " + result)
    return