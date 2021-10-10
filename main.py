import fitz
import json
import re



def validate_string(string):
   if len(string.replace('_',''))<1:
      return ''
   return string.strip()

#  function to extract one info
def key_values(blocks):
   result = dict()
   _key = None


   for block in blocks:
      for line in block['lines']:
         for span in line['spans']:
           
            

            if span['size'] > 15:
               #  getting the name
               result['name']=validate_string(span['text'])

             #  email and address
            elif span['origin'][0]>200 and span['origin'][0]<300:
               code_email = span['text'].split('|')
               print(code_email)
               if result.get('email') == None:
                  result['email'] = validate_string(code_email[1])
                  result['address'] =validate_string(code_email[0])
               else:
                  result['address'] += span['text']
            # if we found a subheading
            elif span['size']>=12 and span['size']<15:
               if span['text'].strip():
                  _key = validate_string(span['text'])

            else:
              
               if _key:
                  try:
                     result[_key] += validate_string(span['text'])
                  except KeyError:
                     result[_key] = validate_string(span['text'])

   print(result)

   # save the result to json file
   with open('result.json', 'w') as fp:
      json.dump(result, fp)

#  opening file
def extract_data(path):
   with fitz.open(path) as doc:
      for page in doc:
         key_values(page.getText('dict')['blocks'])


if __name__ == "__main__":
   extract_data("sample.pdf")