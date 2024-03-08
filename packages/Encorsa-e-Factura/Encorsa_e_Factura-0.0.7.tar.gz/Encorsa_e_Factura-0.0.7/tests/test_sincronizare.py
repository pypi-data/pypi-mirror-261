import unittest
import os
import sys
from datetime import datetime
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
        # Test case 1: Testing with extracted_data containing name and email
        # This case is important to ensure that the function correctly handles a dictionary with "name" and "email" keys.
        extracted_data = {
            "name": "John Doe",
            "email": "johndoe@example.com"
        }
        expected_result = [
            {"guid": "name", "svalue": "John Doe"},
            {"guid": "email", "svalue": "johndoe@example.com"}
        ]
        self.assertEqual(create_form_filed_json(extracted_data), expected_result)

        # Test case 2: Testing with extracted_data containing age and city
        # This case is important to verify that the function works correctly with a dictionary containing "age" and "city" keys.
        extracted_data = {
            "age": 25,
            "city": "New York"
        }
        expected_result = [
            {"guid": "age", "svalue": 25},
            {"guid": "city", "svalue": "New York"}
        ]
        self.assertEqual(create_form_filed_json(extracted_data), expected_result)

        # Test case 3: Testing with extracted_data containing country and zipcode
        # This case is important to ensure that the function handles a dictionary with "country" and "zipcode" keys correctly.
        extracted_data = {
            "country": "USA",
            "zipcode": "12345"
        }
        expected_result = [
            {"guid": "country", "svalue": "USA"},
            {"guid": "zipcode", "svalue": "12345"}
        ]
        self.assertEqual(create_form_filed_json(extracted_data), expected_result)

        # Test case 4: Testing with extracted_data containing language and version
        # This case is important to verify that the function correctly handles a dictionary with "language" and "version" keys.
        extracted_data = {
            "language": "Python",
            "version": 3.9
        }
        expected_result = [
            {"guid": "language", "svalue": "Python"},
            {"guid": "version", "svalue": 3.9}
        ]
        self.assertEqual(create_form_filed_json(extracted_data), expected_result)

        # Test case 5: Testing with extracted_data containing is_active and timestamp
        # This case is important to ensure that the function works correctly with a dictionary containing "is_active" and "timestamp" keys.
        extracted_data = {
            "is_active": True,
            "timestamp": datetime(2021, 9, 1, 12, 0, 0, 0)
        }
        expected_result = [
            {"guid": "is_active", "svalue": True},
            {"guid": "timestamp", "svalue": datetime(2021, 9, 1, 12, 0, 0, 0)}
        ]
        self.assertEqual(create_form_filed_json(extracted_data), expected_result)

if __name__ == '__main__':
    unittest.main()