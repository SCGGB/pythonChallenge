#Encrytion file in python
#This program receives a file in txt and transform the data
#using the ascii map to change the letters

def encryption(inputText):
    print('Encription function')
    finalText = ''
    for character in inputText:
        asciiMap=ord(character)
        asciiMap+=1
        finalText += chr(asciiMap)
    return finalText


def decryption(inputText):
    print('Decryption function')
    finalText = ''
    for character in inputText:
            asciiMap = ord(character)
            asciiMap += 1
            finalText += chr(asciiMap)
    return finalText



def encryptionFile(location):
    fileEnc = open(location,'r')
    inputText = fileEnc.read()
    encryptedText = encryption(inputText)

    fileEnc = open(location,'w')
    fileEnc.write(encryptedText)
    fileEnc.close()
    print('The file was ecrypted')

def decryptionFile(location):
    fileEnc = open(location,'r')
    inputText = fileEnc.read()
    decryptedText = decryption(inputText)

    fileEnc = open(location,'w')
    fileEnc.write(decryptedText)
    fileEnc.close()
    print('The file was decrypted')


userAnwer=input('Choose  "E" for encryption or choose "D" for decryption')
fileLocation=input('Select the file location')

if userAnwer.upper()=='E':
    encryptionFile(fileLocation)
else:
    decryptionFile(fileLocation)

