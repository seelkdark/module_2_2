first = int(input('введите первое число: '))
second = int(input('введите второе число: '))
third = int(input('введите третье число: '))
if  first == second == third:
    print('3')
elif first == second or second == third or first == third:
    print('2')
else:
    print(0)