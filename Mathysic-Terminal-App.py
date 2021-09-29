import itertools
import ctypes
import sys
import time
import colorama
from colorama import Fore
import os
colorama.init()

def checkOs():
    os.system("cls" if os.name == "nt" else "clear")

def error_block(query, keyfunc):
    while True:
        try:
            value = keyfunc(input(query))
            return value
        except Exception:
            print('-'*50)
            print("Please enter a correct value")
            print('-'*50)    
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./15)

def veryslowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10./10)


def mainmenu():
    checkOs()
    print(Fore.YELLOW)
    slowprint("\nWelcome to Mathysic!\n\n")
    print(Fore.GREEN)
    print("'0' is for Exit\n")
    print("'1' is for Calculator\n")
    print("'2' is for Physics\n")
    print("'3' is for Mathematics\n")
    print(Fore.CYAN)

    mainchoice = input("Enter your choice: ")

    if mainchoice == "1":
        calculator()
    if mainchoice == "2":
        physic()
    if mainchoice == '3':
        math()
    if mainchoice == "0":
        print(Fore.CYAN)
        veryslowprint("...")
        exit()
    else:
        print(Fore.GREEN)
        print("-" * 50)
        print(Fore.RED)
        slowprint("Wrong argument, please try again.")
        print(Fore.GREEN)
        print("-" * 50)
        time.sleep(5)
        mainmenu()

def calculator():
    checkOs()
    print(Fore.YELLOW)
    print("\nCalculator\n\n")
    
    print(Fore.GREEN)
    calculatorMenu= error_block('\nNow please select the action you want to do:\n''0'' is for Exit\n''1'' is for Addition\n''2'' is for Extraction\n''3'' is for Division \n''4'' is for Multiplication\n\nChoice:'
    , int)
    if calculatorMenu== 0:
        mainmenu()
    elif calculatorMenu == 1:
        addition()
    elif calculatorMenu== 2:
        extraction()
    elif calculatorMenu== 3:
        division()
    elif calculatorMenu==4:
        multiplication()

    else:
        print(Fore.GREEN)
        print("-" * 50)
        print(Fore.RED)
        slowprint("Wrong argument, please try again.")   
        print(Fore.GREEN)
        print("-" * 50)
        time.sleep(5)
        calculator()
    time.sleep(10)
    calculator()

def physic():
    checkOs()
    print(Fore.YELLOW)
    print("Physic calculations")
    print(Fore.GREEN)
    print("'0' is for Exit\n")
    print("'1' is for Volume calculation\n")
    print("'2' is for Energy calculations\n")
    print("'3' is for Temperature converter\n")
    print("'4' is for Mass calculations \n")
    print("'5' is for Pressure calculations \n ")
    print("'6' is for Power calculations\n")
    

    print(Fore.CYAN)
    psychoice = input("Enter your choice: ")

    if psychoice == "1":
        volume()
    if psychoice == "2":
        energyCalculations()
    if psychoice == "3":
        temperatureConverter()
    if psychoice == "4":
        massCalculations()
    if psychoice == "5":
        pressureCalculations()
    if psychoice == "6":
        powerCalculations()
    
        

    if psychoice == "0":
        mainmenu()
    else:
        print(Fore.GREEN)
        print("-" * 50)
        print(Fore.RED)
        slowprint("Wrong argument, please try again.")
        print(Fore.GREEN)
        print("-" * 50)
        time.sleep(5)
        physic()

def math():
    checkOs()
    print(Fore.YELLOW)
    print("\nMathematic calculations\n\n")
    print(Fore.GREEN)
    print("'0' is for Exit\n")
    print("'1' is for Permitation and Combination calculation\n")
    print("'2' is for Factorial calculation\n")
    print("'3' is for Pythagoras Theorem calculation\n")
    print("'4' is for GCD and LCM calculation\n")
    print("'5' is for Length converter (mm, cm, m, km.)\n")
    print("'6' is for Area calculations\n")
    print("'7' is for Square Root calculations\n")
    print("'8' is for Exponential calculations")

    print(Fore.CYAN)
    mathchoice = input("Enter your choice: ")

    if mathchoice == "1":
        permandcomb()
    if mathchoice == "2":
        factorial()
    if mathchoice == "3":
        pythagorasTheorem()
    if mathchoice == "4":
        gcdlcm()
    if mathchoice == "5":
        lconvert()
    if mathchoice == "6":
        area()
    if mathchoice == "7":
        squareroot()
    if mathchoice== '8':
        exponentialCalculations()    
    if mathchoice == "0":
        mainmenu()
    else:
        print(Fore.GREEN)
        print("-" * 50)
        print(Fore.RED)
        slowprint("Wrong argument, please try again.")
        print(Fore.GREEN)
        print("-" * 50)
        time.sleep(5)
        math()

