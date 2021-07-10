#Created by Jesus Vasquez-Cipriano
#Last Edit on: February 2, 2020
#Copyright © 2020 Jesus Vasquez-Cipriano. All rights reserved.

#This program ciphers and deciphers a user-inputted string
#by using the ordinal of the string's first character as the key to encrypt all string characters.
#The main program interacts (input/output) with the user, calling two functions to cipher and decipher.

def cipher(string):

    ciphered_string = ""
    
    key = ord(string[0])

    for eachCharacter in string:
        ciphered_string += chr(key + ord(eachCharacter))
        
    return ciphered_string

def decipher(string):
    
    deciphered_string = ""
    key = (ord(string[0]))//2
    
    for eachCharacter in string:
        deciphered_string += chr(abs(key - ord(eachCharacter)))
        
    return deciphered_string
    
def main():
    
    inputted_string = input("Give me a string to cipher and decipher: ")
    ciphered_string = cipher(inputted_string)
    deciphered_string = decipher(ciphered_string)
    
    print("This is your ciphered string: ", ciphered_string)
    print("This is your deciphered (original) string: ", deciphered_string)

main()
