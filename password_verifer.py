def view_options(create_password, view_password_list, verify_password):

def make_password(password_prompt, list):
    new_password = list.append(password_prompt)
    return new_password
    
def password_verification(verify,  list):
    if verify in list:
        print('This is Correct')
    else:
        print('Please Try again')

def view_password_list(list):
    view_list = list

    return view_list


#something to view the options
create_new_password = input('Create a new password: ')
verify_password = input('What is your password? ')

view_options(create_new_password, verify_password, ) 

    
#paramaters for make_password
password_keeper = []
password_generator = make_password(create_new_password, password_keeper)

#parameters for view_password
check_password = password_verification(verify_password, password_keeper)
password_keeper = []
verified = 'Yes'