def permandcomb():
    checkOs()
    print(Fore.YELLOW)
    print("'0' is for Exit")
    print("'1' is for Permitation")
    print("'2' is for Combination\n")
    print(Fore.CYAN)
    cpchoice = input("Enter your choice: ")
    if cpchoice == "1":
        permitation()
    if cpchoice == "2":
        combination()
    if cpchoice == "0":
        math()
    else:
        print(Fore.GREEN)
        print("-" * 50)
        print(Fore.RED)
        slowprint("Wrong argument, please try again.")
        print(Fore.GREEN)
        print("-" * 50)
        time.sleep(10)
        permandcomb()

def permitation():
    checkOs()
    print(Fore.YELLOW)
    slowprint("\nPermutation\n\n")
    print(Fore.GREEN)
    writeToList = input(
        "Write the list elements you want ( When typing elements, be careful to leave spaces between the elements! ): ")
    while " " not in writeToList:
        print("-" * 50)
        print(Fore.RED)
        slowprint("Please leave space between elements. Try again.")
        print(Fore.GREEN)
        print("-" * 50)
        writeToList = input(
            "Write the list elements you want ( When typing elements, be careful to leave spaces between the elements! ): ")
    list = writeToList.split(" ")
    perm = itertools.permutations(list)

    for i in perm:
        print(i)

    time.sleep(10)
    permandcomb()

def combination():
    checkOs()
    print(Fore.YELLOW)
    slowprint("\nCombination\n\n")
    print(Fore.GREEN)
    writeToList = input(
        "Write the list elements you want ( When typing elements, be careful to leave spaces between the elements! ): ")
    while " " not in writeToList:
        print("-" * 50)
        print(Fore.RED)
        slowprint("Please leave space between elements. Try again.")
        print(Fore.GREEN)
        print("-" * 50)
        writeToList = input(
            "Write the list elements you want ( When typing elements, be careful to leave spaces between the elements! ): ")
    list = writeToList.split(" ")
    comb = itertools.combinations(list, 2)

    for i in comb:
        print(i)

    time.sleep(10)
    permandcomb()

def factorial():
    checkOs()
    print(Fore.YELLOW)
    slowprint("\nFactorial calculating.\n\n")
    print(Fore.GREEN)
    x = error_block("Factorial number: ", int)
    a = 1
    for i in range(1, x + 1):
        a = a * i
    print(Fore.RED)
    print(str(x) + ' factorial is ' + str(a))

    time.sleep(10)
    math()



def pythagorasTheorem():
    checkOs()
    print(Fore.YELLOW)
    slowprint("\nPythagoras Theorem\n\n")
    print(Fore.GREEN)
    firstSide = error_block("Please enter the first perpendicular side: ", float)
    if firstSide==0:
        mainmenu()                  
    secondSide = error_block("Enter the second perpendicular side: ", int)
    if firstSide==0:
         mainmenu()
              
    total = firstSide ** 2 + secondSide ** 2
    hypotenuse = total ** 0.5
    print(Fore.RED)
    print(f"\nThe hypotenuse is: {hypotenuse}")
    time.sleep(10)
    math()

def gcdlcm():
    checkOs()
    print(Fore.YELLOW)
    print("'0' is for Exit.\n")
    print("'1' is for Lowest Common Multiple\n")
    print("'2' is for Greatest Common Diviser\n")
    print(Fore.CYAN)
    dlchoice = input("Enter your choice: ")
    if dlchoice == "1":
        lcm()
    if dlchoice == "2":
        gcd()
    if dlchoice == "0":
        math()
    else:
        print(Fore.GREEN)
        print("-" * 50)
        print(Fore.RED)
        slowprint("Wrong argument, please try again.")
        print(Fore.GREEN)
        print("-" * 50)
        gcdlcm()


