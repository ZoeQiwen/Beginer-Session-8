alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

direction= input ("Ketik 'encode' untuk encryt, ketik 'decode' untuk decrypt\n").encode()
text = input("ketik pesananmu:\n").lower()
shift = int(input("ketik nomor shift:\n"))

def caesar(original_text,shift_amount,encode_or_decode):
    ouput_text = ""


    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount
        shifted_position %= len(alphabet)
        ouput_text += alphabet[shifted_position]

    print(f"ini adalah hasil {encode_or_decode}: {ouput_text}")
caesar(text,shift,direction)
