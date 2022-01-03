phone_number = {"John Smith": "+3768299928" , "Marry Simpsons": "+423998200919"}
for key, value in phone_number.items():
    print("%s: %s" %(key, value))

 phone_number = {"John Smith": "+3768299928" , "Marry Simpsons": "+423998200919"}   
    for value in phone_number.values():
        print(value.replace("+", "00"))