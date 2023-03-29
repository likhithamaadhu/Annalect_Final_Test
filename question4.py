'''
4.
Write a Python program that prompts the user to enter a size for a hexagon, and then prints a hexagon of that size 
using asterisks(*). The program should handle invalid input gracefully by displaying an error message and asking the 
user to enter a valid input.

Example Output:
Enter a size for the hexagon: 4

   *
  * *
 * * *
* * * *
* * * *
 * * *
  * *
   *
'''
def hexagon(n):
    for i in range(n+1):
        for j in range(i):
            print('*'.center(3),end="") # lines 20 to 23 try to print the above triangle
        print()
    for i in range(n+1,1,-1):
        for j in range(i-1):
            print('*'.center(3),end="")  # lines 24 to 27 try to print the above triangle
        print()

n=int(input("Enter a size for the hexagon: "))
hexagon(n)

