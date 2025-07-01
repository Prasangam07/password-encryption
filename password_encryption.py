# Password Encryption and Decryption Program using Base64
# Author: Prasangam Pathak
# Description: Encode and decode passwords using Base64.

import base64

print("🔐 Welcome to the Password Encryption Program 🔐")

def encode_password(password):
    """Encode the password to Base64."""
    encode_data = base64.b64encode(password.encode('utf-8'))
    return encode_data.decode('utf-8')

def decode_password(encoded_password):
    """Decode the Base64 encoded password back to normal."""
    try:
        decode_data = base64.b64decode(encoded_password.encode('utf-8'))
        return decode_data.decode('utf-8')
    except Exception as e:
        return f"❌ Error decoding: {e}"

choice = input("\nDo you want to (E)ncode or (D)ecode a password? (e/d): ").lower()

if choice == "e":
    password = input("Enter the password to encode: ")
    encoded_password = encode_password(password)
    print(f"✅ Encoded password: {encoded_password}")

elif choice == "d":
    encoded_password = input("Enter the Base64 password to decode: ")
    decoded_password = decode_password(encoded_password)
    print(f"🔓 Decoded password: {decoded_password}")

else:
    print("❌ Invalid choice. Please enter 'e' to encode or 'd' to decode.")
    
#use wisely