def lcm():
    checkOs()
    print(Fore.YELLOW)
    slowprint("\nLCM\n\n")
    print(Fore.GREEN)
    s1 = error_block("Enter the first number: ", int)
    s2 = error_block("Enter the second number: ",int)
    LCM = s1 * s2
    for number in range(LCM, max(s1, s2) - 1, -1):
        if number % s1 == 0 and number % s2 == 0:
            LCM = number
    print(Fore.RED)
    print(f"{s1} and {s2}'s LCM is {LCM}")
    time.sleep(10)
    gcdlcm()


def gcd():
    checkOs()
    print(Fore.YELLOW)
    slowprint("\nGCD\n\n")
    print(Fore.GREEN)
    s1 = error_block("Enter the first number: ", int)
    s2 = error_block("Enter the second number: ",int)
    eKs = min(s1, s2)
    GCD = 1

    for i in range(1, eKs + 1):
        if s1 % i == 0 and s2 % i == 0:
            GCD = i
    print(Fore.RED)
    print(f"{s1} and {s2}'s GCD is {GCD}")
    time.sleep(10)
    gcdlcm()

def lconvert():
    checkOs()
    print(Fore.YELLOW)
    slowprint("\nLength converter\n\n")
    print(Fore.GREEN + "Use only 'mm', 'cm', 'm', 'km'.")
    print(Fore.YELLOW)
    num1 = error_block('Enter the value: ', float)
    while num1<0:
        print('Length cannot be a negative number. Try again.')
        num1 = error_block('Enter the value: ', float)
    unit1 = input('\nWhich unit do you want it converted from:  ')
    unit2 = input('\nWhich unit do you want it converted to: ')
    

    if unit1 == "mm" and unit2 == "cm":
        ans = num1 / 10
        print(f'{num1} mm = {ans} cm') 
    elif unit1 == "mm" and unit2 == "m":
        ans = num1 / 1000
        print(f'{num1} mm = {ans} m') 
    elif unit1 == "mm" and unit2 == "km":
        ans = num1 / 1000000
        print(f'{num1} mm = {ans} km') 

    
    elif unit1 == "cm" and unit2 == "mm":
        ans = num1 * 10
        print(f'{num1} cm = {ans} mm')  
    elif unit1 == "cm" and unit2 == "m":
        ans = num1 / 100.00
        print(f'{num1} cm = {ans} m')
    elif unit1 == "cm" and unit2 == "km":
        ans = num1 / 100000
        print(f'{num1} cm = {ans} km')
     

    elif unit1 == "m" and unit2 == "mm":
        ans = num1 * 1000
        print(f'{num1} m = {ans} mm') 
    elif unit1 == "m" and unit2 == "cm":
        ans = num1 * 100
        print(f'{num1} m = {ans} cm')
    elif unit1 == "m" and unit2 == "km":
        ans = num1 / 1000
        print(f'{num1} m = {ans} km')
    
    
    elif unit1 == "km" and unit2 == "mm":
        ans = num1 * 1000000
        print(f'{num1} km = {ans} cm')    
    elif unit1 == "km" and unit2 == "cm":
        ans = num1 * 100000
        print(f'{num1} km = {ans} mm')             
    elif unit1 == "km" and unit2 == "m":
        ans = num1 * 1000
        print(ans)
     
    else:
        print(Fore.RED)
        slowprint("Please make sure you entered the correct command.")
        time.sleep(5)     
        lconvert()
    time.sleep(10)
    math()





            

def area():
    checkOs()
    print(Fore.YELLOW)
    print("'0' is for Exit\n")
    print("'1' is for Square\n")
    print("'2' is for Circle\n")
    print("'3' is for Triangle\n")
    print("'4' is for Rectangle")
    print(Fore.GREEN)
    areachoice = input("\nEnter your choice: ")
    
    if areachoice == "0":
        math()
    if areachoice == "1":
        square()
    if areachoice == "2":
        circle()
    if areachoice == "3":
        triangle()
    if areachoice == "4":
        rectangle()
    else:
        print(Fore.GREEN)
        print("-" * 50)
        print(Fore.RED)
        slowprint("Wrong argument, please try again.")
        print(Fore.GREEN)
        print("-" * 50)
        area()

