def mean(value):
    if type(value) == dict:
        
    the_mean = sum(value) / len(value)
    return the_mean

monday_temperature = [ 9.1, 8.8, 7.5, 6.6, 9.9]
student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}
print(mean(student_grades))