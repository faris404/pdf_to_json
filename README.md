### Pdf to Json
Convert pdf file to json data,keys are subheading and values are other texts.

### Packages Used
- [click](https://pypi.org/project/click/) for command line options.
- [PyMuPDF](https://pypi.org/project/PyMuPDF/) for reading pdf file in dict format.
### Setups
- create virtualenv and activate it
- install packages using `pip install -r requirements.txt`
### Running
`python main.py --input sample.pdf --output output.json`