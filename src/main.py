import os
import sys
import time

# ----------------------------------------------- Переменные

login = 'guse'
password = '123'
Balance = 1000

#------------------------------------------------ Все функции

def clear_screen(): #---------------------------- Функция очистки экрана
    os.system('cls' if os.name == 'nt' else 'clear')

def main_add_funds(cash): #---------------------- Функция пополнения баланса
    global Balance
    print('Пополняю баланс...')
    time.sleep(1)
    Balance += cash
    print('Баланс пополнен!')
    input('Нажмите на любую клавишу что бы продолжить')
    clear_screen()

def main_hint_menu(): #-------------------------- Функция подсказок
    clear_screen()
    print('-----ОСОБАЯ ПАНЕЛЬ ПОДСКАЗОК-----')
    print(f'Логин - {login}')
    print(f'Пароль - {password}')
    input('Нажмите любую клавишу для выхода.')
    clear_screen()

def main_option_menu(): #------------------------ Функция выбора действий
    clear_screen()
    while True:
        print('-----ТЕРМИНАЛ БАНКА GUSE-----')
        print(':: Выберите действие')
        print('[1] Проверить баланс')
        print('[2] Пополнить баланс')
        print('[3] Вывести деньги')
        print('[4] Выход')
        print('-----------------------------')
        action = input('>')
        if action == '1':
            main_first_option()
        elif action == '2':
            main_second_option()
        elif action == '3':
            main_third_option()
        elif action == '4':
            main_fourth_option()
        else:
            print('ОШИБКА - Неверное действие')
            time.sleep(1)
            clear_screen()

def main_first_option(): #----------------------- Функция проверки баланса(1 действие)
    clear_screen()
    while True:
        print('-----ПРОВЕРКА БАЛАНСА-----')
        print(f'Текущий баланс - {Balance}₽')
        input('Нажмите любую клавишу для выхода.')
        clear_screen()
        break

def main_second_option(): #---------------------- Функция пополнения баланса(2 действие)
    clear_screen()
    global Balance
    while True:
        print('-----МЕНЮ ПОПОЛНЕНИЯ БАЛАНСА-----')
        print(':: Меню быстрых опций')
        print('[1] 50₽')
        print('[2] 100₽')
        print('[3] 250₽')
        print('[4] 500₽')
        print('[5] 1000₽')
        print('[6] Своя сумма')
        print('[7] Выход')
        print('Выберите действие')
        balance_check = input('>')
        if balance_check == '1':
            main_add_funds(50)
            break
        elif balance_check == '2':
            main_add_funds(100)
            break
        elif balance_check == '3':
            main_add_funds(250)
            break
        elif balance_check == '4':
            main_add_funds(500)
            break
        elif balance_check == '5':
            main_add_funds(1000)
            break
        elif balance_check == '6':
            print('Ведите свою сумму:')
            your_own_number = input('>')
            if not your_own_number.isdigit():
                print('ОШИБКА - Введите числа, НЕ буквы')
                time.sleep(1)
                clear_screen()
                continue
            elif int(your_own_number) >= 10000:
                print('Требуется подтверждения логина и пароля')
                yon_login_check = input('Логин>')
                yon_passwrd_check = input('Пароль>')
                if yon_passwrd_check != password or yon_login_check != login:
                    print('ОШИБКА - Неверный логин или пароль')
                    print('Дать подсказку? (y/n)')
                    yon_podskazka_check = input('>')
                    if yon_podskazka_check == 'y':
                        clear_screen()
                        print('-----ОСОБАЯ ПАНЕЛЬ ПОДСКАЗОК-----')
                        print(f'Логин - {login}')
                        print(f'Пароль - {password}')
                        input('Нажмите любую клавишу для выхода.')
                        clear_screen()
                        continue
                    elif yon_podskazka_check == 'n':
                        clear_screen()
                        continue
                    else:
                        print('ОШИБКА - Неверное действие')
                        time.sleep(1)
                        clear_screen()
                        break

                elif yon_login_check == login and yon_passwrd_check == password:
                    print('Пополняю баланс...')
                    time.sleep(1)
                    Balance += int(your_own_number)
                    print('Баланс пополнен!')
                    input('Нажмите любую клавишу что бы продолжить')
                    clear_screen()
                    break

            else:
                print('Пополняю баланс...')
                time.sleep(1)
                Balance += int(your_own_number)
                print('Баланс пополнен!')
                input('Нажмите любую клавишу что бы продолжить')
                clear_screen()
                break

        elif balance_check == '7':
            clear_screen()
            break
        else:
            print('ОШИБКА - Неверное действие')
            time.sleep(1)
            clear_screen()
            continue

