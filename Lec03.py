#    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#                                     >---------------> METHODS USES With STRINGS <---------------< 

#    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////                         (Dont forget to insert Brackets ---()--- after Method)

# 1- To Make The First Letter Capital Use The Method  -----> .capitalize()

# name ='omar'.capitalize()

# print(name)
#                                ********************

# 2- To Make All Letters Capital Use The Method -----> .upper()

# name ='omar'.upper()

# print(name)
#                                ********************

# 3- To Make All Letters Lower Use The Method -----> .lower()

# name ='omar'.lower()

# print(name)
#                                ********************

# 4- To Convert the code to Boolean [true/false] Use The Method -----> .isupper()

# name ='omar'.isupper()

# print(name)
#                                ********************

# 5- To Convert the code to Boolean [true/false] Use The Method -----> .islower()

# name ='omar'.islower()

# print(name)
#                                ********************

# 6- To Convert the code to Boolean [true/false] for one  letter/word    Use The Method -----> .startswith('') 
#                                                for more letters/words  Use The Method -----> .startswith(('','')) Tuple method
# name ='omar'.startswith('m')
# name ='omar'.startswith(('m','o'))

# print(name)
#                                ********************

# 7- To Count something inside the code Use The Method -----> .count('') don't forget the Quotation Marks inside Brackets

# name ='omar ahmed mohamed'.count('m')

# print(name)
#                                ********************

# 8- To Remove The Space inside the code Use The Method -----> .strip()

# name =input('Enter Your Name : ').strip()

# print(name)
#                                ********************

# 9- To Remove letters or words inside the code Use The Method -----> .strip('') 
#                                                 ---> Don't Forget The Quotation Marks Inside Brackets <---

# name =input('Enter Your Name : ').strip('Ali')

# print(name)
#                                ********************

# 10- To Divid The All Sentence to Seperet Words/Letters and Put Them Inside List Use The Method -----> .split() 

# name = 'Omar Mohamed Ahmed'.split()
# print(name)
#                                ********************

# 11- To Remove Letter From The Sentence and Divid the remaining to Seperet Words/Letters and Put Them Inside List Use The Method -----> .split('') 

# name = 'omar mohamed ahmed'.split('r')
# print(name)
# email = input('Enter Your Email Pls :')
# username = email.split('@')
# print(username)
#                                ********************

# 12- To Know the Letter Number in the Word or Sentence Use The Method -----> .index('')

# name = 'Ahmed Mohamed Hassan'.index('d')
#         Ahmed   ---> 01234        In Python we start Counting from zero and include Space in counting 
# print(name)
#                                ********************

# 13- To Replace the Letter in the Word or Sentence with another One Use The Method -----> .replace('','')

# names = 'omar mohamed ahmed'
# names = names.replace('omar','ali')
# print(names)
# 
#                                ********************

# 10- To Divid The All Sentence to Seperet Words/Letters and Put Them Inside List Use The Method -----> .format() 

age = 36
txt = ('my name is joan, and i am {}')
print(txt.format(age))

#    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#                                     >---------------> Len With Strings <---------------<

#    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# 1- To Count All The Letters in the String Word Use The Method -----> print(len()) 

# name = 'Ahmed'
# Index:   01234           -----> Total 5 Letters for Full Word
# print(len(name))
#                                ********************

# 2- To Count All The Letters in the String Sentence Use The Method -----> print(len()) 

# name = 'Ahmed Mohamed Hossam'
#      Ahmed   ---> 01234        In Python we start Counting from zero and include Space in counting 
#      space   ---> 5
#      Mohamed ---> 6789101112
#      space   ---> 13
#      Hossam  ---> 141516171819
# Index:012345678910111213141516171819  -----> Total 20 Letters for Full Sentence

# print(len(name))
#                                ********************

#   /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#                                     >---------------> Slicing With Strings <---------------<

#   /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# FIRST CASE -----> 
#                 IF We Use The Index Number from LEFT To RIGHT Including Space So the Method Will be -----> [start:end] <-----
#                     (Dont forget to insert Brackets ---[Start:End]--- after Code)
#              [Start with letter number : End with letter number + 1 ]----> ( Dont Forget to Count Space Between Words )

