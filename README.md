# Mini-KIS

A small hospital information system (HIS) built as a learning project, using
FHIR (R4), synthetic patient data (Synthea), and DICOM image handling (pydicom).

## Status

In progress. Currently working: FHIR resource upload/search against a public
test server, and a custom FHIR profile defined with FHIR Shorthand.

## Stack

- Python
- FastAPI (planned for the backend API)
- FHIR: `fhirpy` (client), `fhir.resources` (validation/data models)
- Custom FHIR profile: FHIR Shorthand (FSH), compiled with SUSHI
- pydicom (planned, for DICOM image handling)

## Project structure
mini-kis/
├── fhir_import/       # load Synthea bundles, extract resources, upload/search via fhirpy
├── profiles/           # FHIR Shorthand (FSH) source and compiled StructureDefinitions
├── backend/            # FastAPI application (planned)
├── dicom_viewer/        # pydicom-based image handling (planned)
└── requirements.txt

## What works so far

- Parsing Synthea-generated FHIR bundles (`load_bundle.py`)
- Extracting resources of a given type from a bundle (`extract_resources`)
- Uploading Patient resources to a FHIR server via `fhirpy`
- Searching for Patient resources by birthdate via `fhirpy`
- A custom `MiniKISPatient` profile (FHIR Shorthand), constraining the base
  `Patient` resource with required identifier, birthDate, and name
