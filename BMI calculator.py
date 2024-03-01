def calculate_bmi(weight, height):
    # Calculate BMI using weight (kg) and height (m).
    return weight / ((height / 100) ** 2)

def classify_bmi(bmi):
    # Classify BMI into categories based on predefined ranges.
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def save_to_file(name, weight, height, bmi, category):
    # Save BMI record to a file.
    with open("bmi_records.txt", "a") as file:
        file.write(f"{name},{weight},{height},{bmi},{category}\n")

def main():
    while True:
        try:
            print("\n********************************************")
            print("1. Calculate BMI")
            print("2. Exit")
            print("********************************************")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                name = input("Enter your name: ")  
                weight = float(input("Enter your weight in kilograms: "))  
                height = float(input("Enter your height in centimeters: "))  
                if weight <= 0 or height <= 0:
                    raise ValueError("Weight and height must be positive numbers.")  

                bmi = calculate_bmi(weight, height)  
                category = classify_bmi(bmi)  
                print(f"Your BMI is: {bmi:.2f}")  
                print(f"Category: {category}")  

                save = input("Do you want to save this record? (yes/no): ")  
                if save.lower() == "yes":
                    save_to_file(name, weight, height, bmi, category)  
                    print("Record saved successfully.")
                elif save.lower() == "no":
                    print("Record not saved.")
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
            elif choice == 2:
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError as e:
            print("Invalid input. Please enter valid numbers for weight and height.")  

if __name__ == "__main__":
    main()
