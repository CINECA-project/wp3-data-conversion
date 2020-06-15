import pandas as pd

from pipeline_process import PipelineProcess


class DataTransformer(PipelineProcess):
    def __init__(self, mapping=None):
        if mapping:
            self.mapping = mapping
        else:
            print("Please provide a mapping file for transformation")

    @classmethod
    def from_mapping_file(cls, file, delimiter=','):
        df = pd.read_csv(file, delimiter=delimiter)
        mapping_dict = dict()
        for index, row in df.iterrows():
            mapping_dict[row['MAPPING']] = {"FIELD": row['FIELD'], "DATA_TYPE": row['DATA_TYPE']}
        return cls(mapping_dict)

    def transform(self, data):
        transformed_data = {}
        for key, value in data.items():
            if key in self.mapping and not self.is_empty(value):
                self.add_to_data_dict(self.mapping[key]["FIELD"], value, self.mapping[key]["DATA_TYPE"],
                                  transformed_data)
        return transformed_data

    def transform_all(self, data_list):
        transformed_data = []
        for data in data_list:
            transformed_data.append(self.transform(data))

        return transformed_data

    @staticmethod
    def add_to_data_dict(key, value, data_type, data_dict):
        temp_dict = data_dict
        key_parts = key.split(".")
        for i, k in enumerate(key_parts):
            if i == len(key_parts) - 1:
                if data_type.startswith("["):
                    if k in temp_dict:
                        temp_dict[k].append(value)
                    else:
                        temp_dict[k] = [value]
                else:
                    temp_dict[k] = value
            else:
                if k not in temp_dict:
                    temp_dict[k] = {}
                temp_dict = temp_dict[k]

    @staticmethod
    def is_empty(value):
        return not value or str(value).lower() == "none"
