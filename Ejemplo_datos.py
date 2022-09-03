 # -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 06:40:29 2022

@author: USER
"""
from tkinter import *
from tkinter import ttk
import pyodbc

ventana = Tk()
ventana.title("Ejemplo")
ventana.geometry("600x600")
ventana["bg"]="#f60"
e_texto = Entry(ventana, font= ("Calibri 20"))
arbol = ttk.Treeview(ventana, columns=("Id","Apellido" ,"Nombre", "Fecha", "Telefono"))
arbol.insert("",END,text="Principe",values=("10","20"))
arbol.place(x=10, y=20)

try:
    connection=pyodbc.connect("DRIVER={SQL Server}; SERVER=RYOOXNAY; DATABASE=Practica; UID=sa; PWD=ryooxnay")
    print("Conexion exitosa")
    cursor = connection.cursor()
    #cursor.execute("SELECT @@version;")
    #row = cursor.fetchone()
    #print(row)
    cursor.execute("SELECT * FROM usuarios")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        
except Exception as ex:
    print(ex)
finally:
    connection.close()
    print("Conexión finalizada.")
















    

ventana.mainloop()

