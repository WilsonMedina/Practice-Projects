import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,0123456789'

number = int(input('Amount of passwords to generate: '))
lenght = int(input('Input your password lenght: '))

print('\nHere are your password ')

for i in range(number):
    passwords = ''
    for c in range(lenght):
        passwords += random.choice(chars)
    
    print(passwords)