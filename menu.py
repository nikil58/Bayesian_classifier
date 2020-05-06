from tkinter import*
from tkinter import filedialog as fd
from tkinter import messagebox
from learn import read, text

def open_file():
    file_name = fd.askopenfilename()
    read(file_name)
    messagebox.showinfo("Done!","Check out your file")
def press_enter(event):
    """Функция, отвечающая за действия при нажатии на кнопку Enter"""
    s=input_text.get()
    messagebox.showinfo("Done!",text(s))

root = Tk()
root.title("фильтрация спама")                     #название окна
root.geometry("800x600+300+100")                        #размеры окна и смещение его в центр
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
open_button=Button(text="Choose file", command = open_file)
open_button.place(x=350, y=250)

root.mainloop()
