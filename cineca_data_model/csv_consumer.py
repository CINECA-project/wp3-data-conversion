import csv

import pandas as pd

from pipeline_process import PipelineProcess


class CsvDataConsumer(PipelineProcess):
    def __init__(self, file, delimiter=','):
        if file:
            self.data_file = file
            self.delimiter = delimiter
        else:
            print("Please specify data file for the consumer")

    def consume(self):
        with open(self.data_file, 'r') as f:
            data = csv.reader(f, delimiter=self.delimiter)
            headers = next(data, None)
            for row in data:
                yield dict(zip(headers, row))

    def consume_all(self):
        data_list = []
        df = pd.read_csv(self.data_file, sep=self.delimiter)
        headers = list(df)
        for index, row in df.iterrows():
            data_list.append(dict(zip(headers, row)))
        return data_list
