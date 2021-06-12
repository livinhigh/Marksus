import sys
from main import filecall
from wordcrypt import encrypt
from wordcrypt import wordshift

help="""
-h : List all options available
-e : Encrypt a word , usage : python marksus.py -e ivan 12
-dT | -dt : decrypt a textfile
-dW | -dw : decrypt a word , usage : python marksus.py -dw dxcg
"""
def showhelp():
    print(help)
try:        
    if(sys.argv[1]=="-e"):
        if(sys.argv[2].isalnum and sys.argv[3].isdigit):
            encrypt(word=sys.argv[2],shift=sys.argv[3])
        else:
            showhelp()
    elif(sys.argv[1]=="-h"):
        showhelp()
    elif(sys.argv[1]=="-dT" or sys.argv[1]=="-dt"):
        filecall()
    elif(sys.argv[1]=="-dW" or sys.argv[1]=="-dw"):
        if(sys.argv[2].isalpha):
            wordshift(sys.argv[2])
        else:
            showhelp()
except Exception as e:
    print(e)
    showhelp()