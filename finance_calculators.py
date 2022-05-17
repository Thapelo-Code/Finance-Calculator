# import math as request by task
# we will be using methematical functions
import math


# create a statement the user will see when the programme runs
# print function will print whats needed to be displayed 
# create a variable for the first statement 
# casefold() implents caseless string matching
# interest should /100 to recognize it as a percentage
menu_selection = input("Choose either 'investment' or 'bond' from the menu below to proceed:\ninvestment - to calculate the amount of interest you'll earn on interest\nbond - to calculate the amount you'll have to pay on a home loan\n - ").casefold()


if menu_selection == 'investment':
    deposit_amount = float(input("Please enter amount you will be depositing :"))
    interest_rate = float(input("Please enter interest rate input earned :  "))/100
    invest_years = int(input("Please enter the number of years you will be investing : "))
    interest = input("Please choose if you want simple or compound interest :").casefold()
    if interest == 'simple':
        simple_interest_total = (deposit_amount) * (1 + interest_rate * invest_years)
        simple_interest_total = round(simple_interest_total,2)
        print(f'The total invest outcome calculated on simple interest is R{simple_interest_total}')
    if interest == 'compound':
        compound_interest_total = round(deposit_amount * math.pow((1 + interest_rate),invest_years),2)
        print(f'The total invest outcome calculated on compound interest is R{compound_interest_total}')

    

# bond calculation 
# divide the interest by 100 then take the variable and divide it by 12 to get monthly interest rate
# round() the answer to the two decimal places 
elif menu_selection == 'bond':
    value_of_house = float(input("Please input value of house: "))
    interest_rate_of_house = float(input("Please enter interest rate of house: "))/100
    interest_rate_of_house = interest_rate_of_house/12
    number_of_months = int(input("Please input the number of months to repay the bond: "))
    monthly_bond_repayments = (interest_rate_of_house * value_of_house) / (1 - math.pow((1 + interest_rate_of_house), - number_of_months ))
    monthly_bond_repayments = round(monthly_bond_repayments,2)
    print(f"The total monthly amount is R{monthly_bond_repayments}")

else:
    print("You did not choose investment or bond: Please select one ")

