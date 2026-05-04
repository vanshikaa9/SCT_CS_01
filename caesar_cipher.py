def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts text using the Caesar Cipher algorithm.

    Parameters:
        text  (str): The input message
        shift (int): The number of positions to shift each letter
        mode  (str): 'encrypt' or 'decrypt'
    
    Returns:
        str: The resulting encrypted or decrypted text
    """
    result = ""

    # For decryption, simply reverse the shift
    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            # Determine the ASCII base (uppercase or lowercase)
            base = ord('A') if char.isupper() else ord('a')

            # Shift the character and wrap around using modulo 26
            shifted = (ord(char) - base + shift) % 26
            result += chr(base + shifted)
        else:
            # Non-alphabetic characters are added unchanged
            result += char

    return result


def get_shift_value():
    """Prompts the user for a valid shift value between 1 and 25."""
    while True:
        try:
            shift = int(input("Enter shift value (1-25): "))
            if 1 <= shift <= 25:
                return shift
            else:
                print("Please enter a number between 1 and 25.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main():
    print("=" * 40)
    print("       CAESAR CIPHER PROGRAM")
    print("=" * 40)

    while True:
        print("\nOptions:")
        print("  1. Encrypt a message")
        print("  2. Decrypt a message")
        print("  3. Exit")

        choice = input("\nChoose an option (1/2/3): ").strip()

        if choice == "1":
            message = input("Enter the message to encrypt: ")
            shift = get_shift_value()
            encrypted = caesar_cipher(message, shift, "encrypt")
            print(f"\nOriginal  : {message}")
            print(f"Shift     : {shift}")
            print(f"Encrypted : {encrypted}")

        elif choice == "2":
            message = input("Enter the message to decrypt: ")
            shift = get_shift_value()
            decrypted = caesar_cipher(message, shift, "decrypt")
            print(f"\nOriginal  : {message}")
            print(f"Shift     : {shift}")
            print(f"Decrypted : {decrypted}")

        elif choice == "3":
            print("\nGoodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
