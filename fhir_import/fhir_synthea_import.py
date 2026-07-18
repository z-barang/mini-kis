from fhir_client import upload_patient, search_patients_by_birthdate
from load_bundle import extract_resources, load_bundle
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent # current directory
json_filename = "Abdul218_Kuhlman484_a13d8b77-ca50-5a37-1f4c-c24a68778941.json" # name of json file / change when needed
full_path = BASE_DIR / json_filename # path to json file

bundle = load_bundle(full_path)
patients = extract_resources(bundle, 'Patient')


# Upload all patients to the server and print the
# server-assigned ID for each, this is the confirmation that the
# upload actually worked
for patient in patients:
    uploaded = upload_patient(patient)
    print(f"Uploaded patient, server ID: {uploaded.id}")

results = search_patients_by_birthdate('1998-02-27')
print (f"Found {len(results)} patient(s) with birthdate 1998-02-27")

for r in results:
    print(r.id, r.name[0].given[0], r.name[0].family)