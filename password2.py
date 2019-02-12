class Credential:
    """
    Class that generates new instances of contacts.
    """

    credential_list = [] # Empty user list

    def __init__(self,account,username,password):

      # docstring removed for simplicity
        self.account = account
        self.username = username
        self.password = password
        
        user_list = [] # Empty contact list
 # Init method up here