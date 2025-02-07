def encrypt (letter:str , key:int) -> str:
    return chr( ord(letter) * key)

def decrypt (letter:str, key:int) -> str: 
    return chr(ord(letter) // key) 

def encrypt_w (word: str, key:int) -> str: 
    new_word = ""
    for letter in word: 
        new_word += encrypt(letter, key)
    return new_word
    
def decrypt_w (word: str, key: int) -> str: 
    new_word = ""
    for letter in word: 
        new_word += decrypt(letter, key)
    return new_word

if __name__ == "__main__": 
    encrypt_or_decrypt = input("Would you like to encrypt or decrypt your message?: ").lower()
    
    if encrypt_or_decrypt not in ['encrypt', 'decrypt']: 
        print("Invalid choice. Please type either 'encrypt' or 'decrypt' to confirm your choice.")
    else: 
        word = input("Enter your message: ")
        key = int(input("Enter your key: "))
        
        if encrypt_or_decrypt == "encrypt": 
            encrypted = encrypt_w(word, key)
            print("\nOriginal:", word)
            print("Encrypted:", encrypted)
        elif encrypt_or_decrypt == "decrypt": 
            decrypted = decrypt_w(word, key)
            print("\nOriginal:", word)
            print("Decrypted:", decrypted)


