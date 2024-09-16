# Caesar Cipher Encryption and Decryption

# Function to encrypt the message
def encrypt(text, shift):
    encrypted_message = ""
    for char in text:
        # Encrypt uppercase letters
        if char.isupper():
            encrypted_message += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase letters
        elif char.islower():
            encrypted_message += chr((ord(char) + shift - 97) % 26 + 97)
        # Leave non-alphabet characters unchanged
        else:
            encrypted_message += char
    return encrypted_message

# Function to decrypt the message
def decrypt(text, shift):
    decrypted_message = ""
    for char in text:
        # Decrypt uppercase letters
        if char.isupper():
            decrypted_message += chr((ord(char) - shift - 65) % 26 + 65)
        # Decrypt lowercase letters
        elif char.islower():
            decrypted_message += chr((ord(char) - shift - 97) % 26 + 97)
        # Leave non-alphabet characters unchanged
        else:
            decrypted_message += char
    return decrypted_message

# Main function to handle user input and perform encryption or decryption
def caesar_cipher():
    print("Caesar Cipher Algorithm")
    while True:
        choice = input("\nChoose an option (1. Encrypt, 2. Decrypt, 3. Exit): ")

        if choice == "1":
            # Get the message and shift value from the user
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value (0-25): "))
            encrypted_message = encrypt(message, shift)
            print(f"Encrypted message: {encrypted_message}")

        elif choice == "2":
            # Get the message and shift value from the user
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value (0-25): "))
            decrypted_message = decrypt(message, shift)
            print(f"Decrypted message: {decrypted_message}")

        elif choice == "3":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")

# Run the Caesar Cipher program
if __name__ == "__main__":
    caesar_cipher()
