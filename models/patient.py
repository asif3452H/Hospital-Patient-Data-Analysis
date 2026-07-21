

class Patient:

    def __init__(self, patient_id, name, age, disease, city, cost):

        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.city = city
        self.cost = cost

    def __str__(self):

        return (
            f"ID: {self.patient_id} | "
            f"Name: {self.name} | "
            f"Age: {self.age} | "
            f"Disease: {self.disease} | "
            f"City: {self.city} | "
            f"Cost: {self.cost}"
        )