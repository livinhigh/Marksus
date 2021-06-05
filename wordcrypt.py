alphabets = 'abcdefghijklmnopqrstuvwxyz'


def dictVerify(dcipher):
    filename = 'C:\\Users\\jagat\\PycharmProjects\\Marksus\\dictionary\\%s.txt' % dcipher[0]
    with open(filename, 'r') as file:
        for line in file.readlines():
                if dcipher in line and len(line)-1 == len(dcipher):
                    print("The Encrypted Word is : %s" % dcipher)
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
        dictVerify(translated)