def calculate_bmi(Height, Weight):
    print("Height = " + str(Height))
    print("Weight = " + str(Weight))
    #to calculate bmi
    bmi = Weight/(Height*Height)
    print("BMI = " + str(bmi))
    if bmi < 18.5:
        print("You are Under Weight")
    elif bmi >= 18.5 and bmi <= 25:
        print("You are Normal Weight")
    else:
        print("You are Over Weight")

calculate_bmi(Weight=57,Height=1.73)
