class DataPipeline:
    def __init__(self):
        self.consumer = None
        self.processors = []
        self.producer = None

    def with_consumer(self, data_consumer):
        self.consumer = data_consumer
        return self

    def with_processor(self, data_processor):
        self.processors.append(data_processor)
        return self

    def with_producer(self, data_producer):
        self.producer = data_producer
        return self

    def run(self):
        self.run_pre_hook()

        for data in self.consumer.consume():
            transformed_data = data
            for processor in self.processors:
                transformed_data = processor.transform(transformed_data)
            self.producer.produce(transformed_data)

        self.run_post_hook()

    def run_all(self):
        data_list = self.consumer.consume_all()
        for processor in self.processors:
            data_list = processor.transform_all(data_list)
        self.producer.produce_all(data_list)

    def run_pre_hook(self):
        self.consumer.pre()
        for processor in self.processors:
            processor.pre()
        self.producer.pre()

    def run_post_hook(self):
        self.consumer.post()
        for processor in self.processors:
            processor.post()
        self.producer.post()

# # CoLaus
# pipeline = DataPipeline()
# pipeline.with_consumer(CsvDataConsumer("../resources/CoLaus_sample_100linesShuffled.csv", "\t"))
# pipeline.with_processor(DataTransformer.from_mapping_file("../resources/colaus_cineca_mapping.csv"))
# pipeline.with_producer(JsonProducer("../resources/colaus_cineca_pipeline.json"))
# pipeline.run_all()
