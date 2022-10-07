ciphertext = input("Put encrypted word here: ")
plaintext = ""
ciphertextposition = 0
while ciphertextposition < len(ciphertext):
    ciphertextchar = ciphertext[ciphertextposition]
    ASCIIValue = ord(ciphertextchar)
    ASCIIValue = ASCIIValue + 3
    plaintext = plaintext + chr(ASCIIValue)
    ciphertextposition = ciphertextposition + 1
print ("The decrypted word is: " + plaintext)
