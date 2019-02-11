class  Credentials:
    """
    Class that generates new instances of contacts.
    """

    credentials_list = [] # Empty user list

    def __init__(account,username,password):

      # docstring removed for simplicity

        self.username = username
        self.password = password
        self.account = account
        
        
        user_list = [] # Empty contact list