from tkinter import *   #importiert alles vom Framework tkinter, das zum erstellen einer GUI(graphical-user-interface) gemacht ist
from tkinter import messagebox

def read_eingabe_feld():    #Funktion zum einlesen vom Eingabefeld in eine Variable
    global eingabe 
    eingabe = eingabe_feld.get() #damit wird die get Funktion im Eingabefeld aufgerufen und holt sich den eingegebenen Input und speichert es in der Variable eingabe
    print(eingabe)
    return eingabe

def berechnung():
    eingabe = eingabe_feld.get() #damit wird die get Funktion im Eingabefeld aufgerufen und holt sich den eingegebenen Input und speichert es in der Variable eingabe
    eingabe = int(eingabe) #macht aus der eingabe einen Integer - wird benötigt für die Berechnung
    #print(type(eingabe)) #testet ob die Eingabe wirklich ein Integer ist

    if(eingabe % 4 != 0):
        #print('Es ist kein Schaltjahr')

    if(eingabe % 4 == 0 and eingabe % 100 != 0):
        #print('Es ist ein Schaltjahr')

    if(eingabe % 4 == 0 and eingabe % 100 == 0 and eingabe % 400 != 0):
        #print('Es ist kein Schaltjahr')

    if(eingabe % 4 == 0 and eingabe % 100 == 0 and eingabe % 400 == 0):
        #print('Es ist ein Schaltjahr')


window = Tk() #erstellt das Fenster durch tkinter
window.title('Schaltjahrberechnung') #gibt dem Fenster den Titel 'Schaltjahrberechnung'

eingabe_feld = Entry(window) #erzeugt ein im tkinter Framework enthaltenes Eingabefeld innerhalb des Fensters window
berechnen_button = Button(window, text = 'Berechnen' , command=berechnung) #erzeug ein im tkinter Framework enthaltenen Button innerhalb des Fensters window mit dem Text 'Berechnen' darauf und beim klicken wird die Funktion ausgelöst
schliessen_button = Button(window, text = 'Programm beenden', command=window.destroy)
aufforderung_text = Label(window, text = 'Geben Sie bitte das Jahr zum Berechnen ein:') #c-p oben


aufforderung_text.pack()
eingabe_feld.pack() #damit wird das erstellte Objekt eingabe_feld auf dem Fenster window abgelegt
berechnen_button.pack() #damit wird das erstellte Objekt berechnen_button auf dem Fenster window abgelegt
schliessen_button.pack()

window.geometry("400x200")
window.mainloop() #damit wird das tkinter Fenster window gestartet 
