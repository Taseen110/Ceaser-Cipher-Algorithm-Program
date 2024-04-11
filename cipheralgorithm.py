import sys
def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - s - 97) % 26 + 97)
        else:
            result += char
    return result

print("Welcome to the Caesar Cipher Algorithm")
choice = int(input("Press 1 for Message Encryption\nPress 2 for Message Decryption : "))
if choice not in [1,2]:
    print("Invalid Choice!")
    sys.exit()
text = input("Please Enter Message: ")
s = int(input("Please Enter Shift Value: "))

if choice == 1:
    print("Encrypted Message: " + encrypt(text, s))
elif choice == 2:
    print("Message Decrypted: " + decrypt(text, s))

