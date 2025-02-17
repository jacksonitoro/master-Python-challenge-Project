alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#Task 1:  create a function called encrypt() that takes original_text and shift_amount as 2 inputs


# for instance the original_text is "hello" shifted_amount is 2
def encrypt(original_text, shift_amount):
    cipher_text = ""

    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount  #7 --> 9
        #Handling out of range shift amount: for instance if you try to shift z forward by 9
        shifted_position %= len(alphabet) # 0 - 25
        cipher_text += alphabet[shifted_position]  #j

    print(f"Here is the encoded result: {cipher_text}")

encrypt(original_text=text, shift_amount=shift)

