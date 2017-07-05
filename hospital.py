class Hospital(object):

    def __init__(self, hospital_name, capacity):
        self.patients = []
        self.hospital_name = hospital_name
        self.capacity = capacity

    def admit(self,patient):
        if len(self.patients) >= self.capacity:
            print "Hospital at full capacity."
        else:
            patient.bed_number = str(len(self.patients)+1)
            self.patients.append(patient)
        return self
    
    def discharge(self, patient_name):
        for i,patient in enumerate(self.patients):
            if patient.p_name == patient_name:
                patient.bed_number = "None"
                self.patients.pop(i)
        return self

    def displayStats(self):
        for patient in self.patients:
            print patient.patient_id
            print patient.p_name
            print patient.p_allergies
            print patient.bed_number
        print self.hospital_name
        print self.capacity


class Patient(object):
    
    def __init__(self, patient_id, p_name, p_allergies):
        self.patient_id = patient_id
        self.p_name = p_name
        self.p_allergies = p_allergies
        self.bed_number = "None"
        

john = Patient(1,'John','PCN')
mary = Patient(2,'Mary','None')
tom = Patient(3,'Tom','Iodine')

goodHospital = Hospital('Good Hospital',2)

goodHospital.admit(john).admit(mary).admit(tom).discharge('John').displayStats()