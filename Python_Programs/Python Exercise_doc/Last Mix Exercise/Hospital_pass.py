import json
import re


class hospital_gate(Exception):
    def __init__(self):
        self.floors = {'0': 'Cardiology', '1': 'Oncology', '2': 'Orthopaedic', '3': 'Ophthalmology'}
        self.problems = {'Cardiology': ['Heart', 'Blood Pressure', 'Cholesterol', 'Chest pain'],
                         'Ophthalmology': ['Lasik', 'Loss of vision', 'Color blindness', ' Change in vision'],
                         'Orthopaedic': ['Fracture', ' Arthritis', 'Back pain', 'Spine problem', 'Shoulder pain',
                                         'Joint replacement'],
                         'Oncology': ['Tumour', 'Chemo', 'Radiation']}
        self.floors_size = len(self.floors)
        self.patient_details = {}
        # self.patient_department = ""

    def doctor_fun(self):
        department = input("Please enter your department:--").title()
        cnt = 0
        try:
            for key, value in self.floors.items():
                if value == department:
                    print(" \u001b[42m \u001b[1m Here is your pass for", key, "st floot now you can access the floor",
                          key, "\u001b[0m")
                    break
                else:
                    cnt = cnt + 1
                if cnt == self.floors_size - 1:
                    raise hospital_gate
        except hospital_gate:
            print(" \u001b[1m \u001b[41m Please enter valid value, you have entered(", department, ")wrong value "
                                                                                                   "\u001b[0m")

    def patient_fun(self):

        patient_name = input("Please enter your Name:--")
        patient_mob = input("Please enter your Mobile number:--")
        # patient_add = input("Please enter your Address / City:--")
        # patient_age = input("Please enter your Age:--")
        # patient_gen = input("Please enter your Gender:--")
        patient_disease = input("Please enter your Disease:--").title()

        # for key_f, value_f in floors.items():

        for key_p, value_p in self.problems.items():
            if patient_disease in value_p:
                patient_department = key_p
                break
        for key_f, value_f in self.floors.items():
            if patient_department in value_f:
                patient_floor = key_f
                print("\u001b[42m \u001b[1m Here is your pass for floor", patient_floor, "and your department is: ",
                      patient_department, "\u001b[0m")
                self.patient_details["Name"] = patient_name
                self.patient_details["Mobile Number"] = patient_mob
                self.patient_details["Patient Floor"] = patient_floor
                self.patient_details["Department"] = patient_department
                self.patient_details["patient Disease"] = patient_disease

                print("Dictionary details are:---", self.patient_details)
                with open("patient_details.txt", "a+") as file:
                    # json_object = json.dumps(self.patient_details, indent=4, sort_keys=True)
                    # file.write(json_object + ",")
                    file.write("\n")
                    file.write(str(self.patient_details))

    def relatives_fun(self):
        search_patient_name = input("Please enter your relative /Person Name:--")
        # get_patient_floor = ""
        # get_patient_name = ""
        processes = []
        with open("patient_details.txt", "r") as file:
            read_file = file.read()
            file.seek(0)
            read_line = file.readlines()
            if search_patient_name in read_file:
                for num, line in enumerate(read_line, 0):
                    if search_patient_name in line and "Patient Floor" in line:
                        get_patient_floor = line.split()[-6].strip()
                        print(search_patient_name, "is on ", get_patient_floor, "floor")
                        # print("num is:--", num)
            else:
                print("Sorry,Patient name is not available......")
