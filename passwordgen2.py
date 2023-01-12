import random
import string
import sys
import pyperclip



while True:

    r = int(input('Enter password length: '))
    choice = input('Special characters (y/n)?: ')
    characters1 = string.ascii_letters + string.digits + string.punctuation
    characters2 = string.ascii_letters + string.digits

    if choice == 'y':
        password = ''.join(random.choice(characters1) for i in range(r)) #Will choose random characters including punctuation
    else:
        password = ''.join(random.choice(characters2) for i in range(r)) #Will choose random characters w/o pubctuation

    print("Random password: ", password)

    while True:
        quit = input('All done (press (q) to quit, or Enter for a new password)?: ')
        if quit == '':
            break #This will send you to the beginning asking you for password length
        elif quit == 'q':
            pyperclip.copy(password) #Will copy password before exiting program to clipboard
            sys.exit()