# name = 'AHMED ALI' 
# Index No:01234 5 678 

# 1- To Slicing The All letters So the Method Will be [start:end] -----> [:]
# name = 'Ahmed Ali'
# print(name[:])
#                                ********************

# 2- To Slicing the letter (D) ----> the index Is Number 4 <---- So the Method Will be [start:end] -----> [4 : 4+1=5]
#                                               OR Write The Index Number Direct [4]                                        
# name = 'AHMED ALI' 
# print(name[4:5])
# print(name[4])
#                                ********************

# 3- To Slicing the letters ( ED AL) ----> The Index Is Numbers 34567 <---- So the Method Will be [start:end] -----> [3 : 7+1=8]
# name = 'AHMED ALI' 
# print(name[3:8])
#                                ********************

# 4- To Slicing The First Letter So the Method Will be [start] -----> [0]
# name = 'Ahmed Ali'
# print(name[0])
#                                ********************

# 5- To Slicing The Last Letter So the Method Will be [end] -----> [-1]
# name = 'Ahmed Ali'
# print(name[-1])
#                                ********************

# SECOND CASE ----> 
#                If We Use The Index Number from RIGHT to LEFT Including Space So the Method Will be -----> [ - start: - end: - step] <-----

# name = 'AHMED ALI' 
# Index No: -9-8-7-6-5 -4  -3-2-1 

# 1- To Slicing The Full Sentence From Right To Left So The Method Will Be [start:end:step] -----> [-1:-10:-1] Or [::-1]

# name = 'Ahmed Ali'
# print(name[-1:-10:-1])
# print(name[::-1])   
#                                ********************

# 2- To Slicing The Letters --->  ALI  <--- From Right To Left So the Method Will be [start:end:step] -----> [-1 : -3+1 : -1] ----> ILA

# name = 'AHMED ALI' 
# print(name[-1:-4:-1])
#                                ********************

# 3- To Slicing The Letters ---> MED AL <--- From Right To Left So the Method Will be [start:end:step] -----> [-2 : -7+1 : -1] ----> LA DEM

# name = 'AHMED ALI' 
# print(name[-2:-8:-1])
#                                ********************

#        >>>>>============================================================================================================================<<<<<
#        >>>>>============================================================================================================================<<<<<

#   /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#                                     >---------------> LEN WITH LIST <---------------<

#   /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# To Count All The words in the List Sentence Use The Method -----> print(len()) 

# name =['Omar','Heba','Ali','Abdulelrahman']
# Index: 0      1      2          3               -----> Total 4 words for Full Sentence

# print(len(name))
#                                ********************

#    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#                                     >---------------> METHODS USES With LIST <---------------< 

#    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////                         (Dont forget to insert Brackets ---()--- after Method)

# 1- To Add String to The End of List Use The Method  -----> .append('Str')
# names = ['Omar','Heba','Ali','Abdulelrahman']
# names.append('Mostafa')
# print(names)
#                                ********************

# 2- To Add List to The End of List Use The Method -----> .append([1,2,3,4])
# names = ['omar','heba','ali','abdulelrahman']
# names.append(['ahmed','mona'])
# print(names)
#                                ********************

# 3- To Add String Before Specific Index Inside The List Use The Method -----> .insert(should write index No here , 'Str')
# names = ['omar','heba','ali','abdulelrahman']
# names.insert(0,'Ahmed')
# print(names)
#                                ********************

# 4 To Replece or Change String Instad of Specific Index Inside The List Use The Method -----> 
# names = ['omar','heba','ali','abdulelrahman']
# names[2] = ('ahmed')
# print(names)
#                                ********************

# 5- To Add List Before Specific Index Inside The List Use The Method -----> .insert(should write index No here , 'Str')
# names = ['omar','heba','ali','abdulelrahman']
# names.insert(0,['Mr Ahmed',1,2,3,4,5])
# print(names)
#                                ********************

# 5- To Copy The List Use The Method -----> .copy() -----> we can use this method before any new modifications to keep the original code safe
# names = ['omar','heba','ali','abdulelrahman']
# x = names.copy()
# print(names)
#                                ********************

