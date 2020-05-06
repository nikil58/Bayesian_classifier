from tkinter import*
from tkinter import filedialog as fd
from tkinter import messagebox
from learn import read, text

def open_file():
    """Функция, отвечающая за открытие любого файла"""
    file_name = fd.askopenfilename()
    read(file_name)
    messagebox.showinfo("Done!","Check out your file")
def press_enter(event):
    """Функция, отвечающая за действия при нажатии на кнопку Enter"""
    s=input_text.get()
    messagebox.showinfo("Done!",text(s))

def help_open():
    help='''Чтобы начать работу, вам достаточно ввести ваше сообщение и нажать Enter.
Появится окно, которое покажет вам спам это или нет.
Также вы можете открыть любой файл в формате .cvs (Таблица exel с разделителем - ;), в которой у вас имеется 2 не пустых столбца.
Желательный вид: первый столбец содержит любую инфурмацию (можно просто нули), а второй - ваши сообщения.
После ваш файл отредактируется и первый столбец будет подписан, и покажет вам, что спам, а что нет'''
    messagebox.showinfo("Help", help)


root = Tk()
root.title("Фильтрация спама")                     #название окна
root.geometry("800x350+300+100")                        #размеры окна и смещение его в центр
root.resizable(False, False) #Отменить возможнось расширения окна

input_text=StringVar()

label = Label(text = "ВВЕДИТЕ ВАШЕ СООБЩЕНИЕ",   #подпись(что делать)
              foreground = "#105753",               #цвет подписи
              padx = "20",                          #отступ по горизонтали
              pady = "20",                          #отступ по вертикали
              font="Arial 16"
              )
label.place(x = 220, y = 60)       #координаты подписи

entry = Entry(textvariable=input_text)                                    #окно ввода
entry.place(height = 20, width = 480, x = 160, y = 130)   #координаты окна ввода
entry.bind ('<Return>', press_enter)

label_or=Label(text = "OR",   #подпись(что делать)
              foreground = "#105753",               #цвет подписи
              padx = "20",                          #отступ по горизонтали
              pady = "20",                          #отступ по вертикали
              font="Arial 16"
              )
label_or.place (x=345, y=165)
open_button=Button(text="Choose file", command = open_file, font=16)
open_button.place(x=340, y=250, height=40, width=90)

help_button=Button(text="Help", command = help_open, font=16)
help_button.place(x=700, y=300, height=40, width=90)
root.mainloop()
