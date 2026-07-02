# exception handling

# exception
# error: comes from mistakes

a = int(input("tell your number->"))

try:
    print(10/a)


except Exception as err:
    print(f"sorry there is an err {err}")

else:
    print("good this is no exception")

finally:
    print("I will run no matter what")


