#Weight Converter

weight = float(input("Add your weight: "));
weightType = input("Select your weight type(Kilogram -> K or Pound -> L): ");

if weightType == "k" or weightType == "K":
    weight *=  2.205;
    unit = "LBs"
    print(f"Your weight is {round(weight, 1)} {unit}")
elif weightType == "L" or weightType == "l":
    weight /=  2.205;
    unit = "KGs"
    print(f"Your weight is {round(weight, 1)} {unit}")
else:
    print(f"Weight type {weightType} is invalid")