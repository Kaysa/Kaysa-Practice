def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else
        the_mean =sum(value) / len(value)
    
    return the_mean

student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}
monday_temperature = [ 9.1, 8.8, 9.9]
print(mean(monday_temperature))   