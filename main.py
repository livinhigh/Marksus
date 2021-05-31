from wordcrypt import wordshift
from filecrypt import readfile


def filecall():
    print("File Path : ")
    path = input()
    readfile(path)

def wordcall():
    print("Encrypted Word : ")
    cipher = input()
    wordshift(cipher)


def switch2():
    print("1. Decrypt Textfile ")
    print("2. Decrypt Word/Sentence")
    choice2 = int(input())

    if choice2 == 1:
        filecall(),
    elif choice2 == 2:
        wordcall()
    else:
        print("Oops wring choice")
        switch2()

def switch1():
    print("1. Encrypt\n")
    print("2. Decrypt\n")
    choice = int(input())
    if choice == 1:
        print("under work"),
    elif choice == 2:
        switch2()
    else:
        print("Oops wrong choice")
        switch1()


print("MARKSUS\n")
switch1()
