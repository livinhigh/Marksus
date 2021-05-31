alphabets = 'abcdefghijklmnopqrstuvwxyz'

def wordshift(cipherword):
    for i in range(len(alphabets)):
        translated = ' '

        for char in cipherword:
            if char in alphabets:
                pos = alphabets.find(char)
                pos = pos - i

                if pos < 0:
                    pos = pos + len(alphabets)

                translated = translated + alphabets[pos]

            else:
                translated = translated + char
        print('Shift :%s  Text:%s' % (i, translated))