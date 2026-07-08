def ceaser_cipher():
    print("let's begin")

    commute_to_perform = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").strip().lower()
    if commute_to_perform == 'encode':
        print("Encoding")
    elif commute_to_perform == 'decode':
        print("Decoding")
    else:
        print("Invalid input, please try again.")
        return ceaser_cipher()

    def operation():
        message = input("please write the message to perform operations:\n")
        shift_amount = int(input("Type the shift number:\n"))
        
        # We need a reference alphabet to find letter positions
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        if commute_to_perform == "encode":
            cipher_text = ""
            for char in message:
                # Keep spaces/symbols/numbers as they are
                if char.lower() in alphabet:
                    # Find the letter's index in the alphabet
                    position = alphabet.index(char.lower())
                    # Shift the index, wrapping around using % 26
                    new_position = (position + shift_amount) % 26
                    
                    # Keep the original casing (uppercase/lowercase)
                    new_char = alphabet[new_position]
                    cipher_text += new_char.upper() if char.isupper() else new_char
                else:
                    cipher_text += char
            print(f"Here is the encoded message: {cipher_text}")

        elif commute_to_perform == "decode":
            plain_text = ""
            for char in message:
                if char.lower() in alphabet:
                    position = alphabet.index(char.lower())
                    # Shift backward for decoding
                    new_position = (position - shift_amount) % 26
                    
                    new_char = alphabet[new_position]
                    plain_text += new_char.upper() if char.isupper() else new_char
                else:
                    plain_text += char
            print(f"Here is the decoded message: {plain_text}")

    operation()

    while True:
        choice = input("do you want to use the caesar cypher again: write 'yes' for yes and 'no' for no:\n" ).lower().strip()
        if choice == 'yes':
            ceaser_cipher()
        elif choice == 'no':
            print("Goodbye!")
            break
        else:
            print("Invalid input, please try again.")
            continue

ceaser_cipher()


