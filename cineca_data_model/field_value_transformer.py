import pandas as pd

from pipeline_process import PipelineProcess


class FieldValueTransformer(PipelineProcess):
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
            mapping_dict = dict()
            for index, row in df.iterrows():
                mapping_dict[str(row["KEY"])] = row["VALUE"]
            field_label_map[sheet_name] = mapping_dict

        return cls(field_label_map)

    def transform(self, data):
        return self.traverse_dict_values(None, data, None, None)

    def transform_all(self, data_list):
        transformed_data = []
        for data in data_list:
            transformed_data.append(self.transform(data))

        return transformed_data

    def traverse_dict_values(self, parent, obj, key, path):
        if isinstance(obj, dict):
            for dict_key, value in obj.items():
                self.traverse_dict_values(obj, value, dict_key, path + "." + dict_key if path else dict_key)
        elif isinstance(obj, list):
            for i in range(0, len(obj)):
                self.traverse_dict_values(obj, obj[i], key, path)
        else:
            if isinstance(parent, dict):
                parent[key] = self.recursive_mapping(path, obj)
            elif isinstance(parent, list):
                index = parent.index(obj)
                parent.remove(obj)
                parent.insert(index, self.recursive_mapping(path, obj))

        return obj

    def recursive_mapping(self, path, key):
        mapping = key
        path_segments = path.split(".")
        for i in range(0, len(path_segments)):
            aggregated_path = ".".join(path_segments[0: len(path_segments) - i])
            if aggregated_path in self.mapping and key in self.mapping[aggregated_path]:
                mapping = self.mapping[aggregated_path][key]
                break

        return mapping
