#! Написана методом проб и ошибок с целью постижения основ Python, любые советы приветствуются на iamhappyperson@bk.ru

from tkinter import *
import sqlite3
import datetime
from tkinter import messagebox as mb


# -*- Добавление данных в таблицу -*-
def addition():
    """
    Кнопка "Добавить обращение в базу"
    """
    ex = executor.get("1.0", 'end-1c')
    if numberreq.get("1.0", 'end-1c') and applicant.get("1.0", 'end-1c') and address.get("1.0", 'end-1c') \
            and datereq.get("1.0", 'end-1c') and themereq.get("1.0", 'end-1c') and exdate.get("1.0", 'end-1c') \
            and ex != '':
        try:
            answer = mb.askyesno(title="ПОДТВЕРДИТЬ ДЕЙСТВИЕ", message="ТОЧНО ДОБАВИТЬ?")
            if answer:
                data = sqlite3.connect("db.db")
                cursor = data.cursor()
                timetoday = datetime.datetime.today().strftime("%d.%m.%Y")  # Тукущее время
                ad_numberreq = numberreq.get("1.0", 'end-1c')
                ad_applicant = applicant.get("1.0", 'end-1c')
                ad_address = address.get("1.0", 'end-1c')
                ad_datereq = datereq.get("1.0", 'end-1c')
                ad_themereq = themereq.get("1.0", 'end-1c')
                ad_exdate = exdate.get("1.0", 'end-1c')
                ad_comment = comment.get("1.0", 'end-1c')
                insetrion = [(ad_numberreq, ad_applicant, ad_address, ad_datereq,
                              ad_themereq, timetoday, ad_exdate, ad_comment, ex)]
                cursor.executemany("INSERT INTO requests VALUES (NULL,?,?,?,?,?,?,?,?,?)", insetrion)
                data.commit()
                data.close()
                mb.showinfo(title="УСПЕХ!", message="ОБРАЩЕНИЕ УСПЕШНО ДОБАВЛЕНО В БАЗУ")
                numberreq.delete("1.0", END)
                applicant.delete("1.0", END)
                address.delete("1.0", END)
                datereq.delete("1.0", END)
                themereq.delete("1.0", END)
                comment.delete("1.0", END)
                exdate.delete("1.0", END)
                executor.delete("1.0", END)
            else:
                numberreq.delete("1.0", END)
                applicant.delete("1.0", END)
                address.delete("1.0", END)
                datereq.delete("1.0", END)
                themereq.delete("1.0", END)
                comment.delete("1.0", END)
                exdate.delete("1.0", END)
                executor.delete("1.0", END)
        except sqlite3.OperationalError:
            mb.showerror(title="ОШИБКА", message="Кто-то еще добавляет данные."
                                                 " Запрещено одновременное добавление данных разными пользователми!!!")
        except:
            mb.showerror(title="ОШИБКА", message="Ошибка добаления записи. Обратитесь к администратору или перезапустите"
                                                 " программу и повторите снова. ")
    else:
        mb.showerror(title="ОШИБКА", message="ПОЛЯ: Номер, Заявитель, Адрес, Дата обращения, Тема обращения, "
                                             "Ответственный исполнитель - должны быть заполнены!")


