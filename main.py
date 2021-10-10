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
   email_regx = r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

   for block in blocks:
      for line in block['lines']:
         for span in line['spans']:
            email_chk = re.findall(email_regx,span['text'])
            if email_chk:
               result['email'] = email_chk[0]
            if span['size'] > 15:
               #  getting the name
               result['name']=validate_string(span['text'])
 

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