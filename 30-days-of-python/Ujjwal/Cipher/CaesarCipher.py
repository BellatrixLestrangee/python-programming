# Caesar Cipher replaces a character by some other character in a definite sequence.

def CaesarCipher(string):
    new_string = ''
    for i in string:
        new_string+=chr(ord(i)+3)
    return(new_string)
    
string = input("Enter String")
print(CaesarCipher(string))

    
