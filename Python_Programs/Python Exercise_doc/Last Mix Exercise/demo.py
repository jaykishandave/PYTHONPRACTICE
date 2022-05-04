import json
import re

floors = {'0': 'Cardiology', '1': 'Oncology', '2': 'Orthopaedic', '3': 'Ophthalmology', '4': 'General'}
problems = {'Cardiology': ['Heart', 'Blood Pressure', 'Cholesterol', 'Chest pain'],
            'Ophthalmology': ['Lasik', 'Loss of vision', 'Color blindness', 'Change in vision'],
            'Orthopaedic': ['Fracture', 'Arthritis', 'Back pain', 'Spine problem', 'Shoulder pain',
                            'Joint replacement'],
            'Oncology': ['Tumour', 'Chemo', 'Radiation'], 'General': ['Cough', 'Fever', 'Headache']}

patient_details = {}

# department = input("Please enter your department:--").title()

# patient_name = input("Please enter your Name:--")
# patient_mob = input("Please enter your Mobile number:--")
# # patient_add = input("Please enter your Address / City:--")
# # patient_age = input("Please enter your Age:--")
# # patient_gen = input("Please enter your Gender:--")
# patient_disease = input("Please enter your Disease:--").title()
search_patient_name = input("Please enter your relative /Person Name:--")

# for key_f, value_f in floors.items():

# for key_p, value_p in problems.items():
#     if patient_disease in value_p:
#         patient_department = key_p
#         break
# for key_f, value_f in floors.items():
#     if patient_department in value_f:
#         patient_floor = key_f
#         print("\u001b[42m \u001b[1m Here is your pass for floor", patient_floor, "and your department is: ",
#               patient_department, "\u001b[0m")
#         patient_details["Name"] = patient_name
#         patient_details["Mobile Number"] = patient_mob
#         patient_details["Patient Floor"] = patient_floor
#         patient_details["Department"] = patient_department

# print("Dictionary details are:---", patient_details)
with open("patient_details.txt", "a+") as file:
    # file.write(json.dumps(patient_details)+"\n")
    file.seek(0)
    read_file = file.read()
    if search_patient_name in read_file:
        print(search_patient_name, "is available")
    else:
        print("Not found")
