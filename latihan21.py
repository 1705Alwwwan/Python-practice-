#give limit for looping proccess
# input variable 
limit = int(input("Enter the limit : ")) 

#  Initialize the sum
sum = 0

# use for loop
for i in range (1, limit + 1):
    sum += i 
    
    print ("sum of the neutral number", limit, "is", sum)