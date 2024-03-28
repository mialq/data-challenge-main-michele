import unittest
from event_validator import json_type_to_python_type

class TestJsonTypeToPythonType(unittest.TestCase):
    def test_conversion(self):
        self.assertEqual(json_type_to_python_type('string'), str)
        self.assertEqual(json_type_to_python_type('integer'), int)
        self.assertEqual(json_type_to_python_type('boolean'), bool)
        self.assertEqual(json_type_to_python_type('object'), dict)
        self.assertIsNone(json_type_to_python_type('unknown'))

if __name__ == '__main__':
    unittest.main()

#teste para validate_event
from event_validator import validate_event

class TestValidateEvent(unittest.TestCase):
    def test_event_validation(self):
        schema = {
            'required': ['name', 'age'],
            'properties': {
                'name': {'type': 'string'},
                'age': {'type': 'integer'}
            }
        }
        valid_event = {'name': 'Renata', 'age': 30}
        invalid_event = {'name': 'Renata', 'age': 'trinta'}
        
        # Testa um evento válido
        is_valid, message = validate_event(valid_event, schema)
        self.assertTrue(is_valid)
        
        # Testa um evento inválido
        is_valid, message = validate_event(invalid_event, schema)
        self.assertFalse(is_valid)

if __name__ == '__main__':
    unittest.main()

    