'''
3.
Write a Python program that calculates the factorial of a given integer. 
The factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. 
For example, 5! = 5 x 4 x 3 x 2 x 1 = 120.

The program should prompt the user to enter a non-negative integer, and then calculate its factorial. 
The program should handle invalid input gracefully by displaying an error message and asking the user to enter a valid input.

Sample Output:
Enter a non-negative integer: 5
The factorial of 5 is 120.

'''

def factorial(n):
    if n>=0:  # to make sure the number is non negative
            if n==1 or n==0:
                return 0
            else:
                fact=1
                for i in range(n,1,-1):
                    fact*=i
                return fact
    else:
        print("invalid number")


n=int(input("Enter a non-negative integer: "))
f=factorial(n)
print("The factorial of {} is {}.".format(n,f))
