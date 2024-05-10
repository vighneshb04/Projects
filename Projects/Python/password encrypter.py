import string

all_characters = string.printable  # includes letters, digits, and special characters
print(all_characters)
num_characters = len(all_characters)


def encryption_decryption(text, mode, key):
    result = ''
    if mode == 'd':
        key = -key

    for char in text:
        if char in all_characters:
            index = all_characters.find(char)
            new_index = (index + key) % num_characters
            result += all_characters[new_index]
        else:
            result += char

    return result


print()
print('****CAESAR CIPHER****')
print()
cn = 'y'
while cn == 'y':

    print('Do you want to encrypt (e) or decrypt (d)?')
    user_input = input().lower()
    print()



    #ENCRYPTION MODE
    if user_input == 'e':
        print('Encryption MODE')
        print()

        key = int(input('Enter the key (1 to 94): '))

        if 1 <= key <= 94:
            text = input(f'Enter the text to {user_input}crypt: ')
            result = encryption_decryption(text, user_input, key)
            result = result.replace(""," ")
            print(f'Ciphertext: {result}')
        else:
            print('Invalid key. Please enter a key between 1 and 94.')


    #DECRYPTION MODE
    elif user_input == 'd':
        print('Decryption MODE')
        print()

        key = int(input('Enter the key (1 to 94): '))

        if 1 <= key <= 94:
            text = input('Enter the text to decrypt: ')
            result = encryption_decryption(text, user_input, key)
            result = result.replace("`", " ")
            print(f'Plaintext: {result}')
        else:
            print('Invalid key. Please enter a key between 1 and 94.')



    else:
        print('Invalid mode. Please enter "e" for encryption or "d" for decryption.')

    cn = input('Do you want to continue? (y/n)').lower()
