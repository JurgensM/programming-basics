def morse(txt):

    morse_code = {
        'A':'.-', 'B':'-...', 'C':'-.-.',
        'D':'-..', 'E':'.', 'F':'..-.',
        'G':'--.', 'H':'....', 'I':'..',
        'J':'.---', 'K':'-.-', 'L':'.-..',
        'M':'--', 'N':'-.', 'O':'---',
        'P':'.--.', 'Q':'--.-', 'R':'.-.',
        'S':'...', 'T':'-', 'U':'..-',
        'V':'...-', 'W':'.--', 'X':'-..-',
        'Y':'-.--', 'Z':'--..', '1':'.----', 
        '2':'..---', '3':'...--', '4':'....-', 
        '5':'.....', '6':'-....', '7':'--...', 
        '8':'---..', '9':'----.', '0':'-----'

    }

    output = ""
    txt = txt.upper()
    for letter in txt:
        for key in morse_code:
            if letter == key:
                output += morse_code[key]

    return output

def main():

    user = input("Insert a message to translate in morse: ")
    print(morse(user))

if __name__ == "__main__":
    main()