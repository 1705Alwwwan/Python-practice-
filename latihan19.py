# implamanted amstrong number with python 
# input the number and determine of amstrong number
num = int(input("Enter the number : ")) 

#manipulate the variable of number 
num_str = str(num)
num_digits = len(num_str)

sum_of_powers = 0 
temp_num = num

#do looping if it's true
while temp_num > 0:
    digit = temp_num % 10 
    sum_of_powers += digit** num_digits 
    temp_num //= 10 

#determine the status of number 
if sum_of_powers == num:
    print (num, f"is an amstrong number")
else:
    print(num,f"is not amstrong number")