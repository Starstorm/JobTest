# BusinessCardParser

This BusinessCardParser command line utility parses the results of an optical character recognition (OCR) component in order to extract the name, phone number, and email address from the processed business card image.

## Usage Instructions:

### Basic Installation & Setup
This installation presumes you already have Python 3 installed and usable with the command "Python". If you have both Python 2 and Pyhton 3 installed on your machine, you may need to change "python" to "python3" in the commands that follow. It was tested with Python 3.6 and 3.7. 

To create your own custom virtual environment (recommended) to test it in, if you have conda pre-installed, you can first run:
```
conda create -n TestingEnv python=3.7
source activate TestingEnv
```
Next, you can do the actual install:
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
However, keep in mind that the name parser works best in cases where there are newline characters.

If desired, you can send the output to a file:
```
python BusinessCardParser.py -f ../examples/example_1.txt -o output_card_data.txt
```
### Testing
You can also test to make sure the various methods are functioning correctly. First, make sure you're in the tests directory:
```
python -m unittest testing
```
If you're not in the tests directory when you run this command, you will likely get a ModuleError.

### Notes & Limitations
So there were a few points to bring up.
First, I was restricted by the interface requirements from improving the design further. Because the interface requires only Strings be returned instead of lists, my selection method for name/phone/email is inherently imperfect - it only finds the "top" element if there are multiple matches because there is no specification as to what the preference should be if there are two or more matches. Otherwise, I would have created additional fields such as "Home Phone", "Cell Phone", "Name One", "Name Two", etc. for each element. 

Second, the name parser works best with newline characters present for the business card. It's arguable whether or not this is a limitation or a feature: a poor OCR device might not return newline characters all the time, but attempting to parse a human name out of a single massively long string versus a single line of that string are two very different tasks. Adding the dozens of extra lines of code needed for the former task might end up actually decreasing overall accuracy if the latter task is the only one that matters - you gain flexiblity but could potentially lose out on raw accuracy for the more focused task. What's more, given the advancements in neural network based OCR technology in recent years and the examples provided, I presumed that newline characters would be present. The phone number and email parsers should work equally well, newline characters or not.

Finally, I added an extra capability - not only can the command line tool accept raw text, it'll also read text from a file and output to a file. Windows is not very fun to attempt to provide it a string argument with newline characters.
