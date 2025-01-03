# make the factorial method 
#input data 
num = int(input("Enter the number for factorial : "))
factorial = 1 

#proccess and output with the braches method 
if num < 0: 
    print ("factorial doesn't exist for negative number")
elif num == 0:
    print ("factorial of 0 is 1")
#use the looping method for arrage the factroial
else:
    for i in range (1, num+1):
        factorial = factorial * i 
        print ("factorial for", num, "is", factorial)