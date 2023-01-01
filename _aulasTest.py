import os
while True:
    frase = input(':: ')
    os.system('cls')
    print(frase.replace(' ', '_').ljust(0, '_')) 
