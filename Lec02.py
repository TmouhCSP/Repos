

# first_name = input('Enter your first name :')
# last_name = input('Enter your last name :')
# full_name = first_name + last_name 
# print('welcome',full_name)

                                                            # NOTE
                               # Data Types

# string---> str ---> words
# integer---> int ---> real numbers
# float---> float---> didgits numbers 
# boolean---> bool--->True , False
# list---> list---> ['str',int,float,bool,[list],(tuple)] I Can Modify 
# tuple---> tuple---> ('str',int,float,bool,[list],(tuple)) I Cant Modify it for example (weeks, months, years )
# dictionary---> dict--->{'key':'value' , 'key' : 'value'}


                # Example

# name_string = 'Mohamed'
# print (name_string)
# print(type(name_string))

# num_integer = 55
# print (num_integer)
# print(type(num_integer))

# num_float = 55.233
# print (num_float)
# print(type(num_float))

# x_boolean = True 
# print (x_boolean)
# print(type(x_boolean))

# clint_list = ['omar',28,'data scientist']
# print(clint_list)
# print(type(clint_list))

# clint_tuple = ('omar',28,'data scientist')
# print(clint_tuple)
# print(type(clint_tuple))

# clint_dict = {
#    'name':'ali',
#    'age':'37',
#    'job title':'finance manager'
# }
# print(clint_dict)
# print(type(clint_dict))


                                                            # NOTE
                                    # Converting Data Types 

           # input ----> always be string type  

# name = input ('enter your name :')
# print(name)
# print(type(name))

           # ---->  To convert data type from string to integer do the following 
# age = int(input('enter your age'))
# print(age)
# print(type(age))

           # ---->  To convert data type from string to float do the following 
# num = float(input('enter your num'))
# print(num)
# print(type(num))

           # ---->  To convert data type from list to tuple do the following 
# list = ['str,int,float,boolean]
# x = tuple(list)
# print(x)
# print(type(x))


                                                            # NOTE
                               # Operators Tooles

# + ----> plus mark 
# - ----> minus mark 
# * ----> multiple mark
# / ----> divided mark
# // ---> اقسم وقرب 
# ** ---> exponent mark (POWER)
# % ----> علامة باقي القسمة


                # EXAMPLE

# num_1 = 15
# num_2 = 10

# result = num_1+num_2
# print(result)

# result = num_1-num_2
# print(result)

# result= num_1*num_2
# print(result)

# result = num_1 / num_2
# print (result)

# result = num_1 // num_2
# print (result)

# result = num_1 ** num_2
# print (result)

# result = num_1 % num_2
# print(result)


                                                            # NOTE
                               # Comparable Tooles

# = ----> set mark
# > ----> bigger than
# < ----> smaller than
# >= ---> bigger than and equal
# <= ---> smaller than and equal
# == ---> equal 
# != ---> no equal

                # EXAMPLE

# num_1 = 10
# num_2 = 5

# print(num_1>num_2)
# print(num_1<num_2)
# print(num_1>=num_2)
# print(num_1<=num_2)
# print(num_1==num_2)
# print(num_1!=num_2)


                                                            # NOTE
                                    # IF Role 

      # First Case ( Short IF ) the best and most Fast case 

# print(True) if num_1 > num_2 else print (False)

     # Second Case 
 
# if condition:
#     coding
# else:
#     coding    

      # Third Case  ( adding unlimited elif ) 

# if   ( write condition direct here after if but without brackets) : ------> I can write if only one time 
#     coding
# elif ( write condition direct here after elif but without brackets) : ----> i can write elif  multiple times
#     coding
# else:                                                                 ----> i can write else  only one time
#     coding   


                # EXAMPLE

# num_1 = 55
# num_2 = 5

# print(True) if num_1 > num_2 else print(False)


# if num_1 > num_2 :
#     print(True)
# elif num_1 < num_2 :
#     print(False)
# else:
#     print('numers are equals')


                # Example (Application for Student Degree )

# name = input ('Enter your name :')
# degree = int(input ( "Enter your degree :"))
# print(degree)
# print(type(degree))

# if  degree >= 90 :
#     print('Congratulations', name ,'your Grade is ','Exellent')
# elif   90 > degree >= 80 :
#     print('Congratulations', name ,'your Grade is ','Very Good')
# elif   80 > degree >= 70 :
#     print('Congratulations', name ,'your Grade is ','Good')
# elif   70 > degree >= 50 :
#     print('Congratulations', name , 'you Grade is ','Pass')
# else:
#     print('Unfortunately',   name ,'your Grade is ','Not Pass')


      # IMPORTANT NOTE: if we need to use ( and ) in IF Role Condition we must be sure that the TWO CONDITION are TRUE 

                # EXAMPLE

# num_1 = 5
# num_2 = 10

# if num_1 < num_2 and num_1 != 8 :
#      print(True)
# elif num_1 < num_2 and num_1 == 5:
#      print(True)
# else:
#      print(False)


                # Example (Application for Student Degree ) ( with and -----> be sure that the Two Condition must be done )

# name = input ('Enter your name :')
# degree = int(input ( "Enter your degree :"))
# print(degree)
# print(type(degree))

# if  degree >= 90 :
#     print('Congratulations', name ,'your Grade is ','Exellent')
# elif   degree < 90 and degree >= 80 :
#     print('Congratulations', name ,'your Grade is ','Very Good')
# elif   degree < 80 and degree >= 70 :
#     print('Congratulations', name ,'your Grade is ','Good')
# elif   degree < 70 and degree >= 50 :
#     print('Congratulations', name , 'you Grade is ','Pass')
# else:
#     print('Unfortunately',   name ,'your Grade is ','Not Pass')


      # IMPOTANT NOTE: if we need to use ( or ) in IF Role Condition we must be sure that at least ONE CONDITION is TRUE 

                # EXAMPLE

# num_1 = 5
# num_2 = 10

# if num_1 < num_2 or num_1 != 5 :
#      print(True)
# elif num_1 < num_2 or num_1 == 5:
#      print(True)
# else:
#      print(False)


      # IMPORTANT NOTE: In case we use (if) multiple times it will convert the IF Role to seperet chain of conditions with Seperet Results 

                # Example for multiple (if) ---> each if has seperet Result 

# num_1 = 10
# num_2 = 5

# if num_1 > num_2 :
#     print('x')
# if num_1 > num_2 and num_1 != 6 :
#     print('y')
# if num_1 <= num_2 or num_1 < num_2 :
#     print('z')
# else :
#     print(False)
    

      #IMPORTANT NOTE: In case we use (elif) multiple times it will convert the IF Role to TANGLED Chain with One Result 
#                (steps for chain from top to down and once it get the first true answers its show the result )

                # Example for multiple (elif) ---> only one Result 


# num_1 = 10
# num_2 = 5

# if num_1 < num_2 :
#     print('x')
# elif num_1 > num_2 and num_1 != 6 :
#     print('y')
# elif num_1 >= num_2 or num_1 < num_2 :
#     print('z')
# else :
#     print(False)