def square():
    checkOs()
    print(Fore.GREEN)
    side1=float(input("Enter the side (cm): "))
    side2=float(input("\nEnter the side (cm): "))
    calc1=side1*side2
    print(Fore.RED)
    print("\nArea of the square is " + str(calc1))
    time.sleep(10)
    area()

def circle():
    checkOs()
    PI = 22/7
    print(Fore.GREEN)
    side1 = float(input("Enter the radius of a circle (cm): "))
    calc2 = PI*side1**2
    print(Fore.RED)
    print("Area of a circle is " + str(calc2))
    time.sleep(10)
    area()

def triangle():
    checkOs()
    print(Fore.GREEN)
    a = float(input("Enter first side (cm): ")) 
    b = float(input("\nEnter second side (cm): "))
    c = float(input("\nEnter third side (cm): "))
    d = (a + b + c) / 2
    calc3 = (d*(d-a)*(d-b)*(d-c)) ** 0.5
    print(Fore.RED)
    print("Area of the triangle is " + str(calc3))
    time.sleep(10)
    area()

def rectangle():
    checkOs()
    print(Fore.GREEN)
    a = float(input('Enter length (cm): '))
    b = float(input('\nEnter breadth (cm): '))
    calc4 = a*b
    print(Fore.RED)
    print("\nArea of the rectangle is " + str(calc4))
    time.sleep(10)
    area()

def squareroot():
    checkOs()
    print(Fore.GREEN)
    a=error_block("Enter the number to take the square root: ", float)
    calc=a**(1/2)
    print(Fore.RED)
    print("Square root is " + str(calc))
    time.sleep(10)
    math()

def exponentialCalculations():
      checkOs()
      print(Fore.YELLOW)
      slowprint("\nExponential Calculations\n\n")
      print(Fore.GREEN)
      
      base=error_block("Enter the base value: ", int)
      upperValue= error_block("Enter the upper value: ",int)
     
         
         
      print("-"*50)
      print(Fore.RED)   
      print(f"Base: {base} \nUpper Value:{upperValue} \n\nResult= {(base)**(upperValue)}")
      time.sleep(10)
    
      math()



def volume():
    checkOs()
    print(Fore.YELLOW)
    print("'0' is for Exit")
    print("'1' is for Cube")
    print("'2' is for Sphere")
    print("'3' is for Clynder")
    print("'4' is for Triangular Prism")
    print("'5' is for Rectangular Prism")
    print(Fore.CYAN)
    choice = input("Enter your choice: ")
    if choice == "1":
        cube()
    if choice == "2":
        sphere()
    if choice == "3":
        cylinder()        
    if choice== "4":
        triangularPrism()
    if choice== "5":
        rectangularPrism()
    if choice == "0":
        physic()
    else:
        print(Fore.GREEN)
        print("-" * 50)
        print(Fore.RED)
        slowprint("Wrong argument, please try again.")
        print(Fore.GREEN)
        print("-" * 50)
        time.sleep(5)
        volume()

def cube():
    checkOs()
    print(Fore.YELLOW)
    slowprint("\nCube\n\n")
    print(Fore.GREEN)
    edge= error_block("Edge size: ", float)
    cubeVolume = edge ** 3
    print(Fore.RED)
    print(f"\nVolume of the cube is {cubeVolume}")
    time.sleep(10)
    volume()

def sphere():
    checkOs()
    print(Fore.YELLOW)
    slowprint("\nSphere\n\n")
    print(Fore.GREEN)
    pi = 22 / 7
    radius = error_block('Radius of sphere: ', float)
    sphereVolume = (4 / 3) * (pi * radius ** 3)
    print(Fore.RED)
    print(f"\nVolume of the sphere is {sphereVolume}")
    time.sleep(10)
    volume()

def cylinder():
    checkOs()
    print(Fore.YELLOW)
    slowprint("\nCylinder\n\n")
    print(Fore.GREEN)
    pi = 22 / 7
    height = error_block('Height of cylinder: ', float)
    radius = error_block('Radius of cylinder: ', float)
    cylinderVolume = pi * radius ** 2 * height
    print(Fore.RED)
    print(f"\nVolume of the cylinder is {cylinderVolume}")
    time.sleep(10)
    volume()

