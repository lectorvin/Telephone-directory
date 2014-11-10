import random
import re
 
book=[] #справочник, name<31, phone<16, address<31
n=0 #кол-во имен в справочнике
p=re.compile('\+?\d+$')
o=re.compile('[a-zA-zа-яА-я]+\s*[a-zA-zа-яА-я]*$')
q=re.compile('\w+$')
letters=['a','e','i','o']
consLet=['b','c','d','f','k','l','m','n','p','r','s','t']
for x in range(random.randint(5,10)): #случайная база данных
    name=chr(random.randint(65,90)) + ( random.choice(letters)+random.choice(consLet) )*random.randint(0,1) + random.choice(letters)*random.randint(0,1) +( random.choice(consLet)+random.choice(letters)+random.choice(consLet) )*random.randint(0,1) + random.choice(consLet)+' '+chr(random.randint(65,90)) + ( random.choice(letters)+random.choice(consLet) )*random.randint(0,1)+random.choice(letters)+chr(random.randint(97,122))
    mobile='+79'+chr(random.randint(48,57))+chr(random.randint(48,57))+chr(random.randint(48,57))+chr(random.randint(48,57))+chr(random.randint(48,57))+chr(random.randint(48,57))+chr(random.randint(48,57))+chr(random.randint(48,57))+chr(random.randint(48,57))
    home_phone=chr(random.randint(48,57))+chr(random.randint(48,57))+chr(random.randint(48,57))+chr(random.randint(48,57))+chr(random.randint(48,57))+chr(random.randint(48,57))+chr(random.randint(48,57))+chr(random.randint(48,57))
    address=chr(random.randint(65,90))+random.choice(letters)+( chr(random.randint(97,122))+random.choice(letters)+chr(random.randint(97,122)) )*random.randint(0,1)+( random.choice(letters)+chr(random.randint(97,122)) )*random.randint(0,1)+random.choice(letters)+chr(random.randint(97,122))+random.choice(letters)+chr(random.randint(97,122))+' St.'
    book+=[[name,mobile,home_phone,address]]
    n+=1
def RightLen(x1,y1,u): #х1 - имя, у1 - макс.длина, проверяет, не ноль ли х1 и меньше ли оно у1, u - формат
    while (not(x1)) or (len(x1)>y1) or (not(u.match(x1))):
        while not(x1):
            x1=input('Введите хоть что-нибудь!\n')
        while (len(x1)>y1) or (not(u.match(x1))):
            x1=input('Неправильный формат ввода!\n')
    return x1
