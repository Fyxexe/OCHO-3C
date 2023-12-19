from encrypt import *
from decrypt import *

while True:
    action = input("Do you want to encrypt or decrypt? (Type 'encrypt' or 'decrypt'): ")

    if action.lower() == "encrypt":
        text = input("Enter text to encrypt: ")
        n = int(input("Enter n for additional level 1 encryption: "))

        tokenText = []
        for i in text:
            char_code = ord(i.upper()) if i.isalpha() else ord(i)
            tokenText.append([char_code])

        tokenText = sorting_for_encrypt_steep2([tokenText], n)
        tokenText = custom_encrypt(tokenText, n)
        tokenText = level2_encrypt(tokenText)
        tokenText = level3_encrypt(tokenText)

        for word in tokenText:
            for num in word:
                print(num, end=' ')
        print()

    elif action.lower() == "decrypt":
        text = input("Enter text to decrypt (separate numbers by spaces): ").split()
        n = int(input("Enter n for additional level 1 decryption: "))

        tokenText = [int(i) for i in text]
        tokenText = sorting_for_decrypt_steep2([tokenText], n)
        tokenText = custom_decrypt(tokenText, n)
        tokenText = level2_decrypt(tokenText)
        tokenText = level3_decrypt(tokenText)

        for char_code in tokenText[0]:
            print(chr(char_code), end='')
        print()

    else:
        print("Invalid choice. Please choose 'encrypt' or 'decrypt'.")

    again = input("Do you want to perform another operation? (Type 'yes' or 'no'): ")
    if again.lower() != "yes":
        break
