# #  write the progrm to print the first 10 natural number 
# print("for loop ")
# for i in range(1,11):
#     print(i)

# num = 1
# print("wHILE LOOP")
# while num <= 10:
#     print(num)
#     num+=1
#  write the progrm to print the first 10 whole  number 
# print("for loop Whole number")
# for i in range(0,10):
#     print(i)

# num = 0
# print("wHILE LOOP whole number ")
# while num < 10:
#     print(num)
#     num+=1

# write the progrm to print the first 10 Even  number 
# print("for loop Even Number  number")
# for i in range(2,22,2):
#     print(i)

# num = 2
# print("wHILE LOOP Even number ")
# while num <= 20:
#     print(num)
#     num+=2
# write the progrm to print the first 10 odd   number 
# print("for loop Even Number  number")
# for i in range(1,20,2):
#     print(i)

# num = 1
# print("wHILE LOOP Even number ")
# while num <= 20:
#     print(num)
#     num+=2

# # Q : 3  write the program to print muliplition table of a given number 
# myNum = int(input("Enter the number : "))
# for i in range(1,11):
#         print(f'{myNum} * {i} = {myNum*i}')

# num = int(input("Enter the number :"))

# myRange = int (input("Enter the range in which i give you prime number "))
# if (myRange == 0 or myRange == 1):
#     print("Not prime number ")
# else:
#     i = 2
#     primeDectector = 0
#     while (i < myRange):
        
#         if (myRange % i == 0 ):
#             primeDectector = primeDectector +1
            
#         i+=1 


# if primeDectector != 0 :
#     print(f'this is {myRange} not  prime number')
# else :

#     print(f'this is {myRange} prime number')


# myRange = int (input("Enter the range in which i give you prime number "))

# for i in range(1,11):
#     if(i == 0 or i ==1):
#         continue
#     else:
#          a = 0
#          primeDect = 0
#          while(a<myRange):
#              if(myRange % i ==0):
#                  ("This is prime number ",i)
#              a+=1
#          else:
#              print("this is not prime number ")
                 
                 
# number = [12,75,150,180,154,525,50]

# for i in number:
#     if(i % 5 ==0):
#         print(i)
#         if(i > 150):
#            continue
#            print("After greater then 150")
#            print(i)
#         if(i>500):
#               break
#               print("After greater then 500")
#               print(i)
# 

# numbers = [12,75,150,180,145,525,50]
# for i in numbers:
#     if i % 5 == 0:
#         if i >= 500:
#           break
#         print(i)
#         if i > 150:
#             continue
        

# gadgets = ["Mobile", "Laptop", 100, "Camera", 310.28, "Speakers", 27.00, "Television", 1000,
#             "Laptop Case", "Camera Lens"]
# strings_list = []
# numbers_list = []
# for item in gadgets:
#     if isinstance(item, str):  
#         strings_list.append(item)
#     elif isinstance(item, (int, float)):  
#         numbers_list.append(item)

# strings_list_sorted_asc = sorted(strings_list)


# strings_list.sort(reverse=True)
# print("Strings List:", strings_list)
# print("Numbers List:", numbers_list)
# print("Sorted Strings in Ascending Order:", strings_list_sorted_asc)
# print("Sorted Strings in Descending Order:", strings_list)

def sum_of_arithmetic_series(a, d, n):

    return (n / 2) * (2 * a + (n - 1) * d)


a = float(input("Enter the first term (a): "))
d = float(input("Enter the common difference (d): "))
n = int(input("Enter the number of terms (n): "))

result = sum_of_arithmetic_series(a, d, n)


print(f"The sum of the first {n} terms of the arithmetic series is: {result}")
