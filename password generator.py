import random
import string

#function to print the password of a given length a given number of times
def printpass(passstring, size,pnum):
    count = 0
    while(count<pnum):
        temp = random.sample(passstring,size)
        print("password :","".join(temp))
        count+=1
repeat = True
while repeat==True:
    #inputing number of passwords required and length of passwords required
    passnum = int(input("Enter desired number of passwords: "))
    length = int(input("Enter desired length of the password: "))

    #creating sample spaces using string library
    cap = string.ascii_uppercase
    small = string.ascii_lowercase
    sym = string.punctuation
    num = string.digits

    #lists conaining variations of positive or negative response
    pos = ['yes', 'YES', 'Yes']
    neg = ['no', 'NO', 'No']

    #creating flag variables for user options
    strall = str(input("should password contain all characters? :"))
    if strall in neg:
        strcap = str(input("should password contain capital letters? :"))
        strsmall = str(input("should password contain small letters? :"))
        strsym = str(input("should password contain symbols? :"))
        strnum = str(input("should password contain numbers? :"))



    #if-else statements to print desired type of password
    if strall in pos:
        printpass(cap+small+num+sym, length, passnum)
    elif strcap in pos and strsmall in neg and strsym in neg and strnum in neg:
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
    
    inp = str(input("Do you need more passwords?: " )) 
    repeat = True if inp in pos else False
    if repeat == False:
        print("Thank you for using the program")
