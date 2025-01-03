# Febocini sequence 
# input data 
nterms =  int(input("How many terms?"))

#parameter 
n1, n2 =  0, 1
count = 0

#branch of sequence
#if users input 0 
if nterms <= 0:
    print ("please enter number with positive numbers")
#if users inpout 1
elif nterms == 1:
    print ("Febocini sequence up ", nterms, ":")
    print (n1)
#if users input more than 1
else: 
    print ("febocini sequence ")
    while count < nterms: 
        print (n1)
        nth = n1 + n2
        #update values--
        n1 = n2
        n2 = nth
        count += 1 
