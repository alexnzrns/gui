from tkinter import *
from tkinter import messagebox


def login():
    uname = uname_input.get() #holt sich Daten und speichert in var 
    password = password_input.get()

    if(uname == "1" and password == "1"):
        messagebox.showinfo("", "Login successfull")
        for widget in window.winfo_children():
            widget.destroy() #zerstört alles und macht Fenster im Prinzip clean
            new_window() #öffnet Funktion Schaltjahr berechnen die wieder Widgets hat
            

    elif(uname == "" and password == ""):
        messagebox.showinfo("", "Keine leeren Felder erlaubt!")
    else:
        messagebox.showinfo("", "Falscher Benutzername oder Passwort")


def schaltjahr_berechnung():
    eingabe = eingabe_feld.get()
    eingabe = int(eingabe)

    schaltjahr_label = Label(window, text = 'Es ist ein Schaltjahr!')

    if(eingabe % 4 != 0):
        schaltjahr_label.configure(text='Es ist kein Schaltjahr!')
        schaltjahr_label.place(x=120, y=100)

    if(eingabe % 4 == 0 and eingabe % 100 != 0):
        #hier fehlt der Lösch-Befehl!
        schaltjahr_label.configure(text='Es ist ein Schaltjahr!')
        schaltjahr_label.place(x=120, y=100)

    if(eingabe % 4 == 0 and eingabe % 100 == 0 and eingabe % 400 != 0):
        schaltjahr_label.configure(text='Es ist kein Schaltjahr!')
        schaltjahr_label.place(x=120, y=100)

    if(eingabe % 4 == 0 and eingabe % 100 == 0 and eingabe % 400 == 0):
        schaltjahr_label.configure(text='Es ist ein Schaltjahr!')
        schaltjahr_label.place(x=120, y=100)


def new_window():
    global eingabe_feld 
    eingabe_feld = Entry(window) 
    berechnen_button = Button(window, text = 'Berechnen', command=schaltjahr_berechnung) 
    schliessen_button = Button(window, text = 'Programm beenden', command=window.destroy)
    aufforderung_text = Label(window, text = 'Geben Sie bitte das Jahr zum Berechnen ein:')
    
    aufforderung_text.place(x=55, y=10)
    eingabe_feld.place(x=100, y=40) #damit wird das erstellte Objekt eingabe_feld auf dem Fenster window abgelegt
    berechnen_button.place(x=145, y =70) #damit wird das erstellte Objekt berechnen_button auf dem Fenster window abgelegt
    schliessen_button.place(x=120, y=170)


window = Tk()
window.title('GUI')

Label (window, text = 'Benutzername:').place(x=40, y=30)
Label (window, text = 'Passwort:').place(x=40, y=60)

uname_input = Entry(window)
uname_input.place(x=150, y=30)

password_input = Entry(window)
password_input.place(x=150, y=60)
password_input.config(show="*") #damit er die eingegebenen Daten nicht anzeigt

login_button = Button (window, text = 'Login', command=login)
login_button.place(x=210, y=100)

window.geometry("400x200")
window.minsize(400, 200)
window.maxsize(400, 200)
window.mainloop()
