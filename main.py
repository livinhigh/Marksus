from wordcrypt import wordshift
from filecrypt import readfile
from wordcrypt import encrypt

def filecall():
    path = input("File Path : ")
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
    print("1. Encrypt")
    print("2. Decrypt")
    choice = int(input())
    if choice == 1:
        encrypt()
    elif choice == 2:
        switch2()
    else:
        print("Oops wrong choice")
        switch1()

print(".___  ___.      ___      .______       __  ___      _______. __    __       _______.")
print("|   \/   |     /   \     |   _  \     |  |/  /     /       ||  |  |  |     /       |")
print("|  \  /  |    /  ^  \    |  |_)  |    |  '  /     |   (----`|  |  |  |    |   (----`")
print("|  |\/|  |   /  /_\  \   |      /     |    <       \   \    |  |  |  |     \   \    ")
print("|  |  |  |  /  _____  \  |  |\  \----.|  .  \  .----)   |   |  `--'  | .----)   |   ")
print("|__|  |__| /__/     \__\ | _| `._____||__|\__\ |_______/     \______/  |_______/    ")
print("                                                                                    ")
switch1()
