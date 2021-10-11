import unittest
import json
class TestPDFParser(unittest.TestCase):

   def test_result(self):
      #  read json from result
      with open('result.json', 'r') as fp:
         result = json.load(fp)

      assert result['name']
      assert result['email']
      assert result['address']
      assert result['Education']
      assert result['Leadership Experience']
      assert result['Professional Experience']
      assert result['Additional Projects']
      assert result['Skills & Interests']


if __name__ == '__main__':
    unittest.main()