num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))
num3 = int(input("Enter Third Number : "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print (f"The largest number is {largest}")
# f buat nandain kalo string itu formatted string soalnya kalo gapake f di tanda kurung muncul nya largest itu 