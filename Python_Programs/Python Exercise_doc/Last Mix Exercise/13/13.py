from Hospital_pass import *

if __name__ == '__main__':

    hg = hospital_gate()
    flag = False
    while True:

        print("1: Doctor")
        print("2: Patient")
        print("3: Relatives")
        print("4: Exit")

        who = (input("Enter who you are (Doctor/Patient/Relative):--")).title()

        if who == "4" or who == "Exit":
            print("Thank you for using the services.......")
            break
        if who == "1" or who == "Doctor":
            hg.doctor_fun()
        elif who == "2" or who == "Patient":
            hg.patient_fun()
        elif who == "3" or who == "Relative":
            hg.relatives_fun()
        else:
            print("Invalid Input")

        while True:
            another_entry = input("Would you like to continue? Y/N:--").upper()
            if another_entry == "Y":
                pass
                break
            elif another_entry == "N":
                flag = True
                print("Thank you for using the services.......")
                break
            else:
                print("Please Enter the valid input.....")
        if flag:
            break


