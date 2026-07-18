import json
from pathlib import Path

#read synthea fhir bundle json file and extract patient resources

def load_bundle(filepath: str) -> dict:
    with open(filepath) as f: # open json file 
        bundle = json.load(f) 
    return bundle 


def extract_resources(bundle: dict, resource_type: str) -> list:
    results = []  # empty list 
    for entry in bundle['entry']:
        resource = entry['resource'] 
        if resource['resourceType'] == resource_type:  
            results.append(resource) 
    return results  


BASE_DIR = Path(__file__).resolve().parent # current directory
json_filename = "Abdul218_Kuhlman484_a13d8b77-ca50-5a37-1f4c-c24a68778941.json" # name of json file / change when needed
full_path = BASE_DIR / json_filename # path to json file

# test 
bundle = load_bundle(full_path)
patients = extract_resources(bundle, 'Patient')
print(len(patients), "Patients found")
print(patients[0]['birthDate'])
print(patients[0]['gender'])

encounters = extract_resources(bundle, 'Encounter')
print(len(encounters), "Encounters found")
print(encounters[0]['status'])
print(encounters[25]['status'])