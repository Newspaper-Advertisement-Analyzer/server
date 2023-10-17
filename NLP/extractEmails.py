import re
text = "Please contact us at contact@tutorialspoint.com for further information."+\
        " You can also give feedbacl at feedback@tp.com"


def extract_emails(text):
    emails =  re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
    if len(emails) == 0:
        return None
    else:
        return emails
