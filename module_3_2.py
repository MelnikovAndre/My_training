def send_email(message,recipient,*,sender = "university.help@gmail.com"):
    print(message,recipient,end="")
    i="@"
    if i in sender:
        print("")
        if sender.endswith(".com"):
            print(end="")
        elif sender.endswith(".ru"):
            print(end="")
        elif sender.endswith(".net"):
            print(end="")
        else:
            print("Невозможно отправить письмо с адреса <sender> на адрес <recipient>")
    k="@"
    if k in recipient:
        print(end="")
        if recipient.endswith(".com"):
            print(end="")
        elif recipient.endswith(".ru"):
            print(end="")
        elif recipient.endswith(".net"):
            print(end="")
        else:
            print("Невозможно отправить письмо с адреса <sender> на адрес <recipient>")
    if recipient==sender:
        print("Нельзя отправить письмо самому себе!")
    if sender=="university.help@gmail.com":
        print("Письмо успешно отправлено с адреса <sender> на адрес <recipient>")
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>.")




#send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
#send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
#send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
