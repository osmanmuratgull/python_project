#@osmanmuratgull
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
