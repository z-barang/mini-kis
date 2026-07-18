from fhirpy import SyncFHIRClient

# the client connects to an FHIR server, in this case the public FHIR HAPI-Server 
# at https://hapi.fhir.org/baseR4
client = SyncFHIRClient("https://hapi.fhir.org/baseR4")

def upload_patient(patient_data: dict):
    """
    takes a single patient dict (e.g. from the extract_resources() function) 
    and creates a real FHIR resource on the server
    """
  
    # client.resource(...) creates a FHIRResource object from the raw dict.
    # Patient is the resourcetype fhirpy needs to know in order to speak to the right endpoint (/Patient).
    patient_resource = client.resource("Patient", **patient_data)
    
    # .save() sends a POST/PUT to the server and creates the resource there.
    # the server validates automatically against the FHIR specification.
    patient_resource.save()

    return patient_resource

def search_patients_by_birthdate(birthdate: str):
    """
    Shows the other direction: not uploading, but querying the server.
    fhirpy builds a FHIR search query in the background (?birthdate=...).
    """
    patients = client.resources("Patient").search(birthdate=birthdate).fetch()
    return patients