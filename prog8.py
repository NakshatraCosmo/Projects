n=input("Enter a number:")
try:
    num=int(n)
if num>1:
    for i in range(2,num):
        if num%i == 0:
            print(num, "is not a prime number.")
            break
    else:
        print(num, "is a prime number.")
else:
    print("Enter a number greater than 1.")  

except ValueError:
    print("Please type a number.")      