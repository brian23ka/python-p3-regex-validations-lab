import re

# Updated name regex
name = r"^[A-Z][a-z]*(?:['-][A-Z][a-z]*)?(?: [A-Z][a-z]*(?:['-][A-Z][a-z]*)?)?$"
name_regex = re.compile(name)

# Existing phone number regex is OK
phone_number = r"^(\(\d{3}\)\s*|\d{3}[-.\s]?)\d{3}[-.\s]?\d{4}$"
phone_regex = re.compile(phone_number)

# Updated email regex (starts with a letter)
email_address = r"^[A-Za-z][\w\.-]*@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
email_regex = re.compile(email_address)