# -*- Поиск по таблице -*-
def searchbase():
    """
    Кнопка "Найти и отобразить"
    """
    if sdata.get() == '1':
        value = numberreq.get("1.0", 'end-1c')
        if len(value) > 0:
            data = sqlite3.connect("db.db")
            cursor = data.cursor()
            allfind = cursor.execute("SELECT numberreq, applicant, address, datereq, themereq,"
                                     " exdate, comment, executor FROM requests WHERE numberreq like '%'||?||'%'", (value,))
            result = allfind.fetchall()
            if result:
                currents.delete("1.0", END)
                for i in result:
                    currents.insert(1.0, i)
                    currents.insert(1.0, '\n')
                    currents.insert(1.0, '-----------------------------------------------')
                    currents.insert(1.0, '\n')
            else:
                mb.showerror(title="ОШИБКА", message="Значение '" + value + "' отсутствует а базе.")
                data.commit()
                data.close()
        else:
            mb.showerror(title="ОШИБКА", message="Поле 'НОМЕР' не может быть пустым ")
    if sdata.get() == '2':
        value = applicant.get("1.0", 'end-1c')
        if len(value) > 0:
            data = sqlite3.connect("db.db")
            cursor = data.cursor()
            allfind = cursor.execute("SELECT numberreq, applicant, address, datereq, themereq,"
                                     " exdate, comment, executor FROM requests WHERE applicant like '%'||?||'%'", (value,))
            result = allfind.fetchall()
            if result:
                currents.delete("1.0", END)
                for i in result:
                    currents.insert(1.0, i)
                    currents.insert(1.0, '\n')
                    currents.insert(1.0, '-----------------------------------------------')
                    currents.insert(1.0, '\n')
            else:
                mb.showerror(title="ОШИБКА", message="Значение '" + value + "' отсутствует а базе.")
                data.commit()
                data.close()
        else:
            mb.showerror(title="ОШИБКА", message="Поле 'ЗАЯВИТЕЛЬ' не может быть пустым ")
    if sdata.get() == '3':
        value = address.get("1.0", 'end-1c')
        if len(value) > 0:
            data = sqlite3.connect("db.db")
            cursor = data.cursor()
            allfind = cursor.execute("SELECT numberreq, applicant, address, datereq, themereq,"
                                     " exdate, comment, executor FROM requests WHERE address like '%'||?||'%'", (value,))
            result = allfind.fetchall()
            if result:
                currents.delete("1.0", END)
                for i in result:
                    currents.insert(1.0, i)
                    currents.insert(1.0, '\n')
                    currents.insert(1.0, '-----------------------------------------------')
                    currents.insert(1.0, '\n')
            else:
                mb.showerror(title="ОШИБКА", message="Значение '" + value + "' отсутствует а базе.")
                data.commit()
                data.close()
        else:
            mb.showerror(title="ОШИБКА", message="Поле 'АДРЕС' не может быть пустым ")
    if sdata.get() == '4':
        value = datereq.get("1.0", 'end-1c')
        if len(value) > 0:
            data = sqlite3.connect("db.db")
            cursor = data.cursor()
            allfind = cursor.execute("SELECT numberreq, applicant, address, datereq, themereq,"
                                     " exdate, comment, executor FROM requests WHERE datereq like '%'||?||'%'", (value,))
            result = allfind.fetchall()
            if result:
                currents.delete("1.0", END)
                for i in result:
                    currents.insert(1.0, i)
                    currents.insert(1.0, '\n')
                    currents.insert(1.0, '-----------------------------------------------')
                    currents.insert(1.0, '\n')
            else:
                mb.showerror(title="ОШИБКА", message="Значение '" + value + "' отсутствует а базе.")
                data.commit()
                data.close()
        else:
            mb.showerror(title="ОШИБКА", message="Поле 'ДАТА ОБРАЩЕНИЯ' не может быть пустым ")
    if sdata.get() == '5':
        value = themereq.get("1.0", 'end-1c')
        if len(value) > 0:
            data = sqlite3.connect("db.db")
            cursor = data.cursor()
            allfind = cursor.execute("SELECT numberreq, applicant, address, datereq, themereq,"
                                     " exdate, comment, executor FROM requests WHERE themereq like '%'||?||'%'", (value,))
            result = allfind.fetchall()
            if result:
                currents.delete("1.0", END)
                for i in result:
                    currents.insert(1.0, i)
                    currents.insert(1.0, '\n')
                    currents.insert(1.0, '-----------------------------------------------')
                    currents.insert(1.0, '\n')
            else:
                mb.showerror(title="ОШИБКА", message="Значение '" + value + "' отсутствует а базе.")
                data.commit()
                data.close()
        else:
            mb.showerror(title="ОШИБКА", message="Поле 'ТЕМА ОБРАЩЕНИЯ' не может быть пустым ")
    if sdata.get() == '6':
        value = exdate.get("1.0", 'end-1c')
        if len(value) > 0:
            data = sqlite3.connect("db.db")
            cursor = data.cursor()
            allfind = cursor.execute("SELECT numberreq, applicant, address, datereq, themereq,"
                                     " exdate, comment, executor FROM requests WHERE exdate like '%'||?||'%'", (value,))
            result = allfind.fetchall()
            if result:
                currents.delete("1.0", END)
                for i in result:
                    currents.insert(1.0, i)
                    currents.insert(1.0, '\n')
                    currents.insert(1.0, '-----------------------------------------------')
                    currents.insert(1.0, '\n')
            else:
                mb.showerror(title="ОШИБКА", message="Значение '" + value + "' отсутствует а базе.")
                data.commit()
                data.close()
        else:
            mb.showerror(title="ОШИБКА", message="Поле 'ДАТА ИСПОЛНЕНИЯ' не может быть пустым ")
    if sdata.get() == '7':
        value = comment.get("1.0", 'end-1c')
        if len(value) > 0:
            data = sqlite3.connect("db.db")
            cursor = data.cursor()
            allfind = cursor.execute("SELECT numberreq, applicant, address, datereq, themereq,"
                                     " exdate, comment, executor FROM requests WHERE comment like '%'||?||'%'", (value,))
            result = allfind.fetchall()
            if result:
                currents.delete("1.0", END)
                for i in result:
                    currents.insert(1.0, i)
                    currents.insert(1.0, '\n')
                    currents.insert(1.0, '-----------------------------------------------')
                    currents.insert(1.0, '\n')
            else:
                mb.showerror(title="ОШИБКА", message="Значение '" + value + "' отсутствует а базе.")
                data.commit()
                data.close()
        else:
            mb.showerror(title="ОШИБКА", message="Поле 'В ДЕЛО' не может быть пустым ")
    if sdata.get() == '8':
        value = executor.get("1.0", 'end-1c')
        if len(value) > 0:
            data = sqlite3.connect("db.db")
            cursor = data.cursor()
            allfind = cursor.execute("SELECT numberreq, applicant, address, datereq, themereq,"
                                     " exdate, comment, executor FROM requests WHERE executor like '%'||?||'%'", (value,))
            result = allfind.fetchall()
            if result:
                currents.delete("1.0", END)
                for i in result:
                    currents.insert(1.0, i)
                    currents.insert(1.0, '\n')
                    currents.insert(1.0, '-----------------------------------------------')
                    currents.insert(1.0, '\n')
            else:
                mb.showerror(title="ОШИБКА", message="Значение '" + value + "' отсутствует а базе.")
                data.commit()
                data.close()
        else:
            mb.showerror(title="ОШИБКА", message="Поле 'ОТВЕТСТВЕННЫЙ ИСПОЛНИТЕЛЬ' не может быть пустым ")


