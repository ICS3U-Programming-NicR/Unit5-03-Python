#!/usr/bin/env python3.10

# Created by: Nicolas Riscalas
# Created on: May 9 2022
# calculates the average percentage


def level():
    # define the variables
    counter = 0
    percentage = 0
    while counter < 1:
        mark = input("what was your level on the last assignment: ")
        # convert level to percentage
        match mark:
            case "4++":
                percentage = 100
                break
            case "4+":
                percentage = 97.5
                break
            case "4":
                percentage = 90.5
                break
            case "4-":
                percentage = 83
                break
            case "3+":
                percentage = 78
                break
            case "3":
                percentage = 74.5
                break
            case "3-":
                percentage = 71
                break
            case "2+":
                percentage = 68
                break
            case "2":
                percentage = 64.5
                break
            case "2-":
                percentage = 61
                break
            case "1+":
                percentage = 58
                break
            case "1":
                percentage = 54.5
                break
            case "1-":
                percentage = 51
                break
            case _:
                # check if invalid input
                print("you have to input a level above a level 1- or below a 4++")
    # return the value
    return percentage


def percentage_get():
    while True:
        percentage_str = input("What percentage did you get on this assignment: ")
        # makes sure they input an integer
        try:
            percentage = int(percentage_str)
            # check if below or above 100
            if percentage > 100 or percentage < 0:
                print("you have to input a percentage lower than 100 or higher than 0")
                continue
            break
        except:
            print("you have to input an integer")
    # return value
    return percentage


def fraction_get():
    while True:
        numerator_str = input("Enter the numerator of the fraction: ")
        denominator_str = input("Enter the denominator of the fraction: ")
        # makes sure they input an integer
        try:
            numerator = int(numerator_str)
            denominator = int(denominator_str)
            percentage = (numerator / denominator) * 100
            print(percentage)
            # check if percentage is above 0 and below 100
            if percentage < 0 or percentage > 100:
                print(
                    "You have to input a fraction that has a percentage less than 100 and higher than 0"
                )
                continue
            break
        except:
            print("you have to input an integer")
    # return value
    return percentage


def main():
    while True:
        # define variables
        total_percentage = 0
        counter = 0
        # get variables
        while True:
            type_of_input = input(
                "What type of mark did you get(P for percentage/L for level/F for fraction/C for calculate): "
            )
            # check what type of mark they got
            if type_of_input == "L" or type_of_input == "l" or type_of_input == "level":
                counter += 1
                total_percentage = level() + total_percentage
            elif (
                type_of_input == "P"
                or type_of_input == "p"
                or type_of_input == "percentage"
            ):
                counter += 1
                total_percentage = percentage_get() + total_percentage
            elif (
                type_of_input == "F"
                or type_of_input == "f"
                or type_of_input == "fraction"
            ):
                counter += 1
                total_percentage = fraction_get() + total_percentage
            else:
                break
        if counter > 0:
            # calculate the average
            average_percentage = total_percentage / counter
            print("Your average percentage is {}".format(average_percentage))
        else:
            print(
                "your average_percentage is 0 since you didn't input any valid values"
            )
        # try again loop
        input("If you would like to calculate again just press <enter>: ")


if __name__ == "__main__":
    main()
