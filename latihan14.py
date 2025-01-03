# seek prime number with the math program
# 1.input varibale 
num = int(input("Enter number : "))

#bool for the statement of unput bariable
flag = False

# 2. proccess "branch choice from input variable"
# if the number equal result with 1
if num == 1:
    print (num, "it's not prime number") #not prime number
# if the number more than 1
elif num > 1:
    #repeat result from 2 till the smae input
    for i in range (2, num):
        if (num % i) == 0: #if input bariable is divided looping and equal 0
            flag = True #even result 0
            break
if flag: 
    print (num,"it's not prime number") #it's not prime result
else:
    print(num, "it's prime number") #other above statement is prime number --
    