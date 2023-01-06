#! python3
# Author    - Saad khan
# Date      - 1/6/2023
# phoneAndEmail.py - Extract email and phone number from and on clipboard

import pyperclip, re

numbersAndEmails = '''
    +919820397879
    +91-9820397879
    azizzaid308@gmail.com
    +91 9820397879
    009920577934
    saadkhan108b@gmail.com
    00 9920577934
    00-9920577934
    mshahid108b@gmail.com
    8850701287
    2223336665
    

    '''

# Creating phone regex

phoneRegex = re.compile(r''' 
    (\+91|0{0,2})?  #Country code
    ([-|\s])?       #Separator
    ([6789]\d{9})   #Phone Number
    ''', re.VERBOSE)

# Creating email regex

emailRegex = re.compile(r'''(
    ([A-Za-z0-9.+-_%]+)     #Username 
    @                       #@ symbol
    [A-Za-z0-9.+-_%]+       #Domain Name
    \.[a-zA-Z]{2,4}         #Dot extension
    )''', re.VERBOSE)



results = phoneRegex.findall(numbersAndEmails)

print(results)