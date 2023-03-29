'''
2. 
Write a Python program that calculates a student's grade based on their scores in three different tests. 
The program should prompt the user to enter their scores for each test, and then calculate their average score. 
The program should then assign a letter grade based on the following grading scale:

A: average score >= 90
B: 80 <= average score < 90
C: 70 <= average score < 80
D: 60 <= average score < 70
F: average score < 60
The program should print the average score and letter grade.

Output:
Enter score for test 1: 85
Enter score for test 2: 92
Enter score for test 3: 88
Average score: 88.33
Letter grade: B
'''
def run():
    t1=int(input("Enter score for test 1: "))
    t2=int(input("Enter score for test 2: "))
    t3=int(input("Enter score for test 3: "))
    avg=average(t1,t2,t3)  
    print("Average score: ",avg) # i forgot how to format to two digits we will use something like 0.2f
    g=grade(avg)            
    print("Letter grade: ",g)

def average(t1,t2,t3):  # calculates average and return the result to avg variagle
    avg=(t1+t2+t3)/3
    return avg
def grade(g):       # decides the grade based on the average and returns to g variable
    if g>=90:
        return "A"
    elif g <90 and g>=80:
        return "B"
    elif g<80 and g>=70:
        return "C"
    elif g<70 and g>=60:
        return "D"
    elif g<60:
        return "F"
    
run()