#To print the number from 1 to 10
for i in range(1, 11):
    print(i)

# To print the number from 0 to 10 with the interval of 2
for num in range(0, 11, 2):
    print(num)



# -----------------to print the sum of number from 0 to 100--------------------

total = 0
for number in range(0, 101):
    total += number
print(f"the sum of numbers from 0 to 100 is {total}")
