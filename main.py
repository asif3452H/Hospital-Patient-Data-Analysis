

from models.patient import Patient


def main():

    patient = Patient(
        101,
        "Rahim",
        45,
        "Diabetes",
        "Dhaka",
        12000
    )

    print(patient)


if __name__ == "__main__":
    main()