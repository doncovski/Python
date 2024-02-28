import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row.letter: row.code for (index, row) in df.iterrows()}


def main():
    user_word = input("Please enter your word to convert: ").upper()
    try:
        output_list = [new_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry. Only letters from the alphabet please!")
        main()
    else:
        print(output_list)

main()