print('\t\tПофамильный телефонный справочник — это справочник, в котором представлен список фамилий. \n\t\tВыбрав интересующую фамилию, можно просмотреть список людей с такой фамилией, \n\t\tпроживающих в данном городе. \n\t\tТакой справочник полезен, когда нужно найти человека с определённой фамилией. \n\t\tИменно с помощью такого справочника Терминатор Т-800 нашел Джона Коннора, \n\t\tбудущего лидера движения Сопротивления и помог ему победить в войне человечества против машин. \n\t\tТакже, с помощью подобного справочника Марти Макфлай нашел Доктора Брауна в 1955, \n\t\tкоторый помог ему восстановить исторический ход событий в вернуться в будущее.\n\t\thttp://spravkaru.net/names/7/812/list16/')
a=input('Добро пожаловать в телефонный справочник!\nДоступные функции:\n0:выход из справочника\n1:вывести весь справочник\n2:добавить новую запись\n3:поиск номера и адреса человека по его имени, адресу, домашнему или мобильному номеру\n4:сортировка справочника по имени, мобильному телефону, домашнему телефону или адресу\n5:экспорт справочника в файл\n')
while a!='0':
    if p.match(a): #if a.isnumeric
        if int(a)==1: #вывод всей таблицы
            print('+-----+'+'-'*32+'+'+'-'*18+'+'+'-'*17+'+'+'-'*37+'+')
            print('|  №  '+'|'+'    Name'+' '*24+'|'+' Mobile Phone'+' '*5+'|'+'  Home Phone'+' '*5+'|'+'    Address'+' '*26+'|')
            for x in range(0,n):
                print('+-----+'+'-'*32+'+'+'-'*18+'+'+'-'*17+'+'+'-'*37+'+')
                if x+1<10:
                    print('| '+str(x+1)+'   |',end='')
                elif x<100:
                    print('| '+str(x+1)+'  |',end='')
                else:
                    print('| '+str(x+1)+' |',end='')
                print(' '+book[x][0]+' '*(31-len(book[x][0]))+'| '+book[x][1]+' '*(16-len(book[x][1]))+' | '+book[x][2]+' '*(16-len(book[x][2]))+'| '+book[x][3]+' '*(31-len(book[x][3]))+'     |')
            print('+-----+'+'-'*32+'+'+'-'*18+'+'+'-'*17+'+'+'-'*37+'+')
        elif int(a)==2: #добавление новой записи
    #Ввод имени, проверка его на длину и уникальность
            name=input('Введите имя(не больше 20 символов!)\n')
            f=0
            while not(f):
                name=RightLen(name,21,o)
                for x in range(n):
                    if book[x][0]==name:
                        f=1
                if f:
                    name=input('На ваше имя уже зарегистрирован номер! Введите какое-нибудь другое имя\n')
                    f=0
                else:
                    break
    #Ввод мобильного номера, проверка его на длину и уникальность
            mobile=input('Теперь введите мобильный номер(не больше 15 символов!)\n');
            f=0
            while (not(f)) and (mobile):
                mobile=RightLen(mobile,16,p)
                for x in range(n):
                    if book[x][1]==mobile:
                        f=1
                if f:
                    mobile=input('Этот номер уже занят! Введите какой-нибудь другой номер!\n')
                    f=0
                else:
                    break
    #Ввод адреса, проверка, не живет ли там семья таджиков
            address=input('Введите свой адрес(не больше 30 символов!)\n')
            address=RightLen(address,31,q)
            y=int(0)
            for x in range(n):
                if book[x][3]==address:
                    y+=1
            if int(y)>5:
                print('Предупреждаем! На этот адрес зарегистрировано уже слишком много номеров! Возможно, к вам придут из УФМС!\n')
                #call_ufms()
    #Ввод домашнего номера, проверка его на длину и уникальность
            home_phone=input('Теперь введите домашний номер(не больше 15 символов!)\n');
            f=0
            while (not(f))and(home_phone):
                home_phone=RightLen(home_phone,16,p)
                for x in range(n):
                    if (book[x][2]==home_phone)and(address!=book[x][3]):
                        f=1
                if f:
                    home_phone=input('Этот номер уже занят! Введите какой-нибудь другой номер!\n')
                    f=0
                else:
                    break
                
            book+=[[name,mobile,home_phone,address]]
            n+=1
        elif int(a)==3: #поиск
	#поиск по имени
            some=input('Введите 1, если хотите осуществить поиск по имени, 2, если хотите осуществить поиск по мобильному номеру, 3, если хотите осуществить поиск по домашнему номеру, 4, если хотите осуществить поиск по адресу')
            if int(some)==1:
                name=input('Введите искомое имя\n')
                name=RightLen(name,21,o)
                f=0
                for x in range(n):
                    if book[x][0]==name:
                        f=1
                        print('Номер введенного человека: ',book[x][1],', его адрес: ', book[x][3],', его домашний номер: ',book[x][2],'\n')
                if not(f):
                    print('На этого человека не зарегистрирован ни один номер!\n')
	#поиск по мобильному номеру
            elif int(some)==2:
                mobile=input('Введите искомый номер\n')
                mobile=RightLen(mobile,16,p)
                f=0
                for x in range(n):
                    if book[x][1]==mobile:
                        f=1
                        print('Имя владельца номера: ',book[x][0],', его адрес: ', book[x][3],', его домашний номер: ',book[x][2],'\n')
                if not(f):
                    print('Этого номера нет в данном справочнике!\n')
	#поиск по домашнему номеру
            elif int(some)==3:
                home_phone=input('Введите искомый номер\n')
                home_phone=RightLen(home_phone,16,p)
                f=0
                for x in range(n):
                    if book[x][2]==home_phone:
                        f=1
                        print('Имя владельца номера: ',book[x][0],', его адрес: ', book[x][3],', его мобильный номер: ',book[x][1],'\n')
                if not(f):
                    print('Этого номера нет в данном справочнике!\n')
	#поиск по адресу
            elif int(some)==4:
                address=input('Введите искомый адрес\n')
                address=RightLen(address,31,q)
                f=0
                print('По данному адресу проживают:')
                for x in range(n):
                    if book[x][3]==address:
                        f=1
                        print('+ Владелец: ',book[x][0],', мобильный номер: '+book[x][1]+', домашний номер; '+book[x][2],'\n')
                if not(f):
                    print('Никто')
        elif int(a)==4: #сортировка по какому-либо параметру
            some=input('Введите 0, если хотите отсортировать справочник по имени, 1, если хотите отсортировать справочник по мобильному номеру, 2, если хотите отсортировать справочник по домашнему номеру, 3, если хотите отсортировать справочник по адресу \n')
            while (int(some)!=1)and(int(some)!=2)and(int(some)!=0)and(int(some)!=3):
                some=input('Пожалуйста, введите 0,1,2 или 3\n')
            y=input('Введите 1, если хотите отсортировать справочник по возрастанию, или 2, если хотите отсортировать справочник по убыванию\n')
            while (int(y)!=1)and(int(y)!=2):
                y=input('Пожалуйста, введите 1 или 2\n')
            if int(y)==1:
                for x in range(0,n-1):
                    for k in range(0,n-x-1):
                        if book[k][int(some)]>book[k+1][int(some)]:
                            (book[k],book[k+1])=(book[k+1],book[k])
            if int(y)==2:
                for x in range(0,n-1):
                    for k in range(0,n-x-1):
                        if book[k][int(some)]<book[k+1][int(some)]:
                            (book[k],book[k+1])=(book[k+1],book[k])
        elif int(a)==5: #экспорт в файл
            some=input('Введите полный путь к файлу\n')
            while not(some):
                some=input('Введите хоть что-нибудь\n')
            try:
                f=open(some,'a')
            except:
                print('Файл не найден!\n')
                break
            for x in range(n):
                if x+1<10:
                    f.write(' '+str(x+1)+'   ')
                elif x<100:
                    f.write(' '+str(x+1)+'  ')
                else:
                    f.write(' '+str(x+1)+' ')
                f.write(' '+book[x][0]+' '*(31-len(book[x][0]))+' '+book[x][1]+' '*(16-len(book[x][1]))+'  '+book[x][2]+' '*(16-len(book[x][2]))+' '+book[x][3]+' '*(31-len(book[x][3]))+'     \n')
            f.close()
        elif int(a)==42: #типо пасхалка
            print(""" \n"Forty-two!" yelled Loonquawl. "Is that all you've got to show for seven and a half million years' work?"\n"I checked it very thoroughly," said the computer, "and that quite definitely is the answer. I think the problem, to be quite honest with you, is that you've never actually known what the question is."\n"But it was the Great Question! The Ultimate Question of Life, the Universe and Everything!" howled Loonquawl.\n"Yes," said Deep Thought with the air of one who suffers fools gladly, "but what actually is it?"\nA slow stupefied silence crept over the men as they stared at the computer and then at each other.\n"Well, you know, it's just Everything ... Everything ..." offered Phouchg weakly.\n"Exactly!" said Deep Thought. "So once you do know what the question actually is, you'll know what the answer means."\n """)
        else:
            print ('Неизвестная команда!')
    else:
        print ('Неизвестная команда!')
    a=input('Желаете выполнить еще какие-нибудь функции?\nДоступные функции:\n0:выход из справочника\n1:вывести весь справочник\n2:добавить новую запись\n3:поиск номера и адреса человека по его имени, адресу, домашнему или мобильному номеру\n4:сортировка справочника по имени, мобильному телефону, домашнему телефону или адресу\n5:экспорт справочника в файл\n')
print ('Good luck!')
