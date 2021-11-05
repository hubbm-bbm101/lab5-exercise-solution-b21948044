def valid(email):
    if "@" in email and "." in email:
        return True
    return False
print(valid("sufirat05@@gmail.com"))

