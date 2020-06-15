import unittest

from field_value_transformer import FieldValueTransformer
from test import test_data


class TestFieldValueTransformer(unittest.TestCase):

    def test_recursive_mapping(self):
        field_transformer = FieldValueTransformer(test_data.field_mapping)
        female_mapping = field_transformer.recursive_mapping("demographic.gender", "0")
        self.assertEqual(female_mapping, "Female")

    def test_traverse_dict_values(self):
        field_transformer = FieldValueTransformer(test_data.field_mapping)
        transformed_data = field_transformer.transform(test_data.transformed_data)
        self.assertDictEqual(transformed_data, test_data.enhanced_fields)


if __name__ == '__main__':
    unittest.main()
