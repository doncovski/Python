from morse import morse_code_dict


def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
        else:
            morse_code += char
    return morse_code


def main():
    input_text = input("Enter a string to convert to Morse code: ")
    morse_code = text_to_morse(input_text)
    print("Morse Code:", morse_code)


if __name__ == "__main__":
    main()
