
##Obtaining the highest factor, lowest factor, or factor list of any positive integer (the numbers 1, and
## the chosen number will not be included when finding the highest and lowest factor).
print("Welcome!")
num = int(input('Please enter a positive whole number: '))
minimum = 1
numlist = []
for nn in range(minimum, num):
    if num % nn == 0:
        numlist.append(nn)
numlist.append(num)
ll = len(numlist)
if num > 0 and ll > 2:
    numlist.pop(-1)
    maxn = max(numlist)
    numlist.pop(0)
    minn = min(numlist)
    print(f'{num} has been entered.')
    print(f'{num} is not a prime number.')
    print(f"Would you like to see {num}'s 'minimum factor', 'maximum factor', or the 'full list' of {num}'s factors (including 1 and {num})?:")
    option1 = input()
    if option1 == 'minimum' or option1 == 'min' or option1 == 'minimum factor' or option1 == 'min factor':
        print(f'The minimum factor of {num} is {minn}.')
        print(f'Thank you for using this factoring tool!')
    elif option1 == 'maximum' or option1 == 'max' or option1 == 'maximum factor' or option1 == 'max factor':
        print(f'The maximum factor of {num} is {maxn}.')
        print(f'Thank you for using this factoring tool!')
    elif option1 == 'full list' or option1 == 'full' or option1 == 'list':
        numlist.append(1)
        numlist.append(num)
        numlist.sort()
        print(f"The full list of {num}'s factors is {numlist}")
        print(f'Thank you for using this factoring tool!')
elif num == 1 or num == 0:
    print(f'{num} has been entered.')
    print(f'{num} is not a prime number.')
    print(f"Would you like to see {num}'s 'minimum factor', 'maximum factor', or the 'full list' of {num}'s factors?:")
    option1 = input()
    if option1 == 'minimum' or option1 == 'min' or option1 == 'minimum factor' or option1 == 'min factor':
        print(f'The minimum factor of {num} is {num}.')
        print(f'Thank you for using this factoring tool!')
    elif option1 == 'maximum' or option1 == 'max' or option1 == 'maximum factor' or option1 == 'max factor':
        print(f'The maximum factor of {num} is {num}.')
        print(f'Thank you for using this factoring tool!')
    elif option1 == 'full list' or option1 == 'full' or option1 == 'list':
        numlist = [num]
        print(f"The full list of {num}'s factors is {numlist}")
        print(f'Thank you for using this factoring tool!')

elif num > 0 and ll == 2:
    print(f'{num} has been entered.')
    print(f'{num} is a prime number! ')
    print(f'Thank you for using this factoring tool!')
elif num < 0:
    print(f'{num} has been entered.')
    print(f'Error: {num} is not a positive whole number.')
