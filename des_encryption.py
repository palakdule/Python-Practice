from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# DES requires an 8-byte key
key = b'PayKey12'

# Create DES cipher object
cipher = DES.new(key, DES.MODE_ECB)

# Payroll data
payroll_data = input("Enter payroll information: ")

# Encryption
plaintext = payroll_data.encode('utf-8')
padded_text = pad(plaintext, DES.block_size)
encrypted_data = cipher.encrypt(padded_text)

print("\nEncrypted Data (Hex):")
print(encrypted_data.hex())

# Decryption
decipher = DES.new(key, DES.MODE_ECB)
decrypted_padded = decipher.decrypt(encrypted_data)
decrypted_data = unpad(decrypted_padded, DES.block_size)

print("\nDecrypted Payroll Information:")
print(decrypted_data.decode('utf-8'))give commit msg
