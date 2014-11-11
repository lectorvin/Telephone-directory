import random
import re
import time

book = [] # database, name < 31, phone < 16, address < 31
n = 0 # кол-во имен в справочнике
# reg.ex. for check numbers: digit + it can be plus in the beginning
p = re.compile('\+?\d+$')
# for check name: letters and one space in the middle
o = re.compile('[a-zA-zа-яА-я]+\s*[a-zA-zа-яА-я]*$')
# for address: numbers or letters
q = re.compile('\w+$')

letters = ['a', 'e', 'i', 'o']
consLet = ['b','c','d','f','k','l','m','n','p','r','s','t']
""" generate random database, which will be in the beginning """
for x in range(random.randint(5, 10)):
    name = chr(random.randint(65, 90)) + (random.choice(letters) +\
        random.choice(consLet)) * random.randint(0, 1)\
        + random.choice(letters) * random.randint(0, 1)\
        + (random.choice(consLet) + random.choice(letters)\
        + random.choice(consLet))\
        * random.randint(0, 1)\
        + random.choice(consLet) + ' ' + chr(random.randint(65, 90))\
        + (random.choice(letters) + random.choice(consLet))\
        * random.randint(0,1)\
        + random.choice(letters) + chr(random.randint(97, 122))
    """ NB! not chr(random.randint(48, 57))*9 because numbers will be same """
    mobile = '+79' + chr(random.randint(48, 57))\
            + chr(random.randint(48, 57)) + chr(random.randint(48, 57))\
            + chr(random.randint(48, 57)) + chr(random.randint(48, 57))\
            + chr(random.randint(48, 57)) + chr(random.randint(48, 57))\
            + chr(random.randint(48, 57)) + chr(random.randint(48, 57))
    home_phone = chr(random.randint(48, 57)) + chr(random.randint(48, 57))\
                + chr(random.randint(48, 57)) + chr(random.randint(48, 57))\
                + chr(random.randint(48, 57)) + chr(random.randint(48, 57))\
                + chr(random.randint(48, 57)) + chr(random.randint(48, 57))
    address = chr(random.randint(65, 90)) + random.choice(letters)\
            + (chr(random.randint(97, 122)) + random.choice(letters)\
            + chr(random.randint(97, 122)))*random.randint(0,1) +\
            (random.choice(letters) + chr(random.randint(97, 122)))\
            * random.randint(0,1) + random.choice(letters)\
            + chr(random.randint(97, 122)) + random.choice(letters)\
            + chr(random.randint(97, 122)) + ' St.'
    book += [[name, mobile, home_phone, address]]
    n += 1


# х1 - name; у1 - max length; u - reg.ex.
# check, if x1 exist, it is less than y1 and it is mathc u,
# and and user to write x1 again if not
def RightLen(x1, y1, u):
    while (not(x1)) or (len(x1) > y1) or (not(u.match(x1))):
        while not(x1):
            x1 = input('Введите хоть что-нибудь!\n')
        while (len(x1) > y1) or (not(u.match(x1))):
            x1 = input('Неправильный формат ввода!\n')
    return x1


# little preview, copied from http://spravkaru.net/names/7/812/list16/
print("""\t\tПофамильный телефонный справочник — это справочник, в котором\n\
    \t\tпредставлен список фамилий.Выбрав интересующую фамилию, можно\n\
    \t\tпросмотреть список людей с такой фамилией, проживающих в данном\n\
    \t\tгороде. Такой справочник полезен, когда нужно найти человека с\n\
    \t\tопределённой фамилией. Именно с помощью такого справочника\n\
    \t\tТерминатор Т-800 нашел Джона Коннора, будущего лидера движения\n\
    \t\tСопротивления и помог ему победить в войне человечества против машин.\n\
    \t\tТакже, с помощью подобного справочника Марти Макфлай нашел Доктора\n\
    \t\tБрауна в 1955, который помог ему восстановить исторический ход\n\
    \t\tсобытий в вернуться в будущее.\n\
    \t\thttp://spravkaru.net/names/7/812/list16/""")
a = input(
"""Добро пожаловать в телефонный справочник!\nДоступные функции:
    0:выход из справочника
    1:вывести весь справочник
    2:добавить новую запись
    3:поиск номера и адреса человека по его имени, адресу, домашнему
    или мобильному номеру
    4:сортировка справочника по имени, мобильному телефону, домашнему
    телефону или адресу
    5:экспорт справочника в файл\n""")
