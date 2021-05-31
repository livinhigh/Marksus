import operator
import re
import collections

charfrequency = {}
charfrequencysorted = {}
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def decrypt(shift):
    finput = open ("filename.txt", "r")
    inputstr = finput.read()
    outputstr = ''
    for i in range(len(inputstr)):
        char = inputstr[i]
        if (char.isupper()):
            outputstr += chr((ord(char) + shift-65) % 26 +65)
        elif (char.isspace()):
            outputstr += " "
        elif (char.islower()):
            outputstr += chr((ord(char) + shift -97) % 26 +97)
    foutput = open("output.txt","a")
    foutput.write("%s %s" % ("Shift :",shift))
    foutput.write('\n')
    foutput.write(outputstr)
    foutput.write('\n')
    return


def freqDictionary(charfrequency):
    print(charfrequency)
    total=0
    for i in charfrequency:
        total += charfrequency[i]
    for j in charfrequency:
        charfrequency[j] = (float)((charfrequency[j]/total)*100)
    charfrequencysorted = dict(sorted(charfrequency.items(), key=operator.itemgetter(1), reverse=True))
    return charfrequencysorted


def readfile(path):
    fileObj = open(path, "r")
    charStream = fileObj.read()
    charStream = charStream.lower()
    charStream = re.sub("[^a-z]","",charStream,0, re.MULTILINE )
    print(charStream)
    for char in  charStream:
        if char in charfrequency:
             charfrequency[char] += 1
        else:
            charfrequency[char] = 1
    charfrequencysorted = freqDictionary(charfrequency)
    foutput = open("output.txt", "r+")
    foutput.truncate(0)
    foutput.close()
    for i in range(0, 5):
        testchar = list(charfrequencysorted.keys())[i]
        shift = alphabet.index('e') - alphabet.index(str(testchar))
        print(shift)
        decrypt(shift)







