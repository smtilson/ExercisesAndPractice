#This will contain things from the automate book section on regex

import re

PhoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

match = PhoneNumRegex.findall('My number is 415-555-4242. My number is 415-555-4282.')

print(match)

atRegex = re.compile(r'\w+at')
sample = atRegex.findall('The cat in the hat sat on the flat mat.')
print(sample)

noNewlineRegex = re.compile('(.*\s*)')
sample = noNewlineRegex.findall('Serve the public trust.\nProtect the innocent. \nUphold the law.')
print(sample)

def extract_emails(text):
    email = re.compile(r'(\w+\.?\w+@\w+\.\w+)', re.IGNORECASE)
    return email.findall(text)

def extract_emails2(text):
    email = re.compile(r'''(
    [a-z0-9._+%-]+
    @
    [a-z0=9.=]+
    (?:\.[a-z]{2,4})
    )''', re.VERBOSE|re.IGNORECASE)
    return email.findall(text)

def extract_phone(text):
    phoneRegex = re.compile(r'''( 
        (\d{3}|\(\d{3}\))? 
        (?:\s|-|\.)?
        (\d{3})
        (?:\s|-|\.)
        (\d{4}) 
        (\s*(ext|x|ext.)\s*(\d{2,5}))? 
        )''', re.VERBOSE)
    return phoneRegex.findall(text)

sample_text = '800-420-7240 415-863-9900 415-863-9950 info@nostarch.com media@nostarch.com academic@nostarch.com info@nostarch.com'

print(extract_emails(sample_text))
print(extract_emails2(sample_text))
print(extract_phone(sample_text))

