def make_password(password_prompt, list):
    new_password = list.append(password_prompt)
    return (new_password)

create_new_password = input('Create a new password: ')
password_keeper = []
password_generator = make_password(create_new_password, password_keeper)

print(password_keeper)