import unittest

from data_transformer import DataTransformer
from test import test_data


class TestDataTransformer(unittest.TestCase):

    def testAddToDataDict(self):
        key = 'demographic.age'
        value = 60
        data_type = "string"
        data_dict = {}
        DataTransformer.add_to_data_dict(key, value, data_type, data_dict)

        print(data_dict)
        self.assertEqual(data_dict, {'demographic': {'age': 60}})

    def testTransform(self):
        data_transformer = DataTransformer(mapping=test_data.transformer_mapping)
        transformed_data = data_transformer.transform(test_data.data_from_dataset)

        print(transformed_data)
        self.assertDictEqual(transformed_data, test_data.transformed_data)


def test_transform_from_file(self):
    data_transformer = DataTransformer.from_mapping_file(
        "../../resources/mapping/colaus_cineca_mapping_csv")
    transformed_data = data_transformer.transform(test_data.data_from_dataset)

    print(transformed_data)
    self.assertDictEqual(transformed_data, test_data.transformed_data)


if __name__ == '__main__':
    unittest.main()