def triangularPrism():
    checkOs()
    print(Fore.YELLOW)
    slowprint("\nTriangular Prism\n\n")
    print(Fore.GREEN)
    baseSide= error_block("Enter the base side of the triangular prysm: ", float)
    height= error_block("Enter the height of the triangular prysm: ", float)
    print(Fore.RED)
    print(f"\nVolume of triangular prism: {baseSide**2*height}")
    time.sleep(10)
    volume()

def rectangularPrism():
    checkOs()
    print(Fore.YELLOW)
    slowprint("\nRectangular Prism\n\n")
    print(Fore.GREEN)
    
    soleEdge1= error_block("Enter the 1st edge of the sole: ", float)
    soleEdge2= error_block("Enter the 2st edge of the sole: ", float)
    height= error_block("Enter the height of the rectangular prism: ", float)
    print(Fore.RED)
    print(f"\nVolume of rectangular prism: {soleEdge1*soleEdge2*height}")
    time.sleep(10)
    volume()

def energyCalculations():
    checkOs()
    print(Fore.YELLOW)
    slowprint("\nEnergy Calculations\n\n")
    print(Fore.GREEN)
    typesOfEnergy= input('"0" is for Exit\n\n"1" is for Potential energy\n\n"2" is for Kinetic energy\n\nChoice: ')
    if typesOfEnergy== "0":
        physic()
    if typesOfEnergy == "1":
        potentialEnergy()
    elif typesOfEnergy == "2":
        kineticEnergy()
    else:
        print(Fore.GREEN)
        print("-" * 50)
        print(Fore.RED)
        slowprint("Wrong argument, please try again.")
        print(Fore.GREEN)
        print("-" * 50)
        time.sleep(5)
        volume()

def potentialEnergy():
    checkOs()
    print(Fore.YELLOW)
    print('\nPotential Energy\n\n')
    print(Fore.GREEN)
    massOfMatter=error_block('Enter the Mass of the Matter (kg):', float)
    gravitationalAcceleration=error_block ('Enter the gravitational acceleration ( m/s²):', float)
    height= error_block('\nEnter the height (m): ', float)
    
    print(f'\nPotential Energy (J): {massOfMatter*gravitationalAcceleration*height} J')
    time.sleep(10)
    energyCalculations()


def kineticEnergy():
    checkOs()
    print(Fore.YELLOW)
    print('\nKinetic energy\n\n')
    print(Fore.GREEN)
    massOfMatter=error_block('Enter the Mass of the Matter (kg):', float)
    velocity=error_block ('Enter the velocity of the matter (km/h):', float)
    print(Fore.RED)
    print(f'\nKinetic Energy (J): {massOfMatter*velocity*1/2} J')
    time.sleep(10)
    energyCalculations()


def temperatureConverter():
       checkOs()
       print(Fore.YELLOW)
       slowprint("\nTempature Converter\n\n")
       print(Fore.GREEN + "Use only 'C', 'K', 'F'.")
       num1 = error_block('Enter the value: ', float)
       unit1 = input('\nWhich unit do you want it converted from:  ')
       unit2 = input('\nWhich unit do you want it converted to: ')

       if unit1 == 'C' and unit2== 'K':
            print(f'{num1} °C = {num1+273.15} °K')
       elif unit1 == 'C' and unit2== 'F':
            print(f'{num1} °C = {num1*9/5+32} °F')
       elif unit1== 'K' and unit2== 'C':
            print(f'{num1} °K = {num1-273.15} °C')
       elif unit1== 'K' and unit2== 'F':
            print(f'{num1} °K = {num1*9/5-459.67} °F')     
       elif unit1 =='F' and unit2== 'C':
           print(f'{num1} °F = {(num1-32)*5/9} °C')
       elif unit1 =='F' and unit2== 'K':
           print(f'{num1} °F = {(num1-32)/1.8000+273.15} °K')  
       elif unit1 == '0' or unit2== '0':
           mainmenu()
   
       else:
           print(Fore.RED)
           slowprint("Please make sure you entered the correct command.")
           time.sleep(5)
           temperatureConverter()
        
       time.sleep(10)
       physic()

