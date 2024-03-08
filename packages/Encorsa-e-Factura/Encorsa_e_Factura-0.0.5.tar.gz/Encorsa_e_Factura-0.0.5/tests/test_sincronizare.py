import unittest
import os
import sys
# Get the absolute path of the current file
current_file_path = os.path.abspath(__file__)

# Get the directory containing the current file
current_directory = os.path.dirname(current_file_path)

# Get the parent directory of the current directory
parent_directory = os.path.dirname(current_directory)

# Add the grandparent directory to the sys.path
sys.path.append(parent_directory+"/src/Encorsa_e_Factura")
from sincronizare import create_form_filed_json


class TestCreateFormFieldJson(unittest.TestCase):
    def test_create_form_field_json(self):
        # Test case 1
        extracted_data = {
            "name": "John Doe",
            "email": "johndoe@example.com"
        }
        expected_result = [
            {"guid": "name", "svalue": "John Doe"},
            {"guid": "email", "svalue": "johndoe@example.com"}
        ]
        self.assertEqual(create_form_filed_json(extracted_data), expected_result)

        # Test case 2
        extracted_data = {
            "age": 25,
            "city": "New York"
        }
        expected_result = [
            {"guid": "age", "svalue": 25},
            {"guid": "city", "svalue": "New York"}
        ]
        self.assertEqual(create_form_filed_json(extracted_data), expected_result)

        # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()