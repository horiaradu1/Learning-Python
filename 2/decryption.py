ciphertext = input("Put encrypted word here: ")
plaintext = ""
alphabet = "XYZABCDEFGHIJKLMNOPQRSTUVWXYZABC"
ciphertextposition = 0
while ciphertextposition < len(ciphertext):
    ciphertextchar = ciphertext[ciphertextposition]
    alphabetposition = 3
    while ciphertextchar != alphabet[alphabetposition]:
        alphabetposition = alphabetposition + 1
    alphabetposition = alphabetposition + 3
    plaintext = plaintext + alphabet[alphabetposition]
    ciphertextposition = ciphertextposition + 1
print ("The decrypted word is: " + plaintext)
