# While loop that prints 1 to 10
isRunning = True
while isRunning:
    print('Enter a number (1-10) or 0 to exit:')
    number = input()
    if number == '0':
        isRunning = False
    else:
        print('You entered: ' + number)

# While loop that prints a list
nameList = ['Alice', 'Bob', 'Carol']
while len(nameList) > 0:
    print('Enter a name')
    print('The list contains: ' + str(nameList))
    print('Enter 0 to exit')
    name = input()
    if name == '0':
        break
    else:
        nameList.remove(name)
        print('The list now contains: ' + str(nameList))