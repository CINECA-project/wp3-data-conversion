class Cineca:
    cohortAttribute = None
    biosample = None
    laboratoryMeasures = None
    surveyAdministration = None
    questionnaire = None
    researchDataDocuments = None
    statistics = None


class CohortAttribute:
    aimsAndObjectives = None
    timeline = None
    studyDesign = None
    populationData = None
    demographicData = None


class Biosample:
    sampleType = None
    availability = None
    processingMethod = None
    storageMethod = None


class LaboratoryMeasures:
    microbiology = None
    genomics = None


class SurveyAdministration:
    dateAndTimeRelatedInformation = None
    consentAccessibility = None
    uniqueIdentifiers = None


class Questionnaire:
    demographic = None
    lifestyle = None
    Physician = None
    diseases = None
    symptoms = None
    physiologicalMeasurements = None
    nonPharmacologicalInterventions = None
    medication = None
    lifeStage = None


message = {
    "cohortAttribute": {
        "objectives": None,
        "timeline": None,
        "studyDesign": None,
        "populationData": {
            "location": None,
            "enrollmentProcedures": None,
            "numberOfParticipants": None,
        },
        "demographicData": {
            "sexesStudied": None,
            "gendersStudied": None,
            "ageRange": None,
        }
    },
    "biosample": {
        "sampleType": {
            "urine": None,
            "blood": {
                "venousOrArterial": None,  # check representation
                "fastingOrNonFasting": None
            },
            "stool": None,
            "saliva": None,
            "other": None
        },
        "availability": None,
        "processingMethod": None,
        "storageMethod": None
    },
    "laboratoryMeasures": {
        "microbiology": {
            "microbialData": None,
            "biosampleSource": None,
            "availableDataFormats": None
        },
        "genomics": {
            "dataType": {
                "dna": None,  # dna/genotyping separate or not?
                "wgs": None,
                "wes": None,
                "sequenceVariants": None,
                "epigenetics": None,
                "metagenomics": None,
                "rnaSeq": None,
                "eqtl": None,
                "other": None
            },
            "sampleSize": None,
            "availableDataFormats": None,
            "availability": None,
            "processingMethod": None,
            "associatedCellTissueBiosampleType": None,
            "associatedPhenotype": None,
            "associatedDisease": None,
            "associatedMedication ": None
        }
    },
    "surveyAdministration": {
        "dateAndTimeInfo": None,
        "consentAccessibility": None,
        "uniqueIdentifiers": None
    },
    "questionnaire": {
        "demographic": {
            "age": None,  # age/birthdate separate or not?
            "biologicalSex": None,
            "gender": None,
            "ethnicity": None,
            "genealogy": None,
            "birthPlace": None,
            "residence": None,
            "education": None,
            "householdStructure": None
        },
        "lifestyle": {
            "tobacco": None,
            "alcohol": None,
            "physicalActivity": None,
            "sleep": None,
            "nutrition": None
        },
        "Physician": None,
        "diseases": {
            "bloodRelatedDisorders": None,
            "endocrine": None,  # endocrine/nutritional/metabolic disorders truncated is that ok?
            "mentalAndBehaviourDisorders": None,
            "nervousSystem": None,
            "digestiveSystem": None,
            "respiratorySystem": None,
            "circulatorySystem": None,
            "oncological ": None,
            "other": None  # new value to capture other cases
        },
        "symptoms": None,
        "physiologicalMeasurements": {
            "anthropometry": {
                "weight": None,
                "height": None
            },
            "circulationAndRespiration": {
                "bloodPressure": None,
                "heartRate": None
            }
        },
        "nonPharmacologicalInterventions": {
            "surgicalInterventions": None
        },
        "medication": {
            "associatedDiseases": None,
            "prescription": None,
            "drugResponse": None,
            "posology": None,
            "administrationMethod": None,
            "other": None  # new value to capture other cases
        },
        "lifeStage": None
    },
    "researchDataDocuments": None,
    "statistics": None
}
