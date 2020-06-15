from csv_consumer import CsvDataConsumer
from data_pipeline import DataPipeline
from data_transformer import DataTransformer
from field_value_transformer import FieldValueTransformer
from field_value_transformer_pre import FieldValueTransformerPre
from json_producer import JsonProducer

data_dir = "../resources/data/"
mapping_dir = "../resources/mapping/"


def main():
    # CoLaus
    DataPipeline() \
        .with_consumer(CsvDataConsumer(data_dir + "CoLaus_sample_100linesShuffled.csv", "\t")) \
        .with_processor(DataTransformer.from_mapping_file(mapping_dir + "colaus_cineca_mapping_questionnaire.csv")) \
        .with_processor(FieldValueTransformer.from_mapping_file(mapping_dir + "colaus_data_label_mapping.xlsx")) \
        .with_producer(JsonProducer(data_dir + "colaus_cineca.json")) \
        .run()

    # H3Africa
    DataPipeline() \
        .with_consumer(CsvDataConsumer(data_dir + "h3africa_dummy_datasets_for_cineca_demo.csv", ";")) \
        .with_processor(DataTransformer.from_mapping_file(mapping_dir + "h3africa_cineca_mapping_questionnaire.csv")) \
        .with_producer(JsonProducer(data_dir + "h3africa_cineca.json")) \
        .run()

    # CHILD
    DataPipeline() \
        .with_consumer(CsvDataConsumer(data_dir + "child_demo_data.csv", ",")) \
        .with_processor(FieldValueTransformerPre.from_mapping_file("../resources/mapping/child_initial_data_label_mapping.xlsx")) \
        .with_processor(DataTransformer.from_mapping_file(mapping_dir + "child_cineca_mapping_questionnaire.csv")) \
        .with_producer(JsonProducer(data_dir + "child_cineca.json")) \
        .run()


main()