# -*- Удаление из таблицы -*-
def remove():
    """
    Кнопка "Удаление обращения"
    """
    def removerequest():
        if deleteen.get() and deleteendate.get() != "":
            data = sqlite3.connect("db.db")
            cursor = data.cursor()
            available = cursor.execute("SELECT * FROM requests WHERE (numberreq = ?) AND (datereq = ?)", (deleteen.get(), deleteendate.get()))
            availability = available.fetchall()
            if availability:
                answer = mb.askyesno(parent=swindow, title="ПОДТВЕРДИТЬ ДЕЙСТВИЕ", message="ТОЧНО УДАЛИТЬ?")
                if answer:
                    try:
                        cursor.execute("DELETE FROM requests WHERE numberreq = (?) AND datereq = (?)", (deleteen.get(), deleteendate.get()))
                        data.commit()
                        data.close()
                        swindow.destroy()
                        mb.showinfo(title="УСПЕХ", message="Обращение успешно удалено")
                    except sqlite3.OperationalError:
                        mb.showerror(parent=swindow, title="ОШИБКА", message="Кто-то еще настраивает базу данных!!."
                                                                             " Перезапустите программу и попробуйте снова !!!")
                    except sqlite3.ProgrammingError:
                        mb.showerror(parent=swindow, title="ОШИБКА", message="Кто-то еще удаляет данные."
                                                                             " Запрещено одновременное удаление данных разными пользователми!!!")
                else:
                    pass

            else:
                mb.showerror(parent=swindow, title="ОШИБКА", message="Нет такого обращения")
        else:
            mb.showerror(parent=swindow, title="ОШИБКА", message="Введите номер и дату обращения, которое нужно удалить")
    swindow = Toplevel(root)
    swindow.title("УДАЛЕНИЕ ОБРАЩЕНИЯ ПО НОМЕРУ И ДАТЕ: ")
    swindow.geometry("500x40+900+300")
    swindow.resizable(False, False)
    swindow.attributes("-topmost", True)  # Делает окно выше всех открытых на компе окон
    deleteen = Entry(swindow, bg='lightblue')  # Ввод номера обращения для удаления
    deleteendate = Entry(swindow, bg='lightblue')  # Ввод даты обращения для удаления
    label = Label(swindow, text="Номер")
    label2 = Label(swindow, text="Дата")
    #numberreq.delete("1.0", 'end-1c')
    deletion = Button(swindow, text="УДАЛИТЬ", command=removerequest)  # Кнопка удаления обращения
    label.pack(fill=BOTH, expand=1, side=LEFT)
    deleteen.pack(fill=BOTH, side=LEFT, padx=3, pady=3)
    label2.pack(fill=BOTH, expand=1, side=LEFT)
    deleteendate.pack(fill=BOTH, side=LEFT, padx=3, pady=3)
    deletion.pack(fill=BOTH, expand=1)


