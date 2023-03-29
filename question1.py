'''
1. Temperature Conversion:
Write a Python program that converts temperatures from Celsius to Fahrenheit and vice versa. The program should prompt the user to enter a temperature and whether they want to convert it from Celsius to Fahrenheit or from Fahrenheit to Celsius. The program should then perform the conversion and print the result.
1 celsius = 33.8 Fahrenheit

Sample output:
Enter the temperature: 25
Enter 'C' to convert from Celsius to Fahrenheit, or 'F' to convert from Fahrenheit to Celsius: C
25 degrees Celsius is 77.0 degrees Fahrenheit.
'''

# F = (C × 9/5) + 32
# C = (F − 32) x 5/9
def run():
    n=int(input("Enter a temperature: "))
    choice=input("Enter 'C' to convert from Celsius to Fahrenheit,'F' to convert from Fahrenheit to Celsius: ")
    
    if choice=='C':
        res=fahrenheit(n)           #this method converts celsius temp to fahrenheit temp
        print(n,"degrees celsius is ",res," degrees fahrenheit temperature")
        print("-----------------")
    elif choice=='F':
        res=celsius(n)              #this method converts celsius temp to fahrenheit temp to celsius temp 
        print(n,"degrees celsius is ",res," degrees fahrenheit temperature")
        print("-----------------")
    else:
        print("invalid option")

def fahrenheit(n):
    f=(n*(9/5))+32
    return f

def celsius(n):
    c=(n-32)*5/9
    return c

run()