def massCalculations():
    checkOs()
    print(Fore.YELLOW)
    slowprint("Mass Calculations\n\n")
    print(Fore.YELLOW + "Use only 'Kg', 'G', 'Mg', 'T (ton)'")
    print(Fore.CYAN)
    num1 = error_block('Enter the value: ', float)
    unit1 = input('\nWhich unit do you want it converted from:  ')
    unit2 = input('\nWhich unit do you want it converted to: ')

    if unit1== 'Kg' and unit2== 'G':
        print(f'{num1} Kg = {num1/0.0010000} g')
    elif unit1== 'Kg' and unit2== 'Mg':
        print(f'{num1} Kg = {num1*1000000} Mg')
    elif unit1== 'Kg' and unit2== 'T':
        print(f'{num1} Kg = {num1/1000} T')

    elif unit1== 'G' and unit2== 'Kg':
        print(f'{num1} g = {num1/1000} Kg')
    elif unit1== 'G' and unit2== 'Mg':
        print(f'{num1} g = {num1*1000} Mg')
    elif unit1== 'G' and unit2== 'T':
        print(f'{num1} g = {num1/1000000 } T') 

    elif unit1== 'Mg' and unit2== 'Kg':
        print(f'{num1} Mg = {num1/1000000} Kg')
    elif unit1== 'Mg' and unit2== 'G':
        print(f'{num1} Mg = {num1/1000 } G')
    elif unit1== 'Mg' and unit2== 'T':
        print(f'{num1} Mg = {num1/1000000000 } T')

    elif unit1== 'T' and unit2== 'Kg':
        print(f'{num1} T = {num1*1000} Kg')
    elif unit1== 'T' and unit2== 'G':
        print(f'{num1} T = {num1*1000000 } G')
    elif unit1== 'T' and unit2== 'Mg':
        print(f'{num1} T = {num1*1000000000 } Mg')                 

    else:
        print(Fore.RED)
        slowprint("Please make sure you entered the correct command.")
        time.sleep(5)
        massCalculations()
              
    time.sleep(10)
    physic()   
    
def pressureCalculations():
       checkOs()
       print(Fore.YELLOW)
       slowprint("\nPressure Calculations\n\n")
       force= error_block("Enter the force value (N): ", float)
       field=error_block("Enter the field value (m²): ", float)
       print(Fore.RED)
       print(f"\nPressure: {force/field}")     
       time.sleep(10)
       physic()
       
       
def powerCalculations():
       checkOs()
       print(Fore.YELLOW)
       slowprint("\nPower Calculations\n\n")
       print(Fore.GREEN)
       workDone=error_block("Enter the value of work done(W): ", float)
       timeİnSeconds= error_block("Enter time value(please enter the time value in seconds (t)): ", float)
       print(Fore.RED) 
       print(f'\nPower (P)= {workDone/timeİnSeconds} P')
       time.sleep(10)
       physic()


   


def addition():
    checkOs()
    print(Fore.YELLOW)
    slowprint("\nAddition\n\n")
    print(Fore.GREEN)
    value= error_block('Enter the first value to here: ', float)
    value2= error_block('Enter the second value to here: ', float)
    print(Fore.RED)
    print(f'\n{value} + {value2} = {value+value2}')
    time.sleep(10)
    calculator()

def extraction():
    checkOs()
    print(Fore.YELLOW)
    slowprint("\nExtraction\n\n")
    print(Fore.GREEN)
    value=error_block ('Enter the first value to here: ', float)
    value2= error_block('Enter the second value to here: ', float)
    print(Fore.RED)
    print(f'\n{value} - {value2} = {value-value2}')
    time.sleep(10)
    calculator()  

def division():
    checkOs()  
    print(Fore.YELLOW)   
    slowprint("\nDivision\n\n")
    print(Fore.GREEN)
    value= error_block('Enter the first value to here: ', float)
    value2=error_block ('Enter the second value to here: ', float)
    while value2==0:
         print('-'*50)
         print('A number cannot be divided by zero. Try again.')
         print('-'*50)
         value2= error_block('Enter the second value to here: ', float)
    print(Fore.RED)
    print(f'\n{value} / {value2} = {value/value2}')
    time.sleep(10)
    calculator()  

def multiplication():
    checkOs()
    print(Fore.YELLOW)
    slowprint("\nMultiplication\n\n")
    value= error_block('Enter the first value to here: ', float)
    value2= error_block('Enter the second value to here: ', float)
    print(Fore.RED)
    print(f'\n{value} * {value2} = {value*value2}')
    time.sleep(10)
    calculator()


mainmenu()