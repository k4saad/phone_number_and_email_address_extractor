#! python3
# phoneAndEmail.py - Extract email and phone number from and on clipboard

import pyperclip, re

numbers = '''
    +919820397879
    +91-9820397879
    +91 9820397879
    009920577934
    00 9920577934
    00-9920577934
    8850701287
    2223336665
    

    '''


phoneRegex = re.compile(r" (\+91|0{0,2})?([-|\s])?([6789]\d{9})")

results = phoneRegex.findall(numbers)
#results = phoneRegex.finditer(numbers)
for res in results:
    print(f"{res[0]}{res[1]}{res[2]}")