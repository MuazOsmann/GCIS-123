def decision(distancee):
    if distancee == 0 or distancee > 15:
    
        print("Print distance if its zero or greter than 15 =", distancee)
    elif distancee > 15 and distancee < 20:
        print("good distance", distancee)
    elif distancee < 15:
        print("Average Distance", distancee) 
    else:
        print("Error 404")

def main():
    distance = int(input("Enter Distance"))
    decision(distance)
    print

main()