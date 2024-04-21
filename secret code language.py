'''Coding:
if the word contains atleast 3 characters, remove the first letter and append it at the end now append three random characters at the starting and the end else: simply reverse the string

Decoding:
if the word contains less than 3 characters, reverse it else: remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

Your program should ask whether you want to code or decode'''


import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ans = " "
print("""
      ------------MENU--------------
      1. Code
      2. Decode
      """)
choice=int(input("Please enter your choice:"))
if choice==1:
    word=input("Please enter the word you want to code: ").lower()
    if len(word)>=3:
        ans = word[1:len(word)]+word[0]
        for i in range(0,3):
                rndm = random.randint(0,26)
                ans=ans+letters[rndm]
                rndm = random.randint(0,26)
                ans=letters[rndm]+ans
    else:
        for i in range(-1,-1-len(word),-1):
            ans=ans+word[i]
    print(f"The coded word is : {ans}")
elif choice==2:
    word=input("Please enter the word you want to code :").lower()
    if len(word)>=3:
        ans = word[-4]+word[3:-4]
    else:
        for i in range(-1,-1-len(word),-1):
            ans=ans+word[i]
    print(f"The decoded word is : {ans}")
else:
    print("Ayo! Please select the choice from the menu only")