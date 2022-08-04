#this is a email and phone number extractor to make work easier
#by @nyamosi

import re #the regular expression module
import pyperclip #module that will help copy and paste items to the clipboard

#this is the phone number extractor
phoneRegex= re.compile ('''(
(\d{3}|\(\d{3}\))?              #areacode
(\s|-|\.)?                      #separator
(\d{3})                         #first three digits
(\s|-|\.)                       #separator
(\d{4})                         #last four digits
(\s*(ext|x|ext.) \s*(\d{2,5}))? #extension
)''',re.VERBOSE)

#this is the email extractor
emailRegex = re.compile (r'''(
[a-z A-Z 0-9._%+-]+            #username
@                              #symbol
[a-z A-Z 0-9.-]+               #domain name
(\.[a-z A-Z] {2,4})            #dot something
)''',re.VERBOSE)


#finding matches in the clipboard
text=str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] == '':
                        phoneNum  == ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
                        matches.append(groups[0])

#copying results to the clipboard

if len(matches) > 0:
                        pyperclip.copy('\n'.join(matches))
                        print("copied to clip:")
                        print('\n'.join(matches))
else:
        print("Try again no numbers or email addresses found")
                    

