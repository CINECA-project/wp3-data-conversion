import math

import numpy as np
import pandas as pd

from pipeline_process import PipelineProcess


class FieldValueTransformerPre(PipelineProcess):
    def __init__(self, mapping=None):
        if mapping:
            self.mapping = mapping
        else:
            print("Please provide a mapping file for transformation")

    @classmethod
    def from_mapping_file(cls, file):
        field_label_map = {}
        excel_file = pd.ExcelFile(file)
        for sheet_name in excel_file.sheet_names:
            df = excel_file.parse(sheet_name)
            df = df.replace(np.nan, '', regex=True)
            mapping_dict = dict()
            for index, row in df.iterrows():
                mapping_dict[str(row["KEY"])] = row["VALUE"]
            field_label_map[sheet_name] = mapping_dict

        return cls(field_label_map)

    def transform(self, data):
        return self.transform_values(data)

    def transform_all(self, data_list):
        transformed_data = []
        for data in data_list:
            transformed_data.append(self.transform(data))

        return transformed_data

    def transform_values(self, data):
        result = {}
        for key, value in data.items():
            mapped_value = value
            if key in self.mapping:
                if value in self.mapping[key]:
                    mapped_value = self.mapping[key][value]

            if mapped_value:
                result[key] = mapped_value

        return result

