#      Numbers in Python 

#      int
# num = 233434 ;
# print(num,type(num))


#      float
# num = 2.4 ;
# print(num,type(num))

#    complex numbers   (real and imaginary)
# num = 2 + 5j
# print(num,type(num))
# print(num.real)
# print(num.imag)

#   negative
# num = -2323 ;
# print(num)


# a = 20 ;
# b = 3 ;
# c = a // b;
# print(c)


#       Type Conversion in Python
# a = "192"
# print(a,type(a))
# a = int("192") 
# print(a)
# a = int(a) + 55
# print(a,type(a))

# a = complex(a)
# print(a,type(a))


    # Inbuilt function for numbers
# x = -2.33
# x = abs(x)
# print(x)

# import math

# x = 10
# x = math.exp(x)
# print(x)

# print(math.pi)

# print(math.sqrt(81))

# print(max(12,3,45,6677,64,3,4233))
# print(min(12,3,45,6677,64,3,4233))


# ------------------------------------------------------


#     Lists     


# num = [23,"A",44,"hey"]
# print(num,type(num))
# print(num[-2]) #  last second will print
# print(num[:3])   # first 3 elements will print
# print(num[2:])    #  elements which remains after 2 elements will print 
# print(num[1:4])     #   elements between 1 and 4 print (4th element is an null element)
# print(num[::3])
# print(num[::-1])   # print the list in reverse order

# mat = [[23,45,33],['er',"t","mike"]]
# print(mat)
# print(mat[1])


#  operation in lists

# z=[0]*100          # to print list with hundred zeros
# print(z) 


# a = ['a','b','c','d']
# b = ['one','two','three','four']
# c = a + b     # it will concatenate the string
# print(c)

# new = list("hey there")    # it will unpack the string
# print(new)

# num = [1,2,3,4]

# one, *other = num ;    # it will stores a single element into single list
# print(one)
# print(other)


#    methods in list

num = [1,2,3,4]
# num.append(6)   # add 6 in the last of list
# print(num)

# stg = ['as','ee','rr']
# num.extend(stg)   # it will add string std in last of string num
# print(num)


# num.insert(1,"newelement")   # it wil add the string add the given index
# print(num)

# num.remove("newelement")
# print(num)

# ll = ['t','y','a','q']
# ll.sort()               # it will sort the list
# print(ll)


# Built-in functions with lists 

x = [9,17,14,4,90,55]

# print(len(x))      # it will show length of the list

# print(min(x))      # it will show min element

# print(max(x))      # it will show max element 

# print(sum(x))      # # it will show sum of element

