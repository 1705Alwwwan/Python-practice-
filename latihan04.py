#masukan data awal
a = input("enter the first variable (a) : ")
b = input("enter the second variable (b) : ")
#tampilkan data sementara
print("the original values = ", "a = ", a, "b", b)
#manipulasi data dari data awal
temp = a 
a = b 
b = temp 
#tampilkan data yang termanipulasi 
print("swapped values : ", "a = ", a, "b = ", b)