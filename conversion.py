    # Hilda Rocio Martin - 06/13/19 - Exercise 7.1 (conversion.py).
    # Write a program that reads a floating point number using the input() function. Assume this
    # number is in meters and convert it to feet, yards, and miles. Then print each of these three
    # results.

# Program inputs
Meters = float(input("Please type a measurement in meters: "))
# Saving values in variables
Meters_to_Feet = Meters*3.281 # Converts meters to feet
Meters_to_Yards = Meters*1.094 # Converts meters to yards
Meters_to_Miles = Meters*6.214* 10**-4 # Converts meters to miles
# Displaying the results for each conversion
print("The measurement in feet is:\n", Meters_to_Feet)
print("In yards:\n", Meters_to_Yards)
print("In miles:\n", Meters_to_Miles)


    # Live Run
    # (base) C:\Users\hilda\.PyCharmCE2019.1\config\scratches>python3 _conversion.py
    # Please type a measurement in meters: 2
    # The measurement in feet is:
    #  6.562
    # In yards:
    #  2.188
    # In miles:
    #  0.0012428

