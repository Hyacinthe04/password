from credential import Credential
def create_credential(account,username,password):
    '''
    Function to create a new contact
    '''
    new_credential = Credential(account,username,password)
    return new_credential

def save_contacts(credential):
    '''
    Function to save contact
    '''
    credential.save_credential()

def del_credential(credential):
    '''
    Function to delete a contact
    '''
   credential.delete_credential()

def find_credential(username):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return Credential.find_by_username(username)

def check_existing_credentials(username):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return Credential.credential_exist(username)

def display_credentials():
    '''
    Function that returns all the saved contacts
    '''
    return Credential.display_credentials()


def main():
    print("Hello Welcome to your credential list. What is your name?")
            username = input()

            print(f"Hello {username}. what would you like to do?")
            print('\n')

            while True:
                    print("Use these short codes : cc - create a new credential, dc - display contacts, fc -find a contact, ex -exit the contact list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New Credential")
                            print("-"*10)

                            print ("account ....")
                            account = input()

                            print("username ...")
                            username = input()

                            print("password ...")
                            password = input()

                           


                            save_credentials(create_credential(account,username,password)) # create and save new contact.
                            print ('\n')
                            print(f"New Credential {username} {password} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_credentials():
                                    print("Here is a list of all your contacts")
                                    print('\n')

                                    for credential in display_credentials():
                                            print(f"{credential.account} {credential.username} .....{credential.password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any credentials saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the number you want to search for")

                            search_username = input()
                            if check_existing_credentials(search_username):
                                    search_credential = find_credential(search_username)
                                    print(f"{search_credential.first_name} {search_credential.last_name}")
                                    print('-' * 20)

                                    print(f"Phone number.......{search_credential.phone_number}")
                                    print(f"Email address.......{search_credential.email}")
                            else:
                                    print("That credential does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")