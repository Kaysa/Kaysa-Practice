def Weather(temp):
    if temp > 7:
        return "Warm"
    else:
        return "Cold"
user_input = float(input("Enter Temperature:"))
print(Weather(user_input))

