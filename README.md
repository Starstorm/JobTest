# BusinessCardParser

This BusinessCardParser command line utility parses the results of an optical character recognition (OCR) component in order to extract the name, phone number, and email address from the processed business card image.

## Usage Instructions:

### Basic Installation & Setup
```
git clone https://github.com/Starstorm/JobTest.git
cd JobTest
python setup.py install
cd BusinessCardParser
```
### Usage Guide
To extract the contact info from the three examples provided:
```
python BusinessCardParser.py -f ../examples/example_1.txt
python BusinessCardParser.py -f ../examples/example_2.txt
python BusinessCardParser.py -f ../examples/example_3.txt
```
If you'd prefer to manually enter your text, you can do that as well:
```
python BusinessCardParser.py -t "Business Card Text...."
```
Finally, you can send the output to a file if you prefer:
```
python BusinessCardParser.py -f ../examples/example_1.txt -o output_card_data.txt
```
### Testing
You can also test to make sure the various methods are functioning correctly. First, make sure you're in the tests directory:
```
python -m unittest testing
```
### Notes & Limitations
So there were a few points to bring up.
First and foremost, I was restricted by the interface requirements in terms of additional improvements for the card reader. Because the interface requires only Strings be returned instead of lists, my selection method for name/phone/email is inherently imperfect - it only finds the "top" element if there are multiple matches because there is no specification as to what the preference should be if there are two or more matches. Otherwise, I would have created additional fields such as "Home Phone", "Cell Phone", "Name One", "Name Two", etc. for each element. 

Also, I added an extra capability - not only can the command line tool accept raw text, it'll also read text from a file. This should allow it an easier time functioning with newline characters.
