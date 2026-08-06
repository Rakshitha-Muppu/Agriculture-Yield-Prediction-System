import re

def validate_email(email):

    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    return bool(re.match(pattern, email))


def validate_phone(phone_number):

    return (
        len(phone_number) == 10
        and phone_number.isdigit()
    )


def validate_password(password):

    return len(password) >= 6