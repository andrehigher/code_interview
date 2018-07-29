class User:
    """ Represents user in the system with their properties.
    """
    
    def __init__(self, name, age):
        """ Initializes user class with name and age. Also, active is False.
        """
        self.name = name
        self.age = age
        self.active = False
        self.warning = 0

    def set_active(self):
        """ Sets user as active.
        """
        self.active = True

    def set_inactive(self):
        """ Sets user as inactive.
        """
        self.active = False

    def set_warning(self):
        """ Sets user as inactive.
        """
        self.warning += 1
        if self.warning >= 3:
            self.active = False

    def clean_warning(self):
        """ Clean warnings.
        """
        self.warning = 0
        self.active = True