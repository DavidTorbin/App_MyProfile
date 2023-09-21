# MyProfile app

SEPARATOR = '------------------------------------------'

# user profile # профиль пользователя
user_name = ''
user_age = 0
user_phone = ''
user_mail = ''
index = ''
post_adress = ''
user_unfo = ''

# social links # соц сети, изменить на юр информацию При выборе пункта меню «2 — Информация о предпринимателе» пользователь вводит информацию в следующие поля: ОГРНИП, ИНН,«Расчётный счёт», «Название банка», БИК и «Корреспондентский счёт».При вводе проверьте, что поле ОГРНИП содержит 15 цифр, а расчётный счёт — 20 цифр.
orgnip = ''
inn = ''
checking_accaint = ''
bank_name = ''
bik = ''
correspondent_account = ''


def general_info_user(n_parameter, a_parameter, ph_parameter, e_parameter, index, post_adress, i_parameter):
    print(SEPARATOR)
    print('Имя:    ', n_parameter)
    if 11 <= a_parameter % 100 <= 19:
        years_parameter = 'лет'
    elif a_parameter % 10 == 1:
        years_parameter = 'год'
    elif 2 <= a_parameter % 10 <= 4:
        years_parameter = 'года'
    else:
        years_parameter = 'лет'

    print('Возраст:', a_parameter, years_parameter)
    print('Телефон:', ph_parameter)
    print('E-mail: ', e_parameter)
    print('Почтовый индекс: ', index)
    print('Почтовый адрес: ', post_adress)
    if user_unfo:
        print('')
        print('Дополнительная информация:')
        print(i_parameter)


print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    # main menu главное меню
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    option = int(input('Введите номер пункта меню: '))
    if option == 0:
        break

    if option == 1:
        # submenu 1: edit info
        while True:
            print(SEPARATOR)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Информация о предпринимателе')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                # input general info
                user_name = input('Введите имя: ')
                while 1:
                    # validate user age
                    user_age = int(input('Введите возраст: '))
                    if user_age > 0:
                        break
                    print('Возраст должен быть положительным')

                uph = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                user_phone = ''
                for ch in uph:
                    if ch == '+' or ('0' <= ch <= '9'):
                        user_phone += ch

                user_mail = input('Введите адрес электронной почты: ')
                index = int(input('Введите почтовый индекс: '))
                post_adress = input('Введите почтовый адрес(без индекса): ')
                user_unfo = input('Введите дополнительную информацию:\n')

            elif option2 == 2:
                # input social links
                while 2:
                    ogrnip = input('Введите ОГРНИП: ')
                    ogrnip_summ = len(ogrnip)

                    if ogrnip_summ == 15:
                        break
                    print('ОГРНИП должен содержать 15 цифр!')

                inn = input('Введите ИНН: ')
                while 3:
                    checking_accaint = input('Введите расчетный счет: ')
                    checking_accaint_summ = len(checking_accaint)
                    if checking_accaint_summ == 20:
                        break
                    print('Расчетный счет должен содержать 20 цифр!')
                bank_name = input('Введите название Банка: ')
                bik = input('Введите БИК: ')
                correspondent_account = input('Введите корреспондентский счет: ')
            else:
                print('Введите корректный пункт меню')
    elif option == 2:
        # submenu 2: print info
        while True:
            print(SEPARATOR)
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Общая информация')
            print('2 - Вся информация')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                general_info_user(user_name, user_age, user_phone, user_mail, index, post_adress, user_unfo)

            elif option2 == 2:
                general_info_user(user_name, user_age, user_phone, user_mail, index, post_adress, user_unfo)

                # print social links
                print('')
                print('Информация о предпринимателе')
                print('ОГРНИП:', orgnip)
                print('ИНН: ', inn)
                print('Расчетный счет:   ', checking_accaint)
                print('Название банка: ', bank_name)
                print('БИК: ', bik)
                print('Корреспондентский счет: ', correspondent_account)
            else:
                print('Введите корректный пункт меню')
    else:
        print('Введите корректный пункт меню')