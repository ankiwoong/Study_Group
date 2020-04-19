import re

# group()
phonenum_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phonenum_regex.search('Phone : 963-193-1853')
print(mo.group())


# groups()
phonenum_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phonenum_regex.search('Phone : 579-240-2288')
print(mo.groups())


# group 1, 2
phonenum_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phonenum_regex.search('Phone : 807-352-4368')
print(mo.group(1))
print(mo.group(2))

# findall
print(phonenum_regex.findall('Phone: 601-148-0677 TEL: 239-396-4504'))

phonenum_regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
print(phonenum_regex.findall('Cell: 740-427-7094 TEL : 472-658-9059'))
