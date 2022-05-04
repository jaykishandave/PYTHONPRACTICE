currency_dict = {'USD': 'Dollar',
                 'EUR': 'Euro',
                 'GBP': 'Pound',
                 'INR': 'Rupee'}
val_list = list(currency_dict.values())
key_list = list(currency_dict.keys())


def return_key(val):
    for i in range(len(currency_dict)):
        if val_list[i] == val:
            print(key_list[i])
    return "Key Not Found"


return_key("Rupee")