# -*- Вывод последних данных в главное окно -*-
def update():
    """
    Кнопка "Показать последние"
    """
    #a = entry_renew.get()
    try:
        #text2=str()
        data = sqlite3.connect("db.db")
        cursor = data.cursor()
        a = int(entry_renew.get())
        #print(a)
        execution = cursor.execute("SELECT numberreq, applicant, address, datereq, themereq, exdate, "
                                   "comment, executor FROM requests ORDER BY ID DESC LIMIT (?)", (a,))
        currents.delete("1.0", END)
        for i in execution:
            currents.insert(1.0, i)
            currents.insert(1.0, '\n')
            currents.insert(1.0, '-----------------------------------------------')
            currents.insert(1.0, '\n')
        # symbols = ['{}']
        # #text = currents.get("1.0", 'end-1c')
        # text = currents.get('1.0',END+'-1c')
        # for symbol in symbols:
        #     if symbol in text:
        #         text2 = text.replace(symbol, '')
        # currents.delete("1.0", END)
        # currents.insert(1.0, text2)
    except sqlite3.IntegrityError:
        mb.showerror(title="ОШИБКА", message="Введены неверные данные")
    except:
        mb.showerror(title="ОШИБКА", message="Проверьте введенные данные.")

# -*- Редактирование данных в таблице -*-
def edit():
    """
    Кнопка "Редактирование обращения номер"
    """
    number = entry_edit.get()
    ot = entry_otdate.get()

    def editing():
        if newinfo.get("1.0", 'end-1c') != '':
            answer = mb.askyesno(parent=swindow, title="Подтверждение действия", message="Точно изменить?")
            if answer:
                value = str((askchoose.get(ACTIVE)))
                secondvalue = newinfo.get("1.0", 'end-1c')
                insertion = [(secondvalue, number, entry_otdate.get())]
                data = sqlite3.connect("db.db")
                cursor = data.cursor()
                try:
                    if value == 'НОМЕР':
                        cursor.executemany("UPDATE requests SET numberreq = (?) WHERE numberreq = (?) AND datereq = (?) ", insertion)
                    elif value == 'ЗАЯВИТЕЛЬ':
                        cursor.executemany("UPDATE requests SET applicant = (?) WHERE numberreq = (?) AND datereq = (?) ", insertion)
                    elif value == 'АДРЕС':
                        cursor.executemany("UPDATE requests SET address = (?) WHERE numberreq = (?) AND datereq = (?) ", insertion)
                    elif value == 'ДАТА ОБРАЩЕНИЯ':
                        cursor.executemany("UPDATE requests SET datereq = (?) WHERE numberreq = (?) AND datereq = (?) ", insertion)
                    elif value == 'ТЕМА ОБРАЩЕНИЯ':
                        cursor.executemany("UPDATE requests SET themereq = (?) WHERE numberreq = (?) AND datereq = (?) ", insertion)
                    elif value == 'ДАТА ИСПОЛНЕНИЯ':
                        cursor.executemany("UPDATE requests SET exdate = (?) WHERE numberreq = (?) AND datereq = (?) ", insertion)
                    elif value == 'В ДЕЛО':
                        cursor.executemany("UPDATE requests SET comment = (?) WHERE numberreq = (?) AND datereq = (?) ", insertion)
                    elif value == 'ОТВЕТСТВЕННЫЙ':
                        cursor.executemany("UPDATE requests SET executor = (?) WHERE numberreq = (?) AND datereq = (?) ", insertion)
                    data.commit()
                    data.close()
                    mb.showinfo(parent=swindow, title="УСПЕХ! ", message="Успешно изменено")
                    swindow.destroy()
                except sqlite3.OperationalError:
                    mb.showerror(title="ОШИБКА", message="Кто-то еще изменяет данные."
                                                         " Запрещено одновременное изменение данных разными пользователми!!!")
                except:
                    mb.showerror(title="ОШИБКА",
                                 message="Ошибка изменения записи. Обратитесь к администратору или перезапустите"
                                         " программу и повторите снова. ")
        else:
            mb.showerror(parent=swindow, title="ОШИБКА", message="Полле ввода не должно быть пустым")
    if entry_edit.get() and entry_otdate.get() != "":
        currentreq = entry_edit.get()
        currentdate = entry_otdate.get()
        data = sqlite3.connect("db.db")
        cursor = data.cursor()
        available = cursor.execute("SELECT * FROM requests WHERE (numberreq = ?) AND (datereq = ?)", (currentreq, currentdate))
        availability = available.fetchall()
        if availability:
            swindow = Toplevel(root)
            swindow.title("РЕДАКТИРОВАНИЕ: ")
            swindow.geometry("300x215+900+300")
            swindow.resizable(False, False)
            swindow.attributes("-topmost", True)  # Делает окно выше всех открытых на компе окон
            askinfo = Label(swindow, text="Выберите параметр для редактирования: ")
            askchoose = Listbox(swindow, width=42, height=8,)

            newinfo = Text(swindow, width=35, height=3, borderwidth=2, bg='lightblue')
            scrolnewinfo = Scrollbar(swindow, cursor='hand1')
            scrolnewinfo.config(command=newinfo.yview)
            proceed = Button(swindow, text="Редактировать выбранный элемент", command=editing)

            askinfo.pack()
            askchoose.pack()
            newinfo.pack(side=LEFT, anchor='n',expand=1)
            scrolnewinfo.pack(side=LEFT, anchor='n', fill=X)
            proceed.place(relwidth=1, y=191)  # Кнопка редактирования новых данных
            newinfo.config(yscrollcommand=scrolnewinfo.set)  # Конфигурация окна ввода новой инфы

            for i in ('НОМЕР', 'ЗАЯВИТЕЛЬ', 'АДРЕС', 'ДАТА ОБРАЩЕНИЯ', 'ТЕМА ОБРАЩЕНИЯ', 'ДАТА ИСПОЛНЕНИЯ', 'В ДЕЛО', 'ОТВЕТСТВЕННЫЙ',):
                askchoose.insert(0, i)

        else:
            mb.showerror(title="ОШИБКА", message="Нет такого обращения")
    else:
        mb.showerror(parent=root, title="ОШИБКА", message="Введите номер и дату обращения, которое нужно отредактировать")


