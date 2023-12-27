def make_password(password_prompt, list):
    new_password = list.append(password_prompt)
    return (new_password)

def password_verification(verify,  list):
    if verify in list:
        print('This is Correct')
    else:
        print('Please Try again')
    

create_new_password = input('Create a new password: ')
password_keeper = []
password_generator = make_password(create_new_password, password_keeper)

verify_password = input('What is your password? ')
check_password = password_verification(verify_password, password_keeper)
password_keeper = []
verified = 'Yes'