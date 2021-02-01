#this program is used to encrypt and decrypt files
#If you want to use this program please read the ReadMe first as you can mess up your files
import sys, os
from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from os import path


pathname = os.path.dirname(sys.argv[0])+ '\\'  

def SetPassword():
    pWord = input("Enter what you would like your password to be, Pick somthing long, that you will remember:")
    if pWord == input("Congerm your password:"):
        tempKey = SaltPassword(pWord)
        pasFile = open ("password.txt","wb+")
        pasFile.write(tempKey)
        print("Changed password To "+pWord)
        pasFile.close()
        EntryPrompt()
    else:
        print("Passwords did not match")
        SetPassword()

# the only reason that i am wasting time salting the p-Word is to waste peoples time if they try to use dictonary attacks
# reading this wastes your time 
def SaltPassword(passwordString):
    
    password = passwordString.encode() 
    salt = b'TheBestSaltsAreRandomStings0fNumbersAndCharecters,This1Isnt ' 
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),length=32,salt=salt,iterations=42069,backend=default_backend())      
    return base64.urlsafe_b64encode(kdf.derive(password))
    

def DecryptFile(filey, decKey):
    with open(filey, 'rb') as f:
        data = f.read()  
    print (decKey)
    fernet = Fernet(decKey)
    try:
        decrypted = fernet.decrypt(data)
        with open(filey, 'wb') as f:
            f.write(decrypted) 
            f.close()

    except:
       print("Key BAd? Unsuccessfully decrypted")

def EncryptFile(filey, encKey):
    with open(filey, 'rb+') as f:
        data = f.read()     
        fernet = Fernet(encKey)
        encrypted = fernet.encrypt(data)
        f.seek(0) 
        f.write(encrypted)
        f.truncate()
        f.close()


# goes through every file in the same directary as this script, and also every sub directary below this script.
# It then eaither encrypts those files or dycripts them based on encryption state 
# if encriptStat = 0 encrypt, if = 1 decrypt
def LoopThroughFiles(path, encKey, encryptState):
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_dir():
                LoopThroughFiles(path + entry.name + '\\',encKey,encryptState)
            # string matching is a really slow way to do this, try not to get upset about it
            elif (entry.name != 'FileScrambler.py' and entry.name !='trackEncryptionState.txt' ):
               
                if encryptState == 0:
                    EncryptFile(entry, encKey)
                   
                else:
                    DecryptFile(entry, encKey)
                   


# this runs to check if files are all ready encrypted to see if its ok to encrypt them if it is it encrypts them
def AttemptEncrypt():
    isEncryptedFile = open ("trackEncryptionState.txt","w+")
    if(isEncryptedFile.read() != "1"):
        #go On With Encryptin
        print("encryption state != 1")
        pasFile = open ("password.txt","rb")
        encKey = pasFile.read()
        pasFile.close()
        LoopThroughFiles(pathname,encKey,0)

        isEncryptedFile.write("1")
    else:
        print("files are allready encrypted, doing it twice could cause big problems")
    isEncryptedFile.close()

def StartDecrypt():
    #decrypt sh!+
    decKey = SaltPassword(input("Enter your password: "))
    print(decKey)
    LoopThroughFiles(pathname,decKey,1)
    ptKeyFile = open("password.txt","rb+")
    ptKey = ptKeyFile.read()
    if (decKey == ptKey):
        isEncryptedFile = open ("trackEncryptionState.txt","w+")
        isEncryptedFile.write("0")
        isEncryptedFile.close()
    else:
        print("Decryption failed")

def EntryPrompt():

    promptState = input("\n [1] Spaghettify your files. \n[2] Unspaghettify your files. \n [3] Change your password.\n")
    if(promptState == "1"):
        AttemptEncrypt()
    elif(promptState =="2"):
        StartDecrypt()
    elif(promptState =="3"):
        SetPassword()
    else:
        print("Pick a valid Option you nitwit")
        EntryPrompt()


# Give the user the text prompt when they run the file
print("Welcome To FileScrambler4000, how can I help you today. ") 
if path.isfile("password.txt"):
    pFile = open ("password.txt","r")
    fileLength  = len(pFile.read())
else: 
    fileLength = 0

print(fileLength)
if 1 > fileLength:
    print("You need a password before you can do anything else")
    SetPassword()
pFile.close()
EntryPrompt()