def readme():
    swindow = Toplevel(root)
    swindow.title("Инструкция использования: Пожелания на: iamhappyperson@bk.ru  ")
    swindow.geometry("+900+300")
    swindow.resizable(False, False)
    swindow.attributes("-topmost", True)  # Делает окно выше всех открытых на компе окон
    helpinfo2 = Label(swindow, justify=LEFT, text="""1. Поиск нужного обращения можно делать по любому из значений, для этого нужно 
    поставить галочку "Найти" над тем полем, по значению из которого нужно произвести поиск.
    Все поля чувствительны к регистру (Есть разница между маленькими и БОЛЬШИМИ БУКВАМИ). 
    Поэтому, например, если в базе есть обращение, в котором фамилия ответственного
    начинается с Большой Буквы, то найти это обращение по мАленькой букве не получится. 
    Поиск такого обращения нужно делать по Большой Букве. Поэтому рекомендую вносить в 
    программу обращения в установленной заранее форме.""")
    helpinfo3 = Label(swindow, justify=LEFT, text="""2. Кнопка "Показать последние": Выводит в главное окно последние обращения начиная с конца. 
    Количество выводимых обращений можно менять в окне рядом с этой кнопкой.""")
    heplinfo4 = Label(swindow, justify=LEFT, text="     3. Если у вас есть дополнительные вопросы, просьба обратиться к непосредственному руководителю.")
    helpinfo2.pack()
    helpinfo3.pack()
    heplinfo4.pack()


