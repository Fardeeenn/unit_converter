# unit converter

def kg_to_gm(kg):
    return kg * 1000

def km_to_miles(km):
    return km * 0.621371

while True:
    option = input("Type 'A' for km to miles, 'B' for kg to grams, or 'quit': ")
    try:
        if option == "quit":
            break
        
        elif option == "A":
            text = input("Enter distance in km: ")
            km = float(text)
            print(f"{km} km = {km_to_miles(km):.2f} miles")
        
        elif option == "B":
            text = input("Enter weight in kg: ")
            kg = float(text)
            print(f"{kg} kg = {kg_to_gm(kg):.0f} grams")
        
        else:
            print("Invalid option. Try again.")
    except ValueError:
        print("pls enter a number")


