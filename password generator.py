import random

#function to print the password of a given length a given number of times
def printpass(passstring, size,pnum):
    count = 0
    while(count<pnum):
        temp = random.sample(passstring,size)
        print("".join(temp))
        count+=1
        
#inputing number of passwords required and length of passwords required
passnum = int(input("Enter desired number of passwords: "))
length = int(input("Enter desired length of the password: "))

#creating sample spaces
cap = "QWERTYUIOPASDFGHJKLZXCVBNM"
small = "qwertyuiopasdfghjklzxcvbnm"
sym = "!@#$%^&*()_+{}|:\"<>?[];-',./"
num = "1234567890"

#creating flag variables for user options
strcap = str(input("should password contain capital letters? :"))
strsmall = str(input("should password contain small letters? :"))
strsym = str(input("should password contain symbols? :"))
strnum = str(input("should password contain numbers? :"))
pos = ['yes', 'YES', 'Yes']
neg = ['no', 'NO', 'No']

#if-else statements to print desired type of password
if strcap in pos and strsmall in neg and strsym in neg and strnum in neg:
    printpass(cap, length, passnum)
elif strcap in neg and strsmall in pos and strsym in neg and strnum in neg:
    printpass(small, length, passnum)
elif strcap in neg and strsmall in neg and strsym in pos and strnum in neg:
    printpass(sym, length, passnum)
elif strcap in neg and strsmall in neg and strsym in neg and strnum in pos:
    printpass(num, length, passnum)
elif strcap in pos and strsmall in pos and strsym in neg and strnum in neg:
    printpass(cap+small, length, passnum)
elif strcap in neg and strsmall in pos and strsym in pos and strnum in neg:
    printpass(small+sym, length, passnum)
elif strcap in pos and strsmall in neg and strsym in pos and strnum in neg:
    printpass(sym+cap, length, passnum)
elif strcap in pos and strsmall in neg and strsym in neg and strnum in pos:
    printpass(num+cap, length, passnum)
elif strcap in neg and strsmall in neg and strsym in pos and strnum in pos:
    printpass(num+sym, length, passnum)
elif strcap in neg and strsmall in pos and strsym in neg and strnum in pos:
    printpass(num+small, length, passnum)
elif strcap in pos and strsmall in pos and strsym in pos and strnum in neg:
    printpass(cap+small+sym, length, passnum)
elif strcap in neg and strsmall in pos and strsym in pos and strnum in pos:
    printpass(small+sym+num, length, passnum)
elif strcap in pos and strsmall in neg and strsym in pos and strnum in pos:
    printpass(sym+cap+num, length, passnum)
elif strcap in pos and strsmall in pos and strsym in neg and strnum in pos:
    printpass(num+small+cap, length, passnum)
else:
    print("Please enter proper choices.")
 
