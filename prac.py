alphabet = "abcdefghijklmnopqrstuvwxyz"

def encrypt(plain_text, k):
    cipher_text = ""

    for char in plain_text.lower():
        if char in alphabet:
            p = alphabet.find(char)
            c = (p + k) % 26
            cipher_text += alphabet[c]
        else:
            cipher_text += char

    return cipher_text


def decrypt(cipher_text, k):
    plain_text = ""

    for char in cipher_text.lower():
        if char in alphabet:
            c = alphabet.find(char)
            p = (c - k) % 26
            plain_text += alphabet[p]
        else:
            plain_text += char

    return plain_text


def hack(cipher_text):
    for k in range(1, 26):
        result = decrypt(cipher_text, k)
        print(f"Key {k}: {result}")


print("1. Encrypt")
print("2. Decrypt")
print("3. Hack (Brute Force)")

choice = input("Choose 1, 2 or 3: ")

if choice == "1":
    text = input("Enter plain text: ")
    key = int(input("Enter key (k): "))
    print("Cipher Text:", encrypt(text, key))

elif choice == "2":
    text = input("Enter cipher text: ")
    key = int(input("Enter key (k): "))
    print("Plain Text:", decrypt(text, key))

elif choice == "3":
    text = input("Enter cipher text to hack: ")
    hack(text)

else:
    print("Invalid choice!")