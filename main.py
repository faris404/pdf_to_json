import fitz
import json
import click

class PDFParser:


   def __init__(self,input_file,output_file):
      self.input = input_file
      self.output = output_file

   #  opening file and read all text with properties like size,origin in dict format
   def parse(self):
      try:

         with fitz.open(self.input) as doc:
            for page in doc:
               self.tojson(page.getText('dict')['blocks'])
      except Exception as e:
         # print(e.args[0])
         pass
      
   #  function to extract one info from the pdf blocks
   def tojson(self,blocks):

      result = dict()
      _key = None

      for block in blocks:
         for line in block['lines']:
            for span in line['spans']:

               #  if font size is more than 15 then it is a main heading(name)
               if span['size'] > 15:
                  result['name']=self.validate_string(span['text'])

               #  if the posistion is in center and not main heading then email and address
               elif span['origin'][0]>200 and span['origin'][0]<300:
                  code_email = span['text'].split('|') # getting email from string like 'xxx-yyy | emai@gmail.com'
                  
                  if result.get('email') == None:
                     result['email'] = self.validate_string(code_email[1])
                     result['address'] = self.validate_string(code_email[0])
                  else:
                     result['address'] += span['text']

               # if size of text between 12 and 15 the it is a sub heading
               elif span['size']>=12 and span['size']<15:
                  if span['text'].strip():
                     _key = self.validate_string(span['text'])
               else:
                  #  if we found any keys like (name,address,email and subheading) then others-
                  #  - will be value of keys(subheading)
                  if _key:
                     try:
                        result[_key] += self.validate_string(span['text'])
                     except KeyError:
                        result[_key] = self.validate_string(span['text'])

      # save the result to json file
      with open(self.output, 'w') as fp:
         json.dump(result, fp)


   #  remove _ from string (to remove underlines)  also white space
   def validate_string(self,string):
      if len(string.replace('_',''))<1:
         return ''
      return string.strip()


#  cammand lines using click
@click.command()
@click.option('--input', help='Input file path.')
@click.option('--output',help='Output file path.')
def main(input, output):
   #  validate inputs
   if not input or input.split('.')[1] != 'pdf':
      print('Invalid input file')
   elif not output or output.split('.')[1] != 'json':
      print('Invalid output file')
      
   else:
      #  parsing data
      pdf = PDFParser(input,output)   
      pdf.parse()

if __name__ == '__main__':
    main()

