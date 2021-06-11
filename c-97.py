introString=input("enter your introduction lines: ")
characterCount=0
worldCount=1
for i in introString:
    characterCount=characterCount+1
    if(i==' '):
        worldCount=worldCount+1
print("number of words in a sting:")
print(worldCount)
print("number of characters in a string")
print(characterCount)
