class ContactInfo(object):
    """
    A class used to represent the ContactInfo object
    ...
    Attributes
    ----------
    name : str
        The individual's name. Defaults to UNKNOWN.
    phone_number : str
        The individual's phone number. Defaults to UNKNOWN.
    email_address : str
       The individual's email address. Defaults to UNKNOWN.
    Methods
    -------
    String getName()
        Basic getter method for individual's name.
    String getPhoneNumber()
        Basic getter method for individual's phone number.
    String getEmailAddress()
        Basic getter method for individual's email address.
    String __str__()
        Define stringification for the ContactInfo object. Stringifies the ContactInfo object as specified in the instructions provided at https://asymmetrik.com/programming-challenges.
    """
    def __init__(self, name, phone_number, email_address):
        self.name = name
        self.phone_number = phone_number
        self.email_address = email_address
        
    def getName(self):
        return self.name
    
    def getPhoneNumber(self):
        return self.phone_number
    
    def getEmailAddress(self):
        return self.email_address
    
    def __str__(self):
        return "Name: " + self.getName() + "\nPhone: " + self.getPhoneNumber() + "\nEmail: " + self.getEmailAddress()
