class User:
    """
    Class that generates new instances of contacts.
    """

    user_list = [] # Empty user list

    def __init__(self,username,password):

      # docstring removed for simplicity

        self.username = username
        self.password = password
        
        user_list = [] # Empty contact list
 # Init method up here
    def save_user(self):

        '''
        save_user method saves contact objects into contact_list
        '''

        User.user_list.append(self)