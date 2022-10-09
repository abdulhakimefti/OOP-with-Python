data = "aNtEriouraiwo/n/t>>"

newData = data.lower();
vowel = ""
for character in newData:
    # print(character);
    if character=='a' or character == 'i' or character=='o'or character=='u'or character=='e':
        vowel+=character
    

print(vowel)