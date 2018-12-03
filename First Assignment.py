def question1():
    print("Hello, world!")
    print("Hello", "world!")
    print(3)
    print(3.0)
    print(2+3)
    print(2.0+3.0)
    print("2"+"3")
    print("2+3=", 2+3)
    print(2*3)
    print(2**3)
    print(2/3)
question1()

#question2
def chaosProgramq2():
    #print, eval, input, range, are reserved words for Python
    # for is a coding structure
    print("This program illustrates a chaotic function!")
    x=eval(input("Enter a number between 0 and 1:"))
    for count in range(10):
        x=3.9*x*(1-x)
        print(x)
chaosProgramq2()


#question3
def chaosProgramq3():
    print("This program illustrates a chaotic function!")
    x=eval(input("Enter a number between 0 and 1:"))
    for count in range(10):
        x=2.0*x*(1-x)
        print(x)
chaosProgramq3()
#The difference in results is that while there was much more of a variation between one value to the other when the multiplier was 3.9, but when it became 2.0 the results were much closer.

#question4
def chaosProgramq4():
    #print, eval, input, range, are reserved words for Python
    # for is a coding structure
    print("This program illustrates a chaotic function!")
    x=eval(input("Enter a number between 0 and 1:"))
    for count in range(20):
        x=2.0*x*(1-x)
        print(x)
chaosProgramq4()

#question5
def chaosProgram():
    #print, eval, input, range, are reserved words for Python
    # for is a coding structure
    print("This program illustrates a chaotic function!")
    x=eval(input("Enter a number between 0 and 1:"))
    n=eval(input("How many numbers should I print?"))
    for count in range(n):
        x=2.0*x*(1-x)
        print(x)
chaosProgram()

#question6a
def chaosProgram1():
    #print, eval, input, range, are reserved words for Python
    # for is a coding structure
    print("This program illustrates a chaotic function!")
    x=eval(input("Enter a number between 0 and 1:"))
    for count in range(100):
        x=3.9*x*(1-x)
        print(x)
chaosProgram1()

def chaosProgram2():
    #print, eval, input, range, are reserved words for Python
    # for is a coding structure
    print("This program illustrates a chaotic function!")
    x=eval(input("Enter a number between 0 and 1:"))
    for count in range(100):
        x=3.9*x*(x-x*x)
        print(x)
chaosProgram2()

def chaosProgram3():
    #print, eval, input, range, are reserved words for Python
    # for is a coding structure
    print("This program illustrates a chaotic function!")
    x=eval(input("Enter a number between 0 and 1:"))
    for count in range(100):
        x=3.9*x-3.9*x*x
        print(x)
chaosProgram3()




