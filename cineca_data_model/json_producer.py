import json
import logging

from pipeline_process import PipelineProcess

logger = logging.getLogger('JsonProducer')

class JsonProducer(PipelineProcess):
    def __init__(self, file_name):
        self.file_name = file_name
        self.json_data_list = []
        self.start = True

    def produce(self, data):
        with open(self.file_name, 'a') as f:
            if self.start:
                self.start = False
            else:
                f.write(',\n')
            f.write(json.dumps(data))

    def produce_all(self, data_list):
        with open(self.file_name, 'w') as f:
            json.dump(data_list, f, indent=2)

    def pre(self):
        logger.info("Start writing JSON data to file")
        with open(self.file_name, 'w') as f:
            f.write('[\n')
            f.close()

    def post(self):
        with open(self.file_name, 'a') as f:
            f.write('\n]')
            f.close()

        logger.info("Finished writing JSON data file")
