# print("Sezar Şifresi Kırma Programına Hoşgeldiniz.")
# sifresiz=input("Şifresi kırılacak metni giriniz:")
# def sifrele(metin):
#     sifrelimetin=""
#     for harf in metin:
#         asciikod=ord(harf)
#         asciikod=asciikod-3
#         karakterkod=chr(asciikod)
#         sifrelimetin=sifrelimetin+karakterkod
#     print("Şifresiz:",metin,"Şifreli:",sifrelimetin)

# sifrele(sifresiz)

# import random
# import string
# import os


# def clear():
#     os.system('cls')

#     # Renkler
# blue = '\033[1;34;48m'
# green = '\033[1;32;48m'
# red = '\033[1;31;48m'

# l_chars = string.ascii_lowercase
# u_chars = string.ascii_uppercase
# n_chars = string.digits
# p_chars = string.punctuation
# hesap = l_chars + u_chars + n_chars + p_chars

# banner = f'''
# {green}| {blue}Python SecurePass {green}\----------------------------\n '''


# while True:
#     clear()
#     print(banner)
#     lenght = input(f'{blue}> {green}Password uzunluğu : {red}')
#     data = random.sample(hesap,int(lenght))
#     password = ''.join(data)
#     clear()
#     print(banner)
#     print(f"{blue}>{green} Password : {red}" + password)
#     soru = input(f'{blue}> {green}Yeni şifre (y/n) : {red}')
#     if soru in 'y' or soru in 'Y':
#         continue
#     else:
#         exit()

MAX_KEY_VALUE=100
def getType():
    while True:
        type = input("Encrypt or Decrypt? (e or d).....:")
        if(type=="e" or type=="d"):
            return type
        else:
            print("You must enter e for encrypt or d for decrypt.....:")
def getKey():
    while True:
        key = int(input("Enter a key value between 1-{}".format(MAX_KEY_VALUE)))
        if(key>=1 and key<=100):
            return key
        else:
            print("You must enter a number between 1-{}".format(MAX_KEY_VALUE))
def getMessage(message,key,type):
    if type == "d":
        key = -key
    translated = ""
    for letter in message:
        if letter.isalpha():
            newLetter = ord(letter)
            newLetter += key
            if letter.isupper():
                if newLetter > ord("Z"):
                    newLetter -= 100
                elif newLetter < ord("A"):
                    newLetter += 100
            elif letter.islower():
                if newLetter > ord("z"):
                    newLetter -= 100
                elif newLetter < ord("a"):
                    newLetter += 100
            translated +=chr(newLetter)
        else:
            translated+=letter
    return translated
type = getType()
key = getKey()
message = input("Enter a message.......: ")
print("Translated message......: {}".format(getMessage(message,key,type)))