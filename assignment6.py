# if - elif ladder

temp = int(input("Write the temperature:->"))

if temp < 0:
    print(" Freezing COld")
elif temp >= 0  and temp < 10 :
    print("Very cold")
elif temp >= 10 and temp < 20 :
   print("cold")
elif temp >= 20 and temp < 30:
 print("Pleseant")
elif temp >= 30 and temp < 40:
  print("Hot")
elif temp >= 40 :
  print("very hot")

else:
   print("Temperatue is very hot ") 