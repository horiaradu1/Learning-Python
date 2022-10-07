plaintext = input("Put the word that you want to encrypt here: ")
cipherText = ""
alphabet = "XYZABCDEFGHIJKLMNOPQRSTUVWXYZABC"
plaintextPosition = 0
while plaintextPosition < len(plaintext):
    plaintextChar = plaintext[plaintextPosition]
    alphabetPosition = 3
    while plaintextChar != alphabet[alphabetPosition]:
        alphabetPosition = alphabetPosition + 1
    alphabetPosition = alphabetPosition - 3
    cipherText = cipherText + alphabet[alphabetPosition]
    plaintextPosition = plaintextPosition + 1
print ("The encrypted word is: " + cipherText)
