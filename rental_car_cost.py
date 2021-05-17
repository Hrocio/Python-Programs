# function called rental_car_cost with an argument called days
def rental_car_cost(days):
# Every day the car is rented it costs $40
    rental_cost = days * 40
# If the car is rented for 7 or more days, $50 is off the total
    if days >= 7:
        return rental_cost - 50
# If the car is rented for 3 or more days but less than 7, $20 is off the total
    if days >= 3:
        return rental_cost - 20
    return rental_cost
# define rental_car_cost function
def main():
    rentday = input("Please enter how many days you would like to rent the car: ") # User Input
# Conditions
    if rentday.isdigit():
        fee = rental_car_cost(int(rentday))
        print("Your rental cost is: $" + str(fee))
    else:
        print("Incorrect Input.")
if __name__ == '__main__':
    main()