def main_third_option(): #----------------------- Функция вывода средств(3 действие)
    clear_screen()
    global Balance
    while True:
        print('-----ПАНЕЛЬ ВЫВОДА СРЕДСТВ -----')
        print('[1] Ввести сумму для вывода средств')
        print('[2] Вывести все деньги')
        print('[3] Выход')
        cash_out_option = input('>')
        if cash_out_option == '1':
            print('Введите сумму')
            cash_out_custom =  input('>')
            if not cash_out_custom.isdigit():
                print('ОШИБКА - Введите числа, НЕ буквы')
                time.sleep(1)
                clear_screen()
                continue
            elif int(cash_out_custom) > Balance:
                print('ОШИБКА - Недостаточно средств')
                time.sleep(1)
                clear_screen()
                continue
            elif int(cash_out_custom) >= 10000:
                print('Требуется подтверждения логина и пароля')
                coc_login_check = input('Логин>')
                coc_passwrd_check = input('Пароль>')
                if coc_passwrd_check != password or coc_login_check != login:
                    print('ОШИБКА - Неверный логин или пароль')
                    print('Дать подсказку? (y/n)')
                    coc_podskazka_check = input('>')
                    if coc_podskazka_check == 'y':
                        main_hint_menu()
                        continue
                    elif coc_podskazka_check == 'n':
                        clear_screen()
                        continue
                    else:
                        print('ОШИБКА - Неверное действие')
                        time.sleep(1)
                        clear_screen()
                        break

                else:
                    print('Вывожу средства...')
                    time.sleep(1)
                    Balance -= int(cash_out_custom)
                    print('Средства выведены!')
                    input('Нажмите любую клавишу что бы продолжить')
                    clear_screen()
                    break

            else:
                print('Вывожу средства...')
                time.sleep(1)
                Balance -= int(cash_out_custom)
                print('Средства выведены!')
                input('Нажмите любую клавишу что бы продолжить')
                clear_screen()
                break

        elif cash_out_option == '2':
            print('Требуется подтверждения логина и пароля')
            copt_login_check = input('Логин>')
            copt_passwrd_check = input('Пароль>')
            if copt_passwrd_check != password or copt_login_check != login:
                print('ОШИБКА - Неверный логин или пароль')
                print('Дать подсказку? (y/n)')
                copt_podskazka_check = input('>')
                if copt_podskazka_check == 'y':
                    main_hint_menu()
                    continue
                elif copt_podskazka_check == 'n':
                    clear_screen()
                    continue
                else:
                    print('ОШИБКА - Неверное действие')
                    time.sleep(1)
                    clear_screen()
                    break

            else:
                print('Вывожу средства...')
                time.sleep(1)
                Balance -= Balance
                print('Средства выведены!')
                input('Нажмите любую клавишу что бы продолжить')
                clear_screen()
                break

        elif cash_out_option == '3':
            clear_screen()
            break
        else:
            print('ОШИБКА - Неверное действие')
            time.sleep(1)
            clear_screen()
            break

def main_fourth_option(): #---------------------- Функция выхода из терминала(4 действие)
    sys.exit()

#------------------------------------------------ WELCOME-Панель(изначально врубается)

while True:
    print('-----ТЕРМИНАЛ БАНКА GUSE-----')
    print('Введите логин и пароль')
    while True:
        login_check = input('Логин>')
        passwrd_check = input('Пароль>')
        if passwrd_check != password or login_check != login:
            print('ОШИБКА - Неверный логин или пароль')
            print('Дать подсказку? (y/n)')
            podskazka_check = input('>')
            if podskazka_check == 'y':
                main_hint_menu()
                break
            elif podskazka_check == 'n':
                clear_screen()
                break
            else:
                print('ОШИБКА - Неверное действие')
                time.sleep(1)
                clear_screen()
                break

        else:
            main_option_menu()