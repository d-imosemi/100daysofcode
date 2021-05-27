import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_letter = {row.letter:row.code for (index, row) in data.iterrows()}
print(phonetic_letter)
is_true = True
while is_true:
    word = input("Enter a word: ").upper()

    output_data = [phonetic_letter[letter] for letter in word]
    print(output_data)