# 6- To Clear The List Use The Method -----> .Clear()
# names = ['omar','heba','ali','abdulelrahman']
# names.clear()
# print(names)
#                                ********************

# 7- To Delete The Last Index Inside The List Use The Method  -----> .pop() ----->  only for last index
#    To Delete Specific Index Inside The List Use The Method  -----> .pop() -----> should write the specific index Number inside the Brackets tp deleteit 
# names = ['Omar','Heba','Ali','Abdulelrahman']
# names.pop()
# names.pop(0)
# print(names)
#                                ********************
#   /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#                                     >---------------> Slicing With List <---------------<

#   /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# FIRST CASE -----> We Use The Index Number from LEFT To RIGHT So the Method Will be -----> [start:end] <-----
#                                [Start with String number : End with String number + 1 ]

# names = ['omar','ali','heba','abdulelrahamn','mohamed','mona']
# Index :    0      1     2         3              4       5

# 1- To Slicing The First Index So the Method Will be [start] -----> [0]
# names = ['omar','ali','heba','abdulelrahamn','mohamed','mona']
# print(names[0])
#                                ********************

# 2- To Slicing The Last Index So the Method Will be [end] -----> [-1]
# names = ['omar','ali','heba','abdulelrahamn','mohamed','mona']
# print(names[-1])
#                                ********************

# 3- To Slicing The All List and Delete The Last Index So The Method Will be [start:end] 
# names = ['omar','ali','heba','abdulelrahamn','mohamed','mona']
# names.pop()
# print(names[:])
#                                ********************

# 4- To Slicing Specific Index and Delete The Others From The List So the Method Will be [start:end] -----> [:]
# names = ['omar','ali','heba','abdulelrahamn','mohamed','mona']
# print(names[0:2])
#                                ********************

# 5- To Slicing Specific Index and Delete Specific Index So the Method Will be [start:end] 
# names = ['omar','ali','heba','abdulelrahamn','mohamed','mona']
# names.pop(1)
# names.pop(3)
# print(names[:])
#                                ********************

# SECOND CASE ----> If We Use The Index Number from RIGHT to LEFT So the Method Will be -----> [ - start: - end: - step] <-----

# names = ['omar','ali','heba','abdulelrahamn','mohamed','mona']
# Index :    -6    -5     -4         -3           -2       -1

# 1- To Slicing The Full Sentence From Right To Left So The Method Will Be [start:end:step] -----> [-1:-10:-1] Or [::-1]

# names = ['omar','ali','heba','abdulelrahamn','mohamed','mona']
# print(names[-1:-7:-1])
# print(names[::-1])   
#                                ********************

# 2- To Slicing The All List and Delete Specific Index From Right To Left So the Method Will be [start:end:step] 

# names = ['omar','ali','heba','abdulelrahamn','mohamed','mona']
# names.pop(-3)
# print(names[::-1])
#                                ********************

# 3- To Slicing Specific Index and Delete The Others From Right To Left So the Method Will be [start:end:step] 

# names = ['omar','ali','heba','abdulelrahamn','mohamed','mona']
# print(names[-2:-5:-1])
#                                ********************
#        >>>>>============================================================================================================================<<<<<
#        >>>>>============================================================================================================================<<<<<

#  Simple Progect with Str + List + If : APPLICATION (Welcome Username)

# email = input('Enter your Email pls:').lower().strip()
# print(email)
# username = email.split('@')
# print(username)
# print('Welcome',username[0])
# print('Welcome',username[1])
#                  -----> OR <-----
# email = input('Enter your Email pls:').lower().strip()
# username = email.split('@')[0]
# print('welcome',username)
#                  -----> OR <-----
# email = input('Enter your Email Pls :').strip()
# print('Welcome',email.split('@')[0]) if email.islower() else print('Error Kindly Right Your Email With Small Letter')

#        >>>>>============================================================================================================================<<<<<
#        >>>>>============================================================================================================================<<<<<

#   /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#                                     >---------------> METHODS USES With DICT <---------------<

#   /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
