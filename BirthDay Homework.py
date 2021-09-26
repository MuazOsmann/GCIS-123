
CurrentYear = int(input("Please Enter current Year : "))
CurrentMonth = int(input("Please enter the number of current month : "))
YearofBirth = int(input("Please enter your year of birth : "))
MonthofBirth = int(input("Please enter your Month of birth : "))

Year = (CurrentYear - YearofBirth)*12
Month = (CurrentMonth - MonthofBirth)
Months = (Year + Month)
print("Your age in months is ", Months)