data_from_dataset = {
    "age": 25,
    "gender": "0",
    "sbsmk": "yes",
    "phyact": "2WK",
    "wt": 70,
    "cmatccd1_1": "A12AA",
    "cmatccd1_2": "Proton pump inhibitors",
}

transformed_data = {
    "demographic": {
        "age": 25,
        "gender": "0"
    },
    "lifestyle": {
        "tobacco": "yes",
        "physicalActivity": "2WK"
    },
    "physiologicalMeasurements": {
        "anthropometry": {
            "weight": 70
        }
    },
    "medication": {
        "other": [
            "A12AA",
            "Proton pump inhibitors"
        ]
    }
}

enhanced_fields = {
    "demographic": {
        "age": 25,
        "gender": "Female"
    },
    "lifestyle": {
        "tobacco": "yes",
        "physicalActivity": "2WK"
    },
    "physiologicalMeasurements": {
        "anthropometry": {
            "weight": 70
        }
    },
    "medication": {
        "other": [
            "A12AA",
            "Proton pump inhibitors"
        ]
    }
}

transformer_mapping = {
    "age": {"FIELD": "demographic.age", "DATA_TYPE": "string"},
    "gender": {"FIELD": "demographic.gender", "DATA_TYPE": "string"},
    "sbsmk": {"FIELD": "lifestyle.tobacco", "DATA_TYPE": "string"},
    "phyact": {"FIELD": "lifestyle.physicalActivity", "DATA_TYPE": "string"},
    "wt": {"FIELD": "physiologicalMeasurements.anthropometry.weight",
           "DATA_TYPE": "string"},
    "cmatccd1_1": {"FIELD": "medication.other", "DATA_TYPE": "[string]"},
    "cmatccd1_2": {"FIELD": "medication.other", "DATA_TYPE": "[string]"}
}

field_mapping = {
    "demographic.gender": {"0": "Female", "1": "Male"}
}
