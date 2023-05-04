def calculate_bmi(Height, Weight):
    print("Height = " + str(Height))
    print("Weight = " + str(Weight))
    #to calculate bmi
    bmi = Weight/(Height*Height)
    print("BMI = " + str(bmi))
    if bmi < 18.5:
        print("You are Under Weight")
        return -1
    elif bmi >= 18.5 and bmi <= 25:
        print("You are Normal Weight")
        return 0
    else:
        print("You are Over Weight")
        return 1

calculate_bmi(Weight=57,Height=1.73)
