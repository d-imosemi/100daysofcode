alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo
print(logo)


def caeser(start_text, shift_amount, cipher_direction):
    end_text = ''
    if cipher_direction == 'decode':
            shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f'the {cipher_direction}d text is {end_text}')

should_continue = True
while should_continue:
    direction = input("type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input('type your message:\n').lower()
    shift = int(input('type your shift number:\n'))


    shift = shift % 26
    caeser(start_text=text, shift_amount=shift, cipher_direction=direction)
    result = input('type "yes" if you want to go again. otherwise type "no".\n')
    if result == 'no':
        should_continue = False
        print('goodbye')