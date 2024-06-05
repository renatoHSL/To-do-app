def strength(password):
    validations = []

    long = False
    if len(password) >= 8:
        long = True

    upper_case = False
    print(upper_case)
    is_digit = False
    print(is_digit)

    for i in password:
        if i.isdigit():
            is_digit = True
        if i.isupper():
            upper_case = True

    validations.append(upper_case)
    validations.append(is_digit)
    validations.append(long)

    print(validations)

    if all(validations):
        return "Strong Password"

    else:
        return "Weak Password"

print(strength("NhWD8Sqs5UKWHs4JTPH"))