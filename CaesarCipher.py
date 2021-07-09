#---------------------------------------
#-----------Caesar Cipher---------------
#---------------------------------------

# Ceaser Cipher class
class CaesarCipher:
    # this method encrypt the plain text
    @staticmethod
    def encrypt(string,key):
        result = ""
        for char in string:
            if char == " ": 
                result += " "
                continue
            if ord(char) > 96 :
                result += chr((ord(char) + key - 97) % 26 + 97)
            else:
                result += chr((ord(char)+ key - 65) % 26 +65)
            # acsii_value = ord(char)
            # temp = acsii_value - 97 if acsii_value > 96 else acsii_value - 65
            # new_ascii = (temp + key) % 26
            # new_char = chr(new_ascii+97) if acsii_value > 96 else chr(new_ascii+65)
            # result += new_char
        return result

    # this method decrypt cipher text
    @staticmethod
    def decrypt(string,key):
        result = ""
        for char in string:
            if char == " ":
                result += " "
                continue
            if ord(char) > 96 :
                result += chr((ord(char) - key - 97) % 26 + 97)
            else:
                result += chr((ord(char) - key -65) % 65 +65)
            # acsii_value = ord(char)
            # temp = acsii_value - 97 if acsii_value > 96 else acsii_value - 65
            # new_ascii  = (temp - key) % 26
            # new_char = chr(new_ascii+97) if acsii_value > 96 else chr(new_ascii+65)
            # result += new_char
        return result

#----Testing-------
if __name__ == "__main__":    
    String = "Hey i am a plain text"
    key = 3
    encrypted = CaesarCipher.encrypt(String,key)
    decrypted = CaesarCipher.decrypt(encrypted,key)
    print("Plain Text : ", String)
    print("Encrypted : ", encrypted)
    print("Decrypted : ", decrypted)