root = Tk()
root.attributes('-alpha', 0.9)  # Делаю основное окно прозрачным на 10%
scroller = Scrollbar(root)
currents_scroller = Scrollbar(root)
root.title("Учет обращений, поступивших в Брестский зональный ЦГиЭ")
root.resizable(False, False)
root.geometry("1025x520+500+300")

mainmenu = Menu()  # Меню, которое сверху
mainmenu.add_command(label="Помощь", command=readme)  # Кнопка меню, которое сверху

numberreq = Text(width=10, height=3, borderwidth=2, bg='lightblue', wrap='word')
applicant = Text(width=20, height=3, borderwidth=2, bg='lightblue', wrap='word')
address = Text(width=20, height=3, borderwidth=2, bg='lightblue', wrap='word')
datereq = Text(width=10, height=3, borderwidth=2, bg='lightblue', wrap='word')
themereq = Text(width=28, height=3, borderwidth=2, bg='lightblue', wrap='word')
themereq.config(yscrollcommand=scroller.set)
comment = Text(width=10, height=3, borderwidth=2, bg='lightblue', wrap='word')
exdate = Text(width=10, height=3, borderwidth=2, bg='lightblue', wrap='word')
currents = Text(width=125, height=16, bg='lightblue', wrap='word')
currents.config(yscrollcommand=currents_scroller.set)
frame = Frame(width=1030, height=1, bg="black", colormap="new")
executor = Text(root, width=35, height=1, borderwidth=2, bg='lightblue', wrap='word')  # Окно ввода ответственного исполнителя
executor.config(borderwidth=3)  # Конфигурация окна ввода ответственного исполнителя


