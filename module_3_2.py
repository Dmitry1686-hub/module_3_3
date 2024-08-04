def send_email(messege, recipient ,sender = "university.help@gmail.com"):

    if (str(recipient) and str(sender) != ('@') or ('.com','.ru','.net')) is False:
        print("Невозможно отправить письмо с адреса", str(sender), "на адрес ", str(recipient))
    elif recipient == sender:
        print("Нельзя  отправить письмо самому себе!")
    elif sender == "university.help@gmail.com" :
        print("Письмо успешно отправлено с адреса ", str(sender),'на адрес ', str (recipient))
    elif sender  == 'urban.teacher@mail.uk':
        print("Невозможно отправить письмо с адреса ",str(sender), ' на адрес ', str (recipient))
    else:
         print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ", str(sender), "на адрес ", str(recipient))




send_email('Сообщение для проверки связи ', 'vasyok1337@gmail.com',)
send_email('Вы видите это сообщение как лучший студент курса !', ' urban.fan@mail.ru', sender = 'urban.info@gmail.com')
send_email('Пожалуйста, исправьте задние', 'urban.student@mail.ru', sender= 'urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре ', 'urban.teacher@mail.ru', sender= 'urban.teacher@mail.ru')
