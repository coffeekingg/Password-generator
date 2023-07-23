import random


def pass_check(password):
    big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    small = 'abcdefghijklmnopqrstuvwxyz'
    nums = '1234567890'
    symbols = '!@#№$%^&?*()~'
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

def btm_check():
    password = str(loginInput.get())
    if pass_check(password) == True:
        logoutOutput['text'] ="Пароль достаточно надёжен"
    else:
        password = "-----"
        logoutOutput['text'] ='Пароль недостаточно надёжен'
    logoutRez['text'] = "Ваш пароль:" + password

def btm_gen():
    big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    small = 'abcdefghijklmnopqrstuvwxyz'
    nums = '1234567890'
    symbols = '!@#№$%^&?*()~'
    str = big + small + nums + symbols
    length = 8
    password =''
    #if length < 8:
    #    logoutOutput['text'] ="Пароль недостаточно надёжен. Минимальная длина - 8 символов"
    #else:
    while pass_check(password) != True:
        password = ''
        password = ''.join(random.choice(str) for i in range(length))
    logoutOutput['text'] = 'Генерация завершена'
    logoutRez['text'] = f"Ваш пароль:{password}"


from tkinter import *

root = Tk()


root.title("Генератор паролей")
root.geometry("700x450+700+290")
root.resizable(True, True)



frame = Frame(root, bg = '#ffb300', bd = 5)
frame.place(relx = 0.1, rely = 0.1, relwidth=0.8, relheight=0.5)

title = Label(frame, text = "Вы хотите проверить свой пароль или сгенерировать?\n"
                            "Для проверки введите пароль и нажмите кнопку\n"
                            "Для генерации введите длину и нажмите кнопку\n"
                            "Минимальная длина пароля 8 символов"

                           , bg = "white", font = 40, relief = RAISED)
title.place(x = 70, y = 10)

frame2 = Frame(root, bg = '#ffb700', bd = 5)
frame2.place(relx = 0.1, rely = 0.7, relwidth= 0.8, relheight=0.25)

loginInput = Entry(frame, bg ='white')
loginInput.place(x = 170, y = 175,  width=170)

logoutOutput = Label(frame2, text = 'Результаты проверки / генерации пароля', font = 40, width=40, height=3, relief = RAISED)
logoutOutput.pack()

logoutRez = Label(frame2, text = 'Пароль', font = 40, width=40, height=3, relief = RAISED)
logoutRez.pack()

btn1 = Button(frame, text = "Проверить пароль", font = 40, command = btm_check() )
btn1.place(x = 70, y = 115, width= 200)

#btn2 = Button(frame, text = "Сгенерировать пароль", font = 40, command = btm_gen() )
#btn2.place(x = 290, y = 115)

root.mainloop()