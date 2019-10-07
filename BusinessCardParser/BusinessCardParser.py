class BusinessCardParser(object):
    """
    A class used to represent the BusinessCardParser
    ...

    Attributes
    ----------
    phone_regex : str
        a regex string to match a US-based phone number. Will NOT match international phone numbers!
    email_regex : str
        a regex string to match an email address. Does not check if a domain actually exists, however.
    name_db : NameDataset object
        a NameDataset object which contains approximately 160k human first names (Western characters only)
    name_ner : spacy.lang.en.English object
        An object used for Named Entity Recognition (NER) tasks in the English language.

    Methods
    -------
    ContactInfo getContactInfo(String document)
        Extracts the name, email address, and phone number from the provided document string. Meant for internal use.
    String extractName(String document)
        Extracts the name from the provided document string
    String[] extractEmailPhone(String document)
        Extracts the email address and phone number from the provided document string. Meant for internal use.
    String cleanDoc(String document)
        Conducts basic cleaning activities for the text to clear out excessive newline characters, trailing spaces, and tabs.
    """

    def __init__(self):
        import spacy, names_dataset
        self.name_db = names_dataset.NameDataset()
        self.name_ner = spacy.load('en_core_web_sm')
        self.phone_regex = '(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?'
        self.email_regex = """(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
        
    def getContactInfo(self, document):
        # Clean the document
        document = self.cleanDoc(document)
        
        # Extract the name, email, and phone
        name = self.extractName(document)
        email, phone = self.extractEmailPhone(document)
        
        # Return ContactInfo object
        return ContactInfo(name, phone, email)
    
    def extractName(self, document):
        name = "UNKNOWN"
        # Run Named Entity Recognition on the document
        entities = self.name_ner(document)
        
        # Extract all identified PERSONs in the document with more than one word
        people = [str(elem) for elem in entities.ents if elem.label_ == "PERSON" and str(elem).strip().count(" ") > 0]
        
        # If only one person is found, that becomes the name
        if len(people) == 1:
            name = people[0].replace("\n","").strip()
        
        # If more than one person is found, run second layer of name identification with the name_db object.
        # The first person it finds (i.e. the name closest to the "top" of the business card) is the name we select.
        elif len(people) > 1:
            for person in people:
                first_name = person.split()[0].strip()
                if self.name_db.search_first_name(first_name):
                    name = person
                    break
        return name
    
    def extractEmailPhone(self, document):
        email = "UNKNOWN"
        phone = "UNKNOWN"
        
        # Split document into lines and scan for phone numbers and email addresses.
        # Once again, find the "top" phone and the "top" email address - if multiple are provided, ignore the bottom ones.
        document_lines = document.split("\n")
        for line in document_lines:
            phone_re = re.search(self.phone_regex,line)
            email_re = re.search(self.email_regex,line)
            if phone_re and phone == "UNKNOWN" and not line.startswith(("Fax","fax","FAX")):
                raw_phone_number = phone_re.group().strip()
                phone = re.sub('[^0-9]','', raw_phone_number)
            if email_re and email == "UNKNOWN":
                email = email_re.group().strip()
        return email, phone
    
    def cleanDoc(self, document):
        doc_lines = document.split("\n")
        doc_cleaned = "\n".join([line.replace("\t"," ").strip() for line in doc_lines if line.strip() != ""])
        return doc_cleaned

# Execution begins here
if __name__ == '__main__':
    # Import required modules
    import argparse, re, sys
    from ContactInfo import ContactInfo
    # Configure ArgumentParser for command line interface
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--file", help="Business card text file")
    ap.add_argument("-t", "--text", help="Business card raw text")
    ap.add_argument("-o", "--output", help="Output text for file. If not used, will display to screen.")
    my_args = vars(ap.parse_args())
    
    # Check if either the file or the raw text parameter is set, but not both.
    if (not my_args['text'] and not my_args['file']) or (my_args['text'] and my_args['file']):
        print("[ERROR] Input parameters not set properly. Please use the --help argument for more information on proper usage.")
        sys.exit(0)
        
    # Instantiate BusinessCardParser object
    my_parser = BusinessCardParser()
    
    # Get the business card text
    if my_args['file']:
        with open(my_args['file'],"r") as card_file:
            document = card_file.read()
    else:
        document = my_args['text']
       
    # Generate ContactInfo object
    my_contact_info = my_parser.getContactInfo(document)
    
    # Output results of ContactInfo object
    if my_args['output']:
        with open(my_args['output'], "w") as output_file:
            output_file.write(str(my_contact_info))
    else:
        print(str(my_contact_info))
