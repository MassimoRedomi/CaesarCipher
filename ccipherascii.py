#CAESAR CIPHER ASCII (MONO-ALPHABETICAL)
import sys

def Ack():
    if(sys.argv[1]==("-h" or "-H")):
        print("USE:\n\n ccipherascii.py -e [ENCRYPT] [KEY] path/text.txt\nccipherascii.py -e [DECRYPT] [KEY] path/text.txt")
    elif(sys.argv[1]==("-e" or "-E")):
        return True
    elif(sys.argv[1]==("-d" or "-D")):
        return False
    sys.exit()

def Decrypt(c, k):
    return "".join(chr(((ord(l)-32-int(sys.argv[2])%95)%95)+32) for l in c)

def Encrypt(p, k):
    return "".join(chr(((ord(l)-32+int(sys.argv[2])%95)%95)+32) for l in p)

file=open("ciphertext.txt" if Ack() else "plaintext.txt", "w")
file.write(Encrypt(open(sys.argv[3], "r").read(),sys.argv[2]) if Ack() else Decrypt(open(sys.argv[3], "r").read(), sys.argv[2]))
file.close()




