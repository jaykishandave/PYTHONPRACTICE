def string_check(str_value, match_char):

    # if(str_value.count(match_char)>0):
    #     print("True")
    # else:
    #     print("False")

    if str_value.find(match_char) > 0:
        print(str_value.find(match_char))
        print("True")
    else:
        print("False")


str_value = input("Please enter the String: -").upper()
match_char = input("Please enter the char to find:-").upper()
string_check(str_value,match_char)
# print(string_check(str_value,match_char))
