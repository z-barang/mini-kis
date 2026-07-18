Profile: MiniKISPatient 
Parent: Patient // based on FHIR-Patient
Id: minikis-patient
Title: "MiniKIS Patient"
Description: "Patient-Profil für das Mini-KIS-Projekt"

* identifier 1..* MS // must support
* identifier.system 1..1 
* birthDate 1..1
* name 1..*