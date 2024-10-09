'''
    Lesson: If Statements
    Author: Mr. Kalisz
    Date Created: October 9, 2024
    Date Last Modified: October 9, 2024
'''

#If statements

#condition -> boolean

num = int(input("Input an integer: "))

#if <condition>:
if num < 6:
    #Code that runs when the if statement is true is indent in once
    #This code is skipped when the condition is false
    print("The number you provided was less than 6")
    num = num + 5

if num > 6:
    print("The number you provided was greater than 6")
    num = num - 5

    
#Code you don't want to part of othe if statement is unindented
print("This will always run")
print(num)