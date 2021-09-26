def FirstName():

    name = input("your name : ")
    MiddleName()

def Yearofbirth():
    Date = int(input("Your year of birth : "))

    #Here it will subtract the current year from your year of birth

    print("You are ", 2021 - Date, "Years old")

def MiddleName():
    Middle = input("your middle name : ")


def main():
    Yearofbirth()

FirstName()

main()