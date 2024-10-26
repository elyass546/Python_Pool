def main():
    # Inputs: heights in cm and weights in kg

    height = [2.71, 1.15, 123]     # Use heights in m
    weight = [165.3, 38.4]    # Use weights in kg

    # Call the function
    bmi = give_bmi(height, weight)

    # Print the result
    print(bmi)

    print(apply_limit(bmi, 26))

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:

    # Check if both lists are of the same length
    if len(height) != len(weight):
        print("Height and weight lists must be of the same size.")
        exit()
    
    # Check if all elements in both lists are int or float
    if not all(isinstance(h, (int, float)) for h in height):
        print("All elements in the height list must be either int or float.")
        exit()
    if not all(isinstance(w, (int, float)) for w in weight):
        print("All elements in the weight list must be either int or float.")
        exit()


    # Calculate the area (height squared)
    height_in_m2 = [m ** 2 for m in height]

    # Calculate BMI
    calculated_bmi = [kg / m2 for kg, m2 in zip(weight, height_in_m2)]

    return calculated_bmi

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    above_limit = [item >= limit for item in bmi]
    return above_limit

if __name__ == "__main__":
    main()