largestNum = 0

for i in range(4):
    num = int(input("Number please... "))
    if num > largestNum:
        largestNum = num

print("The largest number is ", str(largestNum) + ".")