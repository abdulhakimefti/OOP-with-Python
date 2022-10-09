from socket import CAN_RAW


data = "firebaby"

encrypt = ""
for character in data :
    encrypt+=chr((ord(character)-87)%26+97)

print(encrypt)

