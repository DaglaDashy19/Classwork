#Dec 4, 2018
#Pg. 53, 54 #s 1-4 and Pg 25 #7

def main():
    print("Hello there! Are you in a country that only reports the temperature through Celsius, but you only understand Fahrenheit? Well this is the program for you.")
    print("If you just follow the instructiors that follow, this program will convert the temperature to Fahrenheit")
    celsius=eval(input("What is the Celsius temperature?"))
    fahrenheit=9/5*celsius+32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")

#main()

#avg2.py
# A simple program to average three exam scores
# Illustrates use of multiple input
#def main():
    print("This program computes the average of three exam scores.")

    score1, score2, score3= eval(input("Enter three scores seperated by a comma: "))
    average = (score1 + score2 +score3)/3

    print("The average of the scores is:", average)

#main()

def main():
    print("Hello there! Are you in a country that only reports the temperature through Celsius, but you only understand Fahrenheit? Well this is the program for you.")
    print("If you just follow the instructiors that follow, this program will convert the temperature to Fahrenheit")
    celsius=eval(input("What is the Celsius temperature?"))
    fahrenheit=9/5*celsius+32
for x in range (5):
    celsius=eval(input("What is the Celsius temperature?"))
    fahrenheit=9/5*celsius+32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")

main()

#convert program
def main():
    celsius=eval(input("What is the Celsius temperature?"))
    fahrenheit=9/5*celsius+32
    print("The temperature is", fahrenheit, "degrees Fahrneheit.")

main()


#futuval.py

def main():
    print("This program cslculastes the future value")
    print("of a 10-year investment.")

    principal = eval(input("Enter the initial principal:"))
    apr=eval(input("Enter the annual interest rate: "))
    n=eval(input("Enter the number of years for the investment: "))

    for i in range(n):
        principal=principal *(1+apr)

    print("The value in", n, "years is:", principal)

    main()


