# Calculator with python
# make a fucntion for calculating
# add function
def add(x, y):
    return x + y

# substract function
def substract (x, y):
    return x - y

# multiply function
def multiply (x, y):
    return x * y

# divided function
def divided (x, y):
    return x / y

print ("Select Operation")
print ("1. Add")
print ("2. substract")
print ("3. multiply")
print ("4. divided ")

# use while loop to get the truth 
while True:
    choice = input("Enter the choice 1/2/3/4 : ") #make a variable to determine input
    if choice in ('1', '2', '3', '4'): #use if to determine choice
        try: #input the number
            num1 = float(input("Enter the first number :"))
            num2 =  float(input("Enter the second number"))
        except ValueError: #if doesn't suited number is invalid
            print ("invalid number. Please re-enter number again") 
            continue
        
        if choice == '1': #if it choose 1, use add fucntion
            print(num1, '+', num2, '=', add(num1, num2))
            
        elif choice == '2': #if it choose 2, use subtract function
            print(num1, '-', num2, '=', substract(num1, num2))
            
        elif choice == '3': #if it choose 3, use multiply function
            print(num1, '*', num2, '=', multiply(num1, num2))
            
        elif choice == '4': #if it choose 4, use divided function
            print(num1, '/', num2, '=', divided(num1, num2))
            
        #make variable to choose the choice for breaka nd continue 
        next_calculation = input("do you want to continue the program (yes/no)?")
        if next_calculation == 'no':
            break 
        elif next_calculation == 'yes':
            continue
        else:
            print ('invalid Input')
            break 