while a != '0':
    if p.match(a): # if a.isnumeric
        # show database, use pheudographic
        if int(a) == 1:
            print('+-----+' + '-'*32 + '+' + '-'*18 + '+' + '-'*17 + '+'
                  + '-'*37 + '+' )
            print('|  №  ' + '|' + '    Name' + ' '*24 + '|' + ' Mobile Phone'
                  + ' '*5 + '|' + '  Home Phone' + ' '*5 + '|' + '    Address'
                  + ' '*26 + '|')
            for x in range(0, n):
                print('+-----+' + '-'*32 + '+' + '-'*18 + '+' + '-'*17 + '+'
                      + '-'*37 + '+')
                if x+1 < 10: # check, if numbers of record has 1,2 or 3 letters
                    print('| ' + str(x+1) + '   |', end='')
                elif x<100:
                    print('| ' + str(x+1) + '  |', end='')
                else:
                    print('| ' + str(x+1) + ' |', end='')
                print(' ' + book[x][0] + ' '*(31-len(book[x][0]))
                    + '| ' + book[x][1] + ' '*(16-len(book[x][1]))
                    + ' | ' + book[x][2] + ' '*(16-len(book[x][2]))
                    + '| '+book[x][3] + ' '*(31-len(book[x][3])) + '     |')
            print('+-----+' + '-'*32 + '+' + '-'*18 + '+' + '-'*17
                                                + '+' + '-'*37 + '+')
        # input new record name, address, phone, and chech them
        elif int(a) == 2:
            # input name
            name=input('Введите имя(не больше 20 символов!)\n')
            f = 0
            while not(f):
                name = RightLen(name, 21, o)
                # check if name is unique
                for x in range(n):
                    if book[x][0] == name:
                        f = 1
                if f:
                    name = input(
"""На ваше имя уже зарегистрирован номер! Введите какое-нибудь другое имя\n""")
                    f = 0
                else:
                    break

            # input mobile number
            mobile = input(
"""Теперь введите мобильный номер (не больше 15 символов!)\n""");
            f = 0
            while (not(f)) and (mobile):
                mobile = RightLen(mobile, 16, p)
                for x in range(n):
                    if book[x][1] == mobile:
                        f = 1
                if f:
                    mobile = input(
"""Этот номер уже занят! Введите какой-нибудь другой номер!\n""")
                    f = 0
                else:
                    break

            # input address
            address=input('Введите свой адрес(не больше 30 символов!)\n')
            address = RightLen(address,31,q)
            y=int(0)
            for x in range(n):
                if book[x][3]==address:
                    y+=1
            # check numbers of people, that wrote this address
            if int(y)>5:
                print(
"""Предупреждаем! На этот адрес зарегистрировано уже слишком много номеров!
Возможно, к вам придут из УФМС!\n""")
                # this function will be written later
                # call_ufms()

            # input home number
            home_phone = input(
"""Теперь введите домашний номер (не больше 15 символов!)\n""");
            f = 0
            while (not(f)) and (home_phone):
                home_phone = RightLen(home_phone, 16, p)
                for x in range(n):
                    if (book[x][2] == home_phone) and (address != book[x][3]):
                        f = 1
                if f:
                    home_phone = input(
                """Этот номер уже занят!Введите какой-нибудь другой номер!\n""")
                    f = 0
                else:
                    break

            # add record in the database
            book += [[name, mobile, home_phone, address]]
            n += 1

        # searching through the database for name, address or phone
        elif int(a) == 3:
            some=input(
"""Введите 1, если хотите осуществить поиск по имени,
2, если хотите осуществить поиск по мобильному номеру,
3, если хотите осуществить поиск по домашнему номеру,
4, если хотите осуществить поиск по адресу\n""")
            # searching for name
            if int(some) == 1:
                name = input('Введите искомое имя\n')
                name = RightLen(name, 21, o)
                f = 0
                for x in range(n):
                    if book[x][0] == name:
                        f = 1
                        print('Номер введенного человека: ',book[x][1],
                            ', его адрес: ', book[x][3],
                            ', его домашний номер: ',book[x][2],'\n')
                if not(f):
                    print('На этого человека не зарегистрирован\
                            ни один номер!\n')
            # searching for mobile
            elif int(some) == 2:
                mobile = input('Введите искомый номер\n')
                mobile = RightLen(mobile, 16, p)
                f = 0
                for x in range(n):
                    if book[x][1] == mobile:
                        f = 1
                        print('Имя владельца номера: ', book[x][0],
                            ', его адрес: ', book[x][3],
                            ', его домашний номер: ',book[x][2],'\n')
                if not(f):
                    print('Этого номера нет в данном справочнике!\n')
            # searching for home phone
            elif int(some) == 3:
                home_phone = input('Введите искомый номер\n')
                home_phone = RightLen(home_phone, 16, p)
                f = 0
                for x in range(n):
                    if book[x][2] == home_phone:
                        f = 1
                        print('Имя владельца номера: ', book[x][0],
                            ', его адрес: ', book[x][3],
                            ', его мобильный номер: ', book[x][1], '\n')
                if not(f):
                    print('Этого номера нет в данном справочнике!\n')
            # searching for address
            elif int(some) == 4:
                address = input('Введите искомый адрес\n')
                address = RightLen(address, 31, q)
                f = 0
                print('По данному адресу проживают:')
                for x in range(n):
                    if book[x][3] == address:
                        f = 1
                        print('+ Владелец: ', book[x][0],
                            ', мобильный номер: ', book[x][1],
                            ', домашний номер; ', book[x][2], '\n')
                if not(f):
                    print('Никто')
        # sort database by name, phone or address
        elif int(a) == 4:
            some = input(
"""Введите 0, если хотите отсортировать справочник по имени,
1, если хотите отсортировать справочник по мобильному номеру,
2, если хотите отсортировать справочник по домашнему номеру,
3, если хотите отсортировать справочник по адресу\n""")
            while ((int(some) != 1) and (int(some) != 2) and
                  (int(some) != 0) and (int(some) != 3)):
                some = input('Пожалуйста, введите 0,1,2 или 3\n')
            y = input(
"""Введите 1, если хотите отсортировать справочник по возрастанию, или
2, если хотите отсортировать справочник по убыванию\n""")
            # check, if user write right number and ask him again if not
            while (int(y) != 1) and (int(y) != 2):
                y = input('Пожалуйста, введите 1 или 2\n')
            # bubble sort
            if int(y) == 1:
                for x in range(0, n-1):
                    for k in range(0, n-x-1):
                        if book[k][int(some)] > book[k+1][int(some)]:
                            (book[k],book[k+1]) = (book[k+1], book[k])
            if int(y) == 2:
                for x in range(0, n-1):
                    for k in range(0, n-x-1):
                        if book[k][int(some)] < book[k+1][int(some)]:
                            (book[k],book[k+1]) = (book[k+1], book[k])
        # export database
        elif int(a) == 5:
            some = input('Введите полный путь к файлу\n')
            while not(some):
                some = input('Введите хоть что-нибудь\n')
            try:
                with open(some,'w') as f:
                    # check, if x has 1, 2 or 3 numbers
                    for x in range(n):
                        if x+1 < 10:
                            f.write(' ' + str(x+1) + '   ')
                        elif x+1 < 100:
                            f.write(' ' + str(x+1) + '  ')
                        else:
                            f.write(' ' + str(x+1) + ' ')
                        f.write(' ' + book[x][0] + ' '*(31-len(book[x][0]))
                            + ' ' + book[x][1] + ' '*(16-len(book[x][1])) + '  '
                            + book[x][2] + ' '*(16-len(book[x][2])) + ' '
                            + book[x][3] + '\n')
                print('Записываю...')
                time.sleep(2)
                print('Готово!\n')
            except IOError:
                print('Неправильный путь!\n')
        elif int(a) == 42: # easter egg
            print(
"""\t\t"Forty-two!" yelled Loonquawl."Is that all you've got to show for
\tseven and a half million years' work?"
\t"I checked it very thoroughly,"said the computer, "and that quite definitelyis
\tthe answer. I think the problem, to be quite honest with you,
\tis that you've never actually known what the question is."
\t"But it was the Great Question! The Ultimate Question of Life, the Universe
\tand Everything!" howled Loonquawl.
\t"Yes," said Deep Thought with the air of one who suffers fools gladly,
\t"but what actually is it?"
\tA slow stupefied silence crept over the men as they stared at the computer
\tand then at each other.
\t"Well, you know, it's just Everything ... Everything ..." offered Phouchg weakly.
\t"Exactly!" said Deep Thought. "So once you do know what the question actually
\tis, you'll know what the answer means."\n""")
        else:
            print('Неизвестная команда!')
    else:
        print('Неизвестная команда!')
    a = input(
"""Желаете выполнить еще какие-нибудь функции?
Доступные функции:
    0:выход из справочника
    1:вывести весь справочник
    2:добавить новую запись
    3:поиск номера и адреса человека по его имени, адресу,
    домашнему или мобильному номеру
    4:сортировка справочника по имени, мобильному телефону,
    домашнему телефону или адресу
    5:экспорт справочника в файл\n""")
print('Good luck!')
