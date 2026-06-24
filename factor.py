n = int(input("which number factor you want->" ))
sum = 0
for i in range(1, n):
    
    if n % i == 0:
        sum = sum + i

if sum == n:
    print("yout number is perfect")
else:
    print("not a perfect number")

