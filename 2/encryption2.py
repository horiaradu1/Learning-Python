plaintext = input("Put the word that you want to encrypt here: ")
cipherText = ""
plaintextPosition = 0
while plaintextPosition < len(plaintext):
    plaintextChar = plaintext[plaintextPosition]
    ASCIIValue = ord(plaintextChar)
    ASCIIValue = ASCIIValue - 3
    cipherText = cipherText + chr(ASCIIValue)
    plaintextPosition = plaintextPosition + 1
print ("The encrypted word is: " + cipherText)
