# find the greatest and print its index too


l = [15, 100,67, 45, 54]
largest = l[0]
index = 0
for i in range(len(l)):
    if l[i] > largest:
        largest = l[i]
        index = i
    
print(f"your largest number is {largest} at index{index}")