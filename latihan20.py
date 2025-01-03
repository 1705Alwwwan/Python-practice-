# Input the interval from the user

lower =  int(input("enter the lower limit of interval : ")) 
upper = int(input("Enter upper limit of  interbal  : ")) 

for numm in range (lower, upper + 1):
    order = len(str(numm))
    temp_num = numm
    sum = 0 
    
    while temp_num > 0 :
        digit = temp_num % 10 
        sum += digit** order
        temp_num //= 10
        
    if numm == sum:
        print (numm) 
    