lab_numberreq = Label(text="Номер", bg='Tan')  # Надпись "Номер"
lab_applicant = Label(text="Заявитель", bg='Tan')  # Надпись "Заявитель"
lab_address = Label(text="Адрес", bg='Tan')  # Надпись "Адрес"
lab_datereq = Label(text="Дата обращения", bg='Tan')  # Надпись "Дата обращения"
lab_themereq = Label(text="Тема обращения", bg='Tan')  # Надпись "Тема обращения"
lab_exdate = Label(text="Дата исполнения", bg='Tan')  # Надпись "Дата исполнения"
lab_comment = Label(text="В дело", bg='Tan')  # Надпись "В дело"
lab_executor = Label(text="Ответственный исполнитель: ", bg='Tan')  # Надпись "Ответственный испольнитель"
lab_ot = Label(text="От: ", bg='Tan')


addrequest = Button(text="Добавить обращение в базу",
                    font='2', command=addition, bg='LightSteelBlue', overrelief=RIDGE, activebackground='Ivory')
edit = Button(text="Редактирование обращения номер: ",
              font='2', bg='LightSteelBlue', overrelief=RIDGE, command=edit, activebackground='Ivory')
delete = Button(text="Удаление обращения",
                font='2', bg='LightSteelBlue', overrelief=RIDGE, command=remove, activebackground='Ivory')
search = Button(text="Найти и отобразить",
                font='2', bg='LightSteelBlue', overrelief=RIDGE, command=searchbase, activebackground='Ivory')
renew = Button(text="Показать последние:",
               font='2', bg='LightSteelBlue', overrelief=RIDGE, command=update, activebackground='Ivory')

sdata = StringVar()  # Переменная для радиокнопок
but_numberreq = Radiobutton(text="Найти", activebackground='LightSteelBlue',
                            value=1, highlightthickness=5, variable=sdata, bg='Tan')  # Радиокнопка "Номер"
but_applicant = Radiobutton(text="Найти", activebackground='LightSteelBlue',
                            value=2, highlightthickness=5, variable=sdata, bg='Tan')  # Радиокнопка "Заявитель"
but_address = Radiobutton(text="Найти", activebackground='LightSteelBlue',
                          value=3, highlightthickness=5, variable=sdata, bg='Tan')  # Радиокнопка "Адрес"
but_datereq = Radiobutton(text="Найти", activebackground='LightSteelBlue',
                          value=4, highlightthickness=5, variable=sdata, bg='Tan')  # Радиокнопка "Дата обращения"
but_themereq = Radiobutton(text="Найти", activebackground='LightSteelBlue',
                           value=5, highlightthickness=5, variable=sdata, bg='Tan')  # Радиокнопка "Тебя обращения"
but_exdate = Radiobutton(text="Найти", activebackground='LightSteelBlue',
                         value=6, highlightthickness=5, variable=sdata, bg='Tan')  # Радиокнопка "Дата исполнения"
but_comment = Radiobutton(text="Найти", activebackground='LightSteelBlue',
                          value=7, highlightthickness=5, variable=sdata, bg='Tan')  # Радиокнопка "В дело"
but_executor = Radiobutton(text="Найти", activebackground='LightSteelBlue',
                          value=8, highlightthickness=5, variable=sdata, bg='Tan')  # Радиокнопка "Ответственный исполнитель"

var_renew = IntVar()  # Переменная для вставки количества отображаемых обращений по умолчания
entry_renew = Entry(width=5, bd=10, textvariable=var_renew, bg='lightblue')  # Окно ввода количчества отображаемых обращений
entry_renew.insert(0,1)  # Вставка в окно ввода количества отображаемых обращений цифры 10
entry_edit = Entry(width=10, bd=10, bg='lightblue')  # Поле ввода номера обращения для редактирования
entry_otdate = Entry(width=12, bd=10, bg='lightblue')  # Поле ввода даты обращения для редактирования


