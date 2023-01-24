#Encryption using Vigener cipher and Caesar cipher
#Сreated by shameworm
alphabet_size = 26
class VigenerCipher:    #Vigener Cipher class 

    #key generator function
    def key_generator(message, key):
        key = list(key) #create list
        if len(message) == len(key): # if the length of the message matches the length of the key, the function returns the key 
            return(key) 
        else:   #break the key into auxiliary keys if the length of the message is longer than the key
            for i in range(len(message) -len(key)): 
                key.append(key[i % len(key)]) 
        return ("" . join(key))#return key  

    #encryption function
    def encryption(message, key):
        encrypt_txt = []#array for encrypt message

        for i in range(len(message)):
            x = (ord(message[i]) + ord(key[i])) % alphabet_size #x = Pi(unicode of message[i]) + Ki(unicode of key[i]) % alphabet_size
            x += ord("A")# x + Unicode of A character
            encrypt_txt.append(chr(x)) #add encrypt character to array
        return (''.join(encrypt_txt)) #return encrypt message as  a string 

class CaesarCipher: #Caesar cipher class
    
    #ecryption function
    def encryption(message):
        shift_pattern = input("Enter shift patern: ")#keyboard entry of the encryption step
        shift_pattern = int(shift_pattern)#transform entry to integer
        res = ""#result string 

        for i in range(len(message)):#loop for line feed
            ch = message[i]

            if(ch.isupper()):                                                          #if character of message is uppercase 
                res += chr((ord(ch) + shift_pattern-ord("A"))%alphabet_size + ord("A"))#res = ch(transform unicode to character) =
                #ch(Unicode of message[i]) + step - 67(unicode of uppercase A) % alhpabet size(26) + 67(unicode of uppercase A)
            
            else:                                                                     #if character of message is lowercase 
                res += chr((ord(ch) + shift_pattern - "a") % alphabet_size + ord("a"))#res = ch(transform unicode to character) =
                # =ch(Unicode of message[i]) + step - 97(unicode of uppercase A) % alhpabet size(26) + 97(unicode of uppercase A)

        return res
        



def main():
    while True:
        message = input("Enter the message: ")
        print("Choose the encryption method")
        crypto_choose = input("1. Vigenere Cipher\n2. Caesar Cipher\n0. Exit\t---\t")#Choose of encryption method
        match crypto_choose:
            case "1": #Vigenere Cipher
                keyword = input("Enter the keyword: ")
                key = VigenerCipher.key_generator(message,keyword)
                encrypt_text = VigenerCipher.encryption(message,key) 
                print("Encrypted message:", encrypt_text)
                print("\n")
            case "2": #Caesar cipher
                encrypt_text = CaesarCipher.encryption(message)
                print("Encripted message:", encrypt_text)
                print("\n")
            case "0":
                return 0
            case _:
                print("An error occurred. Please try again!") #if user try to enter something else
                print("\n\n")
    

main()
