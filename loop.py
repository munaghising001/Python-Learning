#  for Loop


# a = range(1, 20, 1)

# for i in a:
#     print(i)

# reverse loop

# a = range(20, 50, 1)

# for i in a:
#     print(i)

# a = range(16, 1, -1)

# for i in a:
#     print(i)

#  lets print a table of 5

# for i in range(7,71,7):
#   print(i)

# n = int(input("Please enter your table number you want :-"))

# for i in range(n,(n*10)+1,n):
#     print(i)  

# a = "Muna reveive USA Visa"
# for i in range(len(a)):
#   print(a[i])

# a ="Muna is COOL"

# for i in a:
#     print(i)

# for i in range(1, 21):
#    if i == 15:
#       continue
#    else:
#       print(i)

for i in range(1,21):
 if i == 15:
    print("Break statement is executed")
    break
 print(i)

else:
   print("Break statement is not executed")