lab_numberreq.grid(row=100, column=0, pady=5)  # Строка "Номер обращения"
numberreq.grid(row=99, column=0, padx=5)  # Окно ввода "Номер обращения"
but_numberreq.grid(row=98, column=0)  # Радиокнопка для поиска по номеру обращения

lab_applicant.grid(row=100, column=1, pady=5)  # Строка "Заявитель"
applicant.grid(row=99, column=1, padx=5)  # Окно ввода "Заявитель"
but_applicant.grid(row=98, column=1)  # Радиокнопка для поиска по заявителю

lab_address.grid(row=100, column=2, pady=5)  # Строка "Адрес"
address.grid(row=99, column=2, padx=5)  # Окно ввода "Адрес"
but_address.grid(row=98, column=2)  # Радиокнопка для поиска по адресу

lab_datereq.grid(row=100, column=3, pady=5)  # Строка "Дата обращения"
datereq.grid(row=99, column=3, padx=5)  # Окно ввода "Дата обращения"
but_datereq.grid(row=98, column=3)  # Радиокнопка для поиска по дате обращения

lab_themereq.grid(row=100, column=4)  # Строка "Тема обращения"
themereq.grid(row=99, column=4)  # Окно ввода "Тема обращения"
but_themereq.grid(row=98, column=4)  # Радиокнопка для поиска по теме обращения

#scroller.place(x=790, y=74)  # Скроллер справа от окна "Тема обращения"

lab_exdate.grid(row=100, column=5)  # Строка "Дата исполнения"
exdate.grid(row=99, column=5,)  # Окно ввода "Дата исполнения"
but_exdate.grid(row=98, column=5)  # Радиокнопка для поиска по "Дате Исполнения"

lab_comment.grid(row=100, column=6)  # Строка "В Дело"
comment.grid(row=99, column=6)  # Окно ввода "В Дело"
but_comment.grid(row=98, column=6)  # Радиокнопка для поиска по "В Дело"

addrequest.grid(row=96, column=0, pady=5, padx=5, columnspan=3, sticky=W+E+N+S)  # Кнопка добавления
search.grid(row=96, column=3, pady=5, padx=5, columnspan=2, sticky=W+E+N+S)  # Кнопка поиска
delete.grid(row=96, column=5, pady=5, padx=5, columnspan=2, sticky=W+E+N+S)  # Кнопка удаления

frame.place(x=0, y=142)  # Вертикальная линия проходящая через названия окон ввода данных

lab_executor.grid(row=102, column=0, columnspan=2)  # Текст "Ответственный исполнитель: "
executor.grid(row=102, column=2, columnspan=2, sticky='e')  # Окно ввода ответственного исполнителя
but_executor.grid(row=102, column=3, sticky='e')  # Радиокнопка для поиска по ответственному исполнителю

currents.grid(row=105, column=0, columnspan=20, sticky=W)  # Окно вывода последних обращений
currents_scroller.place(x=1007, y=192, height=260,)  # Скроллер главного поля

renew.place(x=2, y=493, anchor=W)  # Кнопка отображения последних обращений
entry_renew.place(x=170, y=493, anchor=W)

edit.place(x=250, y=493, anchor=W)  # Кнопка "Редактирование обращения номер: "
entry_edit.place(x=530, y=493, anchor=W)  # Поле ввода номера редактируемого обращения
lab_ot.place(x=620, y=493, anchor=W)  # Надпись "От: "
entry_otdate.place(x=650, y=493, anchor=W)  # Поле ввода даты обращения для редактирования

currents_scroller.config(command=currents.yview, width=15, cursor='hand1', activerelief=FLAT)  # Скроллер на основном окне
scroller.config(command=themereq.yview, width=15, activerelief=FLAT, highlightcolor='red', cursor='hand1')  # Настройки скроллера главного окна
root.config(menu=mainmenu, bg='Tan')  # Конфигурация главного окна
root.mainloop()  # Зацикливание графического интерфейса