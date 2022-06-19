def has_num():
    def inner():
        pass
    return inner

def has_uppercase(func):
    def inner(*args, **kwargs):
        value = func(*args, **kwargs)
        value_upper = value.lower()
        if value_upper == value:
            return 0   # ... should have at least one capital letter!
        else:
            return 1   # ... has at least one capital letter.

    return inner

def has_lowercase(func):
    def inner(*args, **kwargs):
        value = func(*args, **kwargs)
        value_upper = value.upper()
        if value_upper == value_upper:
            return 0 # ... should have at least one lowercase letter!
        else:
            return 1 # ... has at least one lowercase letter.
    return inner

def length_bigger_than_8(func):
    def inner(*args, **kwargs):
        value = func(*args,**kwargs)
        if len(value) >= 8:
            return 1
        else:
            return 0


    return inner

@length_bigger_than_8
@has_lowercase
@has_uppercase
@has_num
def validation_username(user_name):
    pass

@length_bigger_than_8
@has_lowercase
@has_uppercase
@has_num
def validation_password():

    return '12345678'