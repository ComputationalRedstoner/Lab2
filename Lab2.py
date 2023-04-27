print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
import statistics

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)\nInput: ")
    numbers = input()
    xsplit = numbers.split(",")
    print(xsplit)
    split_numbers = [float(n) for n in xsplit]
    return split_numbers
def calc_average():
    print("calc_average")

def calc_average_temperature(split_numbers):
    i = 0
    total = 0
    for number in split_numbers:
        total = total + float(number)
        i = i + 1
    avgTemp = total/i
    print("Average temperature = " + str(avgTemp))

def calc_min_max_temperature(split_numbers):
    mintemp = min(split_numbers)
    maxtemp = max(split_numbers)
    print("Min temp: " + str(mintemp))
    print("Max temp: " + str(maxtemp))
    split_numbers.sort(reverse=False)
    print(split_numbers)
    return split_numbers

def calc_median_temperature():
    median_temperature = statistics.median(split_numbers)
    print(median_temperature)

split_numbers = display_main_menu()
calc_average_temperature(split_numbers)
calc_min_max_temperature(split_numbers)
calc_median_temperature()