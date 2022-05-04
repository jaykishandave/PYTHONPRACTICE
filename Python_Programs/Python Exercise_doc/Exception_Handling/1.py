"""Write a program to verify offer is applicable for user Or not based on below criteria. If any of the criteria
doesn't meet then offer is not applicable for user. Use custom exception and let user know about all criteria in case
user doesn't fall back under. Use custom exception and let user know about result.
1. If user is >= 25 year old.
2.If user is Male.
3. If user family member is less than 5. """

import re


class OfferIsApplicable(Exception):

    def __init__(self, age, gender, family_member):
        # super().__init__(self, age, gender, family_member)
        self.family_member = family_member
        self.gender = gender
        self.age = age


try:
    age = int(input("Please enter your age:--"))
    gender = input("Please enter your gender:--").lower()
    family_member = int(input("Please enter your family member count:--"))

    if age >= 25 and gender == "male" and family_member < 5:
        print("This offer is applicable for you")
    else:
        raise OfferIsApplicable(age, gender, family_member)
except OfferIsApplicable as ae:
    print("This offer is not applicable for you because of {0},{1},{2} ".format(ae.age, ae.gender, ae.family_member))
