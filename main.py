import random

print("Вы хотите создать свой пароль или сгенерировать?")
print("Нажмите Y для ввода своего пароля")
print("Нажмите G для генерации пароля:")
answer = input()
big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
small = 'abcdefghijklmnopqrstuvwxyz'
nums = '1234567890'
symbols = '!@#№$%^&?*()~'
str = big + small + nums + symbols

def pass_check(password):
    flag = False
    bigkol = 0
    smallkol = 0
    numkol = 0
    symkol = 0
    for i in range(len(password)):
        if big.find(password[i]) != -1:
            bigkol +=1
        elif small.find(password[i]) != -1:
            smallkol +=1
        elif nums.find(password[i]) != -1:
            numkol +=1
        elif symbols.find(password[i]) != -1:
            symkol +=1
    if bigkol != 0 and smallkol != 0 and numkol != 0 and symkol !=0:
        flag = True
    if flag == False or len(password) < 8:
        return False
    else:
        return True

if answer == 'Y':
    print("Введите Ваш пароль. Минимальная длина 8 символов")
    password = input()
    if pass_check(password) == True:
        print("Пароль достаточно надёжен")
    else:
        password = "-----"
        print('Пароль недостаточно надёжен')
    print("Ваш пароль:" + password)

elif answer == 'G':
    print("Введите длину желаемого пароля:")
    length =int(input())
    password =''
    if length < 8:
        print("Пароль недостаточно надёжен. Минимальная длина - 8 символов")
    else:
        while pass_check(password) != True:
            password = ''
            password = ''.join(random.choice(str) for i in range(length))
        print("Ваш пароль:" + password)
else:
    print("Введите Y для проверки Вашего пароля или G для генерации")