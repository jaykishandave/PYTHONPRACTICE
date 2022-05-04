from Hospital_pass import *

hg = hospital_gate()
while True:

    print("1: Doctor")
    print("2: Patient")
    print("3: Relatives")
    print("4: Exit")

    who = (input("Enter who you are (Doctor/Patient/Relative):--"))

    if who == 4:
        print("TATA Good Bye Khatam.......")
        break
    if who == "1" or who == "Doctor":
        hg.doctor_fun()
    elif who == "2" or who == "Patient":
        hg.patient_fun()
    elif who == "3" or who == "Relative":
        hg.relatives_fun()
    else:
        print("Invalid Input")

    another_entry = input("Would you like to continue? Y/N:--").upper()
    if another_entry == "Y":
        pass
    else:
        print("TATA Good Bye Khatam.......")
        break
