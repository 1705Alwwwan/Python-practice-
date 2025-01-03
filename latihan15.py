# input the number and make the variable 
lower = 1
uppor = 10
#print out put statement
print ("print prime numbers between", lower, "and", uppor)

#use the repeatetion for prime number with looping method
for num in range (lower, uppor + 1):
    if num > 1:
        for i in range (2, num): 
            if (num % i) == 0 :
                break
            else:
                print (num) 
                