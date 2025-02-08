import sys
import os
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont
from formulas import *
from tkinter import messagebox
#import pandas as pd



def resource_path(relative_path):
    """ Obtiene la ruta absoluta del recurso, compatible con PyInstaller """
    try:
        # Cuando se ejecuta como .exe, usa la carpeta temporal de PyInstaller
        base_path = sys._MEIPASS
    except Exception:
        # En ejecución normal, usa la ruta absoluta del script
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



######################################################## MENU PRINCIPAL ##################################################################################

def menu_principal():
    #Inicio
    global ventana
    ventana=tk.Tk()
    ventana.title("Inicio Banco")
    ventana.geometry("500x600")
    fondo_imagen = tk.PhotoImage(file=resource_path("fondo.png"))
    fondo_label = tk.Label(ventana, image=fondo_imagen)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

    global Title_font 
    Title_font= tkfont.Font(family="Times New Roman", size=16, weight="bold")
    global Btn_font
    Btn_font= tkfont.Font(family="Times New Roman",size=12)
    style = ttk.Style()
    style.configure('TButton', font=Btn_font)       
    #Bienvenida
    label = ttk.Label(ventana, text="Bienvenido a su Banco de confianza",font=Title_font,background='White')
    label.pack(pady=40)

    label = ttk.Label(ventana, text="¿En qué te podemos colaborar?",font=Title_font,background='White')
    label.pack(pady=40)

    ICButton = ttk.Button(ventana, width=25, style='TButton', text="Interés Compuesto",command=lambda: (ventana.destroy(), InteresCompuesta()))
    ICButton.pack(pady=10)

    EQTButton = ttk.Button(ventana, width=25, style='TButton', text="Equivalencia de Tasas",command=lambda: (ventana.destroy(), Conversión_Tasas()))
    EQTButton.pack(pady=10)

    AButton = ttk.Button(ventana, width=25, style='TButton', text="Anualidades",command=lambda: (ventana.destroy(), Anualidades()))
    AButton.pack(pady=10)

    AmorButton = ttk.Button(ventana, width=25, style='TButton', text="Amortización", command=lambda: (ventana.destroy(), Amortizacion()))
    AmorButton.pack(pady=20)

    Autores = ["Autores","Cristian Alejandro Bejarano Castellanos - 20242678033", "Dana Valentina Lozano Delgadillo - 20242678032", "Carlos Alberto Rubiano - 20242678019", "Lina Marcela Bonill Rincón - 20242678034"]
        
    for author in Autores:
        author_label = ttk.Label(ventana, text=author, font=Btn_font, background='White')
        author_label.pack(pady=5)  
    ventana.mainloop()



######################################################################## INTERÉS COMPUESTO ####################################################################################

def InteresCompuesta(): #Menu de Intéres Compuesta 
    global ventanacompuesta
    ventanacompuesta = tk.Tk()
    ventanacompuesta.title("Intéres compuesto")
    ventanacompuesta.geometry("500x400")

    fondo_imagen = tk.PhotoImage(file=resource_path("fondo.png"))
    fondo_label = tk.Label(ventanacompuesta, image=fondo_imagen)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

    label = ttk.Label(ventanacompuesta, text="Intéres Compuesto",font=Title_font,background='White')
    label.pack(pady=50)
    label = ttk.Label(ventanacompuesta, text="Selecciona el cálculo a realizar",font=Title_font,background='White')
    label.pack(pady=50)

    options = ["Valor", "Tiempo", "Tasa"]
    option_combobox = ttk.Combobox(ventanacompuesta, values=options, state="readonly")
    option_combobox.pack(pady=10)
 
    continue_button = ttk.Button(ventanacompuesta, text="Continuar", 
                                    command=lambda:ValidarOpcionCompuesta(option_combobox.get()))
    continue_button.pack(pady=10)

     # Botón Volver Menu principal
    back_button = ttk.Button(ventanacompuesta, text="Volver Menu principal", command=lambda:(ventanacompuesta.withdraw(),ventanacompuesta.destroy(), menu_principal()))
    back_button.pack(pady=10)

    ventanacompuesta.mainloop()

##################################################################################### ANUALIDADES #######################################################################################

def Anualidades():
    global ventananualidades
    ventananualidades = tk.Tk()
    ventananualidades.title("Anualidades")
    ventananualidades.geometry("500x400")

    fondo_imagen = tk.PhotoImage(file=resource_path("fondo.png"))
    fondo_label = tk.Label(ventananualidades, image=fondo_imagen)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

    label = ttk.Label(ventananualidades, text="Anualidades", font=("Arial", 16, "bold"), background='White')
    label.pack(pady=20)

    #Seleccionar la anualidad    
    label = ttk.Label(ventananualidades, text="Selecciona la anualidad",font=Title_font,background='White')
    label.pack(pady=50)

    #opciones de anualidades
    options = ["Perpetua", "Vencida", "Anticipada"]
    option_combobox = ttk.Combobox(ventananualidades, values=options, state="readonly")
    option_combobox.pack(pady=10)

    #botón de continuar despues de seleccionar la opcion de anualidad
    continue_button = ttk.Button(ventananualidades, text="Continuar", 
                                    command=lambda:ValidarOpcionAnualidad(option_combobox.get()))
    continue_button.pack(pady=10)

    # Botón Volver al Menú principal
    back_button = ttk.Button(ventananualidades, text="Volver al Menú principal", 
                             command=lambda: (ventananualidades.withdraw(), ventananualidades.destroy(), menu_principal()))
    back_button.pack(pady=20)
    ventananualidades.mainloop()

##############################################################################################################################################################################


##################################################################################### ANUALIDADES #######################################################################################

def Amortizacion():
    global ventanaAmortizacion
    ventanaAmortizacion = tk.Tk()
    ventanaAmortizacion.title("Amortización")
    ventanaAmortizacion.geometry("500x400")

    # Imagen de fondo (debe ser un archivo PNG)
    fondo_imagen = tk.PhotoImage(file=resource_path("fondo.png"))
    fondo_label = tk.Label(ventanaAmortizacion, image=fondo_imagen)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

    ttk.Label(ventanaAmortizacion, text="Cálculo de Amortización", font=("Arial", 12, "bold"), background='White').pack(pady=10)

    # Entrada del préstamo
    ttk.Label(ventanaAmortizacion, text="Ingrese el monto del préstamo:", font=("Arial", 10), background='White').pack(pady=5)
    prestamo_entry = ttk.Entry(ventanaAmortizacion, width=30)
    prestamo_entry.pack(pady=5)

    # Entrada de la tasa de interés
    ttk.Label(ventanaAmortizacion, text="Ingrese la tasa de interés (decimal):", font=("Arial", 10), background='White').pack(pady=5)
    tasa_entry = ttk.Entry(ventanaAmortizacion, width=30)
    tasa_entry.pack(pady=5)

    # Entrada del número de períodos
    ttk.Label(ventanaAmortizacion, text="Ingrese el número de períodos:", font=("Arial", 10), background='White').pack(pady=5)
    num_periodos_entry = ttk.Entry(ventanaAmortizacion, width=30)
    num_periodos_entry.pack(pady=5)

    # Output label
    output_label = ttk.Label(ventanaAmortizacion, text="", background='white', font=("Arial", 12, "bold"))
    output_label.pack(pady=10)

    # Botón para calcular
    calcular_button = ttk.Button(ventanaAmortizacion, text="Calcular",
                                 command=lambda: Calcular_Amortizacion(prestamo_entry.get(), tasa_entry.get(), num_periodos_entry.get(), output_label))
    calcular_button.pack(pady=10)

    # Botón para volver al menú principal
    back_menu_principal = ttk.Button(ventanaAmortizacion, text="Volver al Menú Principal", command=lambda:(ventanaAmortizacion.withdraw(), ventanaAmortizacion.destroy(), menu_principal()))
    back_menu_principal.pack(pady=10)

    ventanaAmortizacion.mainloop()

##############################################################################################################################################################################




def ValidarOpcionCompuesta(opcion): #Verifica la opción escogida 
     if opcion == "Valor":
            ventanacompuesta.withdraw()
            ventanacompuesta.destroy()
            InteresCompuestaValor()
     elif opcion =="Tiempo":
            ventanacompuesta.withdraw()
            ventanacompuesta.destroy()
            InteresCompuestoTiempo()
     elif opcion == "Tasa":
            ventanacompuesta.withdraw()
            ventanacompuesta.destroy()
            InteresCompuestoTasa()

def ValidarOpcionAnualidad(opcion): #Verifica la opción escogida 
     if opcion == "Perpetua":
            ventananualidades.withdraw()
            ventananualidades.destroy()
            AnualidadPerpetua()
     elif opcion =="Vencida":
            ventananualidades.withdraw()
            ventananualidades.destroy()
            AnualidadVencida()
     elif opcion == "Anticipada":
            ventananualidades.withdraw()
            ventananualidades.destroy()
            AnualidadAnticipada()
     


def es_numero(texto):
    # Verifica si el texto es vacío o si es un número válido
    return texto.isdigit() or texto == ""


#Verifica en decimal
def es_decimal(P):
        try:
            if P == "":
                return True
            value = float(P)
            if 0.0 <= value <= 1.0:
                return True
            else:
                return False
        except ValueError:
            return False


##### Sección donde el usuario quiere saber el valor sea de Valor futuro o Presente 
def InteresCompuestaValor():
      global ventanaCompuestaValor
      ventanaCompuestaValor = tk.Tk()
      ventanaCompuestaValor.title("Intéres compuesto")
      ventanaCompuestaValor.geometry("500x600")

      fondo_imagen = tk.PhotoImage(file=resource_path("fondo.png"))
      fondo_label = tk.Label(ventanaCompuestaValor, image=fondo_imagen)
      fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

      #Recolectar que tipo de valor : Valor Presente o valor Futuro

      ttk.Label(ventanaCompuestaValor, text="Seleccione el tipo de valor:", font=Title_font,background='White').pack(pady=5)
      calc_type = ttk.Combobox(ventanaCompuestaValor, values=["Valor Presente", "Valor Futuro"], state="readonly")
      calc_type.pack(pady=5)

      #Al obtener el tipo de valor a buscar se debe recolectar los demás datos para completar la formula
      #Valor que si se tiene
      validacion_cantidad=ventanaCompuestaValor.register(es_numero)
      valor_label = ttk.Label(ventanaCompuestaValor, text="Valor Futuro o Presente restante:",font=Title_font,background='White')
      valor_label.pack(pady=5)
      valor_entry = ttk.Entry(ventanaCompuestaValor, width=30, validate='key', validatecommand=(validacion_cantidad, "%P"))
      valor_entry.pack(pady=5)

      #Tasa
      validacion_fraccion=ventanaCompuestaValor.register(es_decimal)
      valor_label_tasa = ttk.Label(ventanaCompuestaValor, text="Tasa en decimal ej:0.10->10%",font=Title_font,background='White')
      valor_label_tasa.pack(pady=5)
      valor_entry_tasa = ttk.Entry(ventanaCompuestaValor, width=30, validate='key', validatecommand=(validacion_fraccion, "%P"))
      valor_entry_tasa.pack(pady=5)
      #Tipo de tasa
      tipo_tasa = ttk.Combobox(ventanaCompuestaValor, values=["Efectiva", "Nominal"], state="readonly", width=10)
      tipo_tasa.pack()

      periodo_tasa = ttk.Combobox(ventanaCompuestaValor, values=["M", "B", "T", "C", "S", "A"], state="readonly", width=5)
      periodo_tasa.pack()

      #Tiempo
      valor_label = ttk.Label(ventanaCompuestaValor, text="Periodo (n)",font=Title_font,background='White')
      valor_label.pack(pady=5)
      valor_entry_n = ttk.Entry(ventanaCompuestaValor, width=30, validate='key', validatecommand=(validacion_cantidad, "%P"))
      valor_entry_n.pack(pady=5)

      periodo_n = ttk.Combobox(ventanaCompuestaValor, values=["M", "B", "T", "C", "S", "A"], state="readonly", width=5)
      periodo_n.pack(pady=5)

      output_label = ttk.Label(ventanaCompuestaValor, text="", background='white')
      output_label.pack(pady=10)

      continue_button = ttk.Button(ventanaCompuestaValor, text="Continuar", 
                                    command=lambda:Calcular_Valor_Compuesto(calc_type, valor_entry.get(),  valor_entry_tasa.get(), tipo_tasa.get(), periodo_tasa.get(), valor_entry_n.get(),periodo_n.get(), output_label ))
      
      #Calcular_ICompuesto(Valor a buscar, Valor que ya tenemos, valor de la tasa, Tipo de tasa, periodo de tasa, Tiempo, periodo de tiempo)
      continue_button.pack(pady=10)

      #Botón volver a la ventana Anterior
      back_button = ttk.Button(ventanaCompuestaValor, text="Volver a la ventana Anterior", command=lambda: (ventanaCompuestaValor.withdraw(), ventanaCompuestaValor.destroy(), InteresCompuesta()))

      back_button.pack(pady=10)
      #Boton para volver al Menu Principal
      back_menu_principal = ttk.Button(ventanaCompuestaValor, text="Volver al menu principal", command=lambda:(ventanaCompuestaValor.withdraw(), ventanaCompuestaValor.destroy(), menu_principal()))
      back_menu_principal.pack(pady=10)
      ventanaCompuestaValor.mainloop()


### Sección de impuesto de tiempo ###

def InteresCompuestoTiempo():
      global ventanaCompuestaTiempo
      ventanaCompuestaTiempo = tk.Tk()
      ventanaCompuestaTiempo.title("Intéres compuesto Tiempo")
      ventanaCompuestaTiempo.geometry("500x400")

      fondo_imagen = tk.PhotoImage(file=resource_path("fondo.png"))
      fondo_label = tk.Label(ventanaCompuestaTiempo, image=fondo_imagen)
      fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
      
      validacion_cantidad=ventanaCompuestaTiempo.register(es_numero)
      validacion_fraccion=ventanaCompuestaTiempo.register(es_decimal)

      #Valor presente 
      valor_label = ttk.Label(ventanaCompuestaTiempo, text="Valor Presente:",font=Title_font,background='White')
      valor_label.pack(pady=5)
      valor_entry_p = ttk.Entry(ventanaCompuestaTiempo, width=30, validate='key', validatecommand=(validacion_cantidad, "%P"))
      valor_entry_p.pack(pady=5)

      #Valor futuro
      valor_label = ttk.Label(ventanaCompuestaTiempo, text="Valor Futuro:",font=Title_font,background='White')
      valor_label.pack(pady=5)
      valor_entry_f = ttk.Entry(ventanaCompuestaTiempo, width=30, validate='key', validatecommand=(validacion_cantidad, "%P"))
      valor_entry_f.pack(pady=5)

      
      #Tasa
      
      valor_label_tasa = ttk.Label(ventanaCompuestaTiempo, text="Tasa en decimal ej:0.10->10%",font=Title_font,background='White')
      valor_label_tasa.pack(pady=5)
      valor_entry_tasa = ttk.Entry(ventanaCompuestaTiempo, width=30, validate='key', validatecommand=(validacion_fraccion, "%P"))
      valor_entry_tasa.pack(pady=5)
      #Tipo de tasa
      tipo_tasa = ttk.Combobox(ventanaCompuestaTiempo, values=["Efectiva", "Nominal"], state="readonly", width=10)
      tipo_tasa.pack()

      periodo_tasa = ttk.Combobox(ventanaCompuestaTiempo, values=["M", "B", "T", "C", "S", "A"], state="readonly", width=5)
      periodo_tasa.pack()

      output_label = ttk.Label(ventanaCompuestaTiempo, text="", background='white')
      output_label.pack(pady=10)

      continue_button = ttk.Button(ventanaCompuestaTiempo, text="Continuar", 
                                    command=lambda:Calcular_Tiempo_Compuesto(valor_entry_p, valor_entry_f,valor_entry_tasa, tipo_tasa, periodo_tasa, output_label))
      
      #Calcular_Tiempo_Compuesto(int(valor presente), int(valor_futuro), int(valor_tasa), tipo_tasa.get(), periodo_tasa.get(), output_label))
      continue_button.pack(pady=10)
      
      #Botón volver a la ventana Anterior
      back_button = ttk.Button(ventanaCompuestaTiempo, text="Volver a la ventana Anterior", command=lambda: (ventanaCompuestaTiempo.withdraw(), ventanaCompuestaTiempo.destroy(), InteresCompuesta()))
      back_button.pack(pady=10)

      #Boton para volver al Menu Principal
      back_menu_principal = ttk.Button(ventanaCompuestaTiempo, text="Volver al menu principal", command=lambda:(ventanaCompuestaTiempo.withdraw(), ventanaCompuestaTiempo.destroy(), menu_principal()))
      back_menu_principal.pack(pady=10)
      ventanaCompuestaTiempo.mainloop()

##Interés Compuesto Tasa ###

def InteresCompuestoTasa():
      global ventanaCompuestaTasa
      ventanaCompuestaTasa = tk.Tk()
      ventanaCompuestaTasa.title("Intéres compuesto Tasa de interés")
      ventanaCompuestaTasa.geometry("500x400")

      fondo_imagen = tk.PhotoImage(file=resource_path("fondo.png"))
      fondo_label = tk.Label(ventanaCompuestaTasa, image=fondo_imagen)
      fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
      
      validacion_cantidad=ventanaCompuestaTasa.register(es_numero)
      validacion_fraccion=ventanaCompuestaTasa.register(es_decimal)

       #Valor presente 
      valor_label = ttk.Label(ventanaCompuestaTasa, text="Valor Presente:",font=Title_font,background='White')
      valor_label.pack(pady=5)
      valor_entry_p = ttk.Entry(ventanaCompuestaTasa, width=30, validate='key', validatecommand=(validacion_cantidad, "%P"))
      valor_entry_p.pack(pady=5)

      #Valor futuro
      valor_label = ttk.Label(ventanaCompuestaTasa, text="Valor Futuro:",font=Title_font,background='White')
      valor_label.pack(pady=5)
      valor_entry_f = ttk.Entry(ventanaCompuestaTasa, width=30, validate='key', validatecommand=(validacion_cantidad, "%P"))
      valor_entry_f.pack(pady=5)

      #Tiempo
      valor_label = ttk.Label(ventanaCompuestaTasa, text="Periodo (n)",font=Title_font,background='White')
      valor_label.pack(pady=5)
      valor_entry_n = ttk.Entry(ventanaCompuestaTasa, width=30, validate='key', validatecommand=(validacion_cantidad, "%P"))
      valor_entry_n.pack(pady=5)

      periodo_n = ttk.Combobox(ventanaCompuestaTasa, values=["M", "B", "T", "C", "S", "A"], state="readonly", width=5)
      periodo_n.pack(pady=5)

      output_label = ttk.Label(ventanaCompuestaTasa, text="", background='white')
      output_label.pack(pady=10)

      #Botones 
      continue_button = ttk.Button(ventanaCompuestaTasa, text="Continuar", 
                                    command=lambda:Calcular_Tasa_Compuesto(valor_entry_p, valor_entry_f,valor_entry_n, periodo_n, output_label))
      
      
      continue_button.pack(pady=10)
      
      #Botón volver a la ventana Anterior
      back_button = ttk.Button(ventanaCompuestaTasa, text="Volver a la ventana Anterior", command=lambda: (ventanaCompuestaTasa.withdraw(), ventanaCompuestaTasa.destroy(), InteresCompuesta()))
      back_button.pack(pady=10)

      #Boton para volver al Menu Principal
      back_menu_principal = ttk.Button(ventanaCompuestaTasa, text="Volver al menu principal", command=lambda:(ventanaCompuestaTasa.withdraw(), ventanaCompuestaTasa.destroy(), menu_principal()))
      back_menu_principal.pack(pady=10)
      ventanaCompuestaTasa.mainloop()



def AnualidadPerpetua():
    global ventanaAnualidadPerpetua
    ventanaAnualidadPerpetua = tk.Tk()
    ventanaAnualidadPerpetua.title("Anualidad Perpétua")
    ventanaAnualidadPerpetua.geometry("500x400")

    # Imagen de fondo (debe ser un archivo PNG)
    fondo_imagen = tk.PhotoImage(file=resource_path("fondo.png"))
    fondo_label = tk.Label(ventanaAnualidadPerpetua, image=fondo_imagen)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

    ttk.Label(ventanaAnualidadPerpetua, text="Seleccione el tipo de cálculo:", font=("Arial", 12, "bold"), background='White').pack(pady=5)
    tipo_calculo = ttk.Combobox(ventanaAnualidadPerpetua, values=["Valor Presente (PV)", "Cuota (A)"], state="readonly")
    tipo_calculo.pack(pady=5)

    # Entrada de valor
    ttk.Label(ventanaAnualidadPerpetua, text="Ingrese el valor conocido (PV o A):", font=("Arial", 10), background='White').pack(pady=5)
    valor_entry = ttk.Entry(ventanaAnualidadPerpetua, width=30)
    valor_entry.pack(pady=5)

    # Entrada de tasa
    ttk.Label(ventanaAnualidadPerpetua, text="Ingrese la tasa de interés (decimal):", font=("Arial", 10), background='White').pack(pady=5)
    tasa_entry = ttk.Entry(ventanaAnualidadPerpetua, width=30)
    tasa_entry.pack(pady=5)

    # Output label
    output_label = ttk.Label(ventanaAnualidadPerpetua, text="", background='white', font=("Arial", 12, "bold"))
    output_label.pack(pady=10)

    # Botón para calcular
    calcular_button = ttk.Button(ventanaAnualidadPerpetua, text="Calcular",
                                 command=lambda: Calcular_Anualidad_Perpetua(tipo_calculo.get(), valor_entry.get(), tasa_entry.get(), output_label))
    calcular_button.pack(pady=10)

    #Boton para volver al Menu Principal
    back_menu_principal = ttk.Button(ventanaAnualidadPerpetua, text="Volver al Menú Principal", command=lambda:(ventanaAnualidadPerpetua.withdraw(), ventanaAnualidadPerpetua.destroy(), menu_principal()))
    back_menu_principal.pack(pady=10)
    ventanaAnualidadPerpetua.mainloop()

    ventanaAnualidadPerpetua.mainloop()


def AnualidadVencida():
    global ventanaAnualidadVencida
    ventanaAnualidadVencida = tk.Tk()
    ventanaAnualidadVencida.title("Anualidad Vencida")
    ventanaAnualidadVencida.geometry("500x400")

    # Imagen de fondo (debe ser un archivo PNG)
    fondo_imagen = tk.PhotoImage(file=resource_path("fondo.png"))
    fondo_label = tk.Label(ventanaAnualidadVencida, image=fondo_imagen)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

    ttk.Label(ventanaAnualidadVencida, text="Seleccione el tipo de cálculo:", font=("Arial", 12, "bold"), background='White').pack(pady=5)
    tipo_calculo = ttk.Combobox(ventanaAnualidadVencida, values=["Valor Presente (PV)", "Cuota (A)"], state="readonly")
    tipo_calculo.pack(pady=5)

    # Entrada de valor
    ttk.Label(ventanaAnualidadVencida, text="Ingrese el valor conocido (PV o A):", font=("Arial", 10), background='White').pack(pady=5)
    valor_entry = ttk.Entry(ventanaAnualidadVencida, width=30)
    valor_entry.pack(pady=5)

    # Entrada de tasa
    ttk.Label(ventanaAnualidadVencida, text="Ingrese la tasa de interés (decimal):", font=("Arial", 10), background='White').pack(pady=5)
    tasa_entry = ttk.Entry(ventanaAnualidadVencida, width=30)
    tasa_entry.pack(pady=5)

    # Entrada de número de períodos
    ttk.Label(ventanaAnualidadVencida, text="Ingrese el número de períodos (n):", font=("Arial", 10), background='White').pack(pady=5)
    n_entry = ttk.Entry(ventanaAnualidadVencida, width=30)
    n_entry.pack(pady=5)

    # Output label
    output_label = ttk.Label(ventanaAnualidadVencida, text="", background='white', font=("Arial", 12, "bold"))
    output_label.pack(pady=10)

    # Botón para calcular
    calcular_button = ttk.Button(ventanaAnualidadVencida, text="Calcular",
                                 command=lambda: Calcular_Anualidad_Vencida(tipo_calculo.get(), valor_entry.get(), tasa_entry.get(), n_entry.get(), output_label))
    calcular_button.pack(pady=10)

    #Boton para volver al Menu Principal
    back_menu_principal = ttk.Button(ventanaAnualidadVencida, text="Volver al Menú Principal", command=lambda:(ventanaAnualidadVencida.withdraw(), ventanaAnualidadVencida.destroy(), menu_principal()))
    back_menu_principal.pack(pady=10)
    ventanaAnualidadVencida.mainloop()

    ventanaAnualidadVencida.mainloop()



def AnualidadAnticipada():
    global ventanaAnualidadAnticipada
    ventanaAnualidadAnticipada = tk.Tk()
    ventanaAnualidadAnticipada.title("Anualidad Anticipada")
    ventanaAnualidadAnticipada.geometry("500x400")

    # Imagen de fondo (debe ser un archivo PNG)
    fondo_imagen = tk.PhotoImage(file=resource_path("fondo.png"))
    fondo_label = tk.Label(ventanaAnualidadAnticipada, image=fondo_imagen)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

    ttk.Label(ventanaAnualidadAnticipada, text="Seleccione el tipo de cálculo:", font=("Arial", 12, "bold"), background='White').pack(pady=5)
    tipo_calculo = ttk.Combobox(ventanaAnualidadAnticipada, values=["Valor Presente (PV)", "Cuota (A)"], state="readonly")
    tipo_calculo.pack(pady=5)

    # Entrada de valor
    ttk.Label(ventanaAnualidadAnticipada, text="Ingrese el valor conocido (PV o A):", font=("Arial", 10), background='White').pack(pady=5)
    valor_entry = ttk.Entry(ventanaAnualidadAnticipada, width=30)
    valor_entry.pack(pady=5)

    # Entrada de tasa
    ttk.Label(ventanaAnualidadAnticipada, text="Ingrese la tasa de interés (decimal):", font=("Arial", 10), background='White').pack(pady=5)
    tasa_entry = ttk.Entry(ventanaAnualidadAnticipada, width=30)
    tasa_entry.pack(pady=5)

    # Entrada de número de períodos
    ttk.Label(ventanaAnualidadAnticipada, text="Ingrese el número de períodos (n):", font=("Arial", 10), background='White').pack(pady=5)
    n_entry = ttk.Entry(ventanaAnualidadAnticipada, width=30)
    n_entry.pack(pady=5)

    # Output label
    output_label = ttk.Label(ventanaAnualidadAnticipada, text="", background='white', font=("Arial", 12, "bold"))
    output_label.pack(pady=10)

    # Botón para calcular
    calcular_button = ttk.Button(ventanaAnualidadAnticipada, text="Calcular",
                                 command=lambda: Calcular_Anualidad_Anticipada(tipo_calculo.get(), valor_entry.get(), tasa_entry.get(), n_entry.get(), output_label))
    calcular_button.pack(pady=10)

    # Botón para volver al menú principal
    back_menu_principal = ttk.Button(ventanaAnualidadAnticipada, text="Volver al Menú Principal", command=lambda:(ventanaAnualidadAnticipada.withdraw(), ventanaAnualidadAnticipada.destroy(), menu_principal()))
    back_menu_principal.pack(pady=10)

    ventanaAnualidadAnticipada.mainloop()



########################################################################################################################################################################################

def Calcular_Anualidad_Perpetua(tipo_calculo, valor, tasa, output_label):
    """Realiza el cálculo de la anualidad perpetua según la opción elegida."""
    try:
        valor = float(valor)
        tasa = float(tasa)

        if tasa <= 0:
            output_label.config(text="La tasa debe ser mayor que 0", foreground="red")
            return

        if tipo_calculo == "Valor Presente (PV)":
            resultado = valor / tasa  # PV = A / r
            output_label.config(text=f"Valor Presente (PV): {resultado:.2f}", foreground="green")
        elif tipo_calculo == "Cuota (A)":
            resultado = valor * tasa  # A = PV * r
            output_label.config(text=f"Cuota de la Anualidad (A): {resultado:.2f}", foreground="green")
        else:
            output_label.config(text="Seleccione un tipo de cálculo", foreground="red")
    except ValueError:
        output_label.config(text="Ingrese valores numéricos válidos", foreground="red")


def es_numero(valor):
    """Valida si el valor ingresado es un número."""
    try:
        float(valor)
        return True
    except ValueError:
        return False



def Calcular_Anualidad_Vencida(tipo_calculo, valor, tasa, n, output_label):
    """Realiza el cálculo de la anualidad vencida."""
    try:
        valor = float(valor)
        tasa = float(tasa)
        n = int(n)

        if tasa <= 0 or n <= 0:
            output_label.config(text="La tasa y el número de períodos deben ser mayores que 0", foreground="red")
            return

        if tipo_calculo == "Valor Presente (PV)":
            resultado = valor*((1-(1+tasa)**(-n))/tasa)
            output_label.config(text=f"Valor Presente (PV): {resultado:.2f}", foreground="green")
        elif tipo_calculo == "Cuota (A)":
            #resultado = valor*(((1-(1+tasa)**(n))-1)/tasa)
            resultado = valor * (tasa / (1 - (1 + tasa) ** -n))
            output_label.config(text=f"Cuota de la Anualidad (A): {resultado:.2f}", foreground="green")
        else:
            output_label.config(text="Seleccione un tipo de cálculo", foreground="red")
    except ValueError:
        output_label.config(text="Ingrese valores numéricos válidos", foreground="red")



def Calcular_Anualidad_Anticipada(tipo_calculo, valor, tasa, n, output_label):
    """Realiza el cálculo de la anualidad anticipada."""
    try:
        if not es_numero(valor) or not es_numero(tasa) or not es_numero(n):
            output_label.config(text="Todos los valores deben ser números", foreground="red")
            return

        valor = float(valor)
        tasa = float(tasa)
        n = int(n)

        if tasa <= 0 or n <= 0:
            output_label.config(text="La tasa y el número de períodos deben ser mayores que 0", foreground="red")
            return

        if tipo_calculo == "Valor Presente (PV)":
            resultado = valor * ((1 - (1 + tasa) ** -n) / tasa) * (1 + tasa)
            output_label.config(text=f"Valor Presente (PV): {resultado:.2f}", foreground="green")
        elif tipo_calculo == "Cuota (A)":
            resultado = (valor * tasa) / ((1 - (1 + tasa) ** -n) * (1 + tasa))
            output_label.config(text=f"Cuota de la Anualidad (A): {resultado:.2f}", foreground="green")
        else:
            output_label.config(text="Seleccione un tipo de cálculo", foreground="red")
    except ValueError:
        output_label.config(text="Ingrese valores numéricos válidos", foreground="red")


def Calcular_Amortizacion(prestamo, tasa, num_periodos, output_label):
    """Realiza el cálculo de la tabla de amortización y la muestra en una ventana con Treeview."""
    try:
        if not es_numero(prestamo) or not es_numero(tasa) or not es_numero(num_periodos):
            output_label.config(text="Todos los valores deben ser números", foreground="red")
            return

        prestamo = float(prestamo)
        tasa = float(tasa)
        num_periodos = int(num_periodos)

        if prestamo <= 0 or tasa <= 0 or num_periodos <= 0:
            output_label.config(text="Todos los valores deben ser mayores que 0", foreground="red")
            return

        # Calcular cuota fija
        cuota = prestamo * (tasa / (1 - (1 + tasa) ** -num_periodos))

        # Inicializar variables
        saldo = prestamo
        tabla = []

        for periodo in range(1, num_periodos + 1):
            interes = saldo * tasa
            capital = cuota - interes
            saldo -= capital
            tabla.append([periodo, round(cuota, 2), round(interes, 2), round(capital, 2), round(saldo, 2)])

        # Crear una nueva ventana para la tabla de amortización
        nueva_ventana = tk.Toplevel()
        nueva_ventana.title("Tabla de Amortización")
        nueva_ventana.geometry("600x400")

        # Crear el Treeview (tabla)
        columnas = ("Periodo", "Cuota", "Interés", "Capital", "Saldo")
        tabla_tree = ttk.Treeview(nueva_ventana, columns=columnas, show="headings")

        # Configurar encabezados
        for col in columnas:
            tabla_tree.heading(col, text=col)
            tabla_tree.column(col, width=100, anchor="center")

        # Insertar datos en la tabla
        for fila in tabla:
            tabla_tree.insert("", "end", values=fila)

        tabla_tree.pack(expand=True, fill="both")

        output_label.config(text=f"Cuota: {round(cuota, 2)}", foreground="green")
    except Exception as e:
        messagebox.showerror("Error", f"Ha ocurrido un error: {str(e)}")



########################################################################################################################################################################################

    


#### Sección de calculos Interes compuesto#####
def Calcular_Valor_Compuesto(calc_type, valor_entry,  valor_entry_tasa, tipo_tasa, periodo_tasa, valor_entry_n,periodo_n,output_label):
     if not calc_type.get() or not valor_entry or not valor_entry_tasa or not tipo_tasa or not periodo_tasa or not valor_entry_n or not periodo_n or not output_label:
          output_label.configure(text="Todos los valores deben ser ingresados")
     else:
            if tipo_tasa == "Nominal" :
                if periodo_tasa == "M":
                    valor_entry_tasa = convertirJI(0,float(valor_entry_tasa),2,12)
                elif periodo_tasa == "B":
                    valor_entry_tasa = convertirJI(0,float(valor_entry_tasa),2,6)             
                elif periodo_tasa == "T":
                    valor_entry_tasa = convertirJI(0,float(valor_entry_tasa),2,4)          
                elif periodo_tasa == "C":
                    valor_entry_tasa = convertirJI(0,float(valor_entry_tasa),2,3)              
                elif periodo_tasa == "S":
                    valor_entry_tasa = convertirJI(0,float(valor_entry_tasa),2,2)            
                elif periodo_tasa == "A":
                    valor_entry_tasa = convertirJI(0,float(valor_entry_tasa),2,1)
                
                valor_entry_n=Cambiar_n(int(valor_entry_n),periodo_tasa,periodo_n)

                if calc_type.get() == "Valor Presente":
                    nuevo_valor=round(float(interesCompuestoP(float(valor_entry),float(valor_entry_tasa),int(valor_entry_n))),3)
                    resultado=(f"El valor presente es = {nuevo_valor} en periodos {periodo_tasa}")
                    output_label.config(text= resultado)                
                else:
                    nuevo_valor=round(float(interesCompuesto(float(valor_entry),float(valor_entry_tasa),int(valor_entry_n))),3)
                    resultado=(f"El valor futuro es = {nuevo_valor} en periodos {periodo_tasa}")
                    output_label.config(text=resultado)
            else:
                 valor_entry_n=Cambiar_n(int(valor_entry_n),periodo_tasa,periodo_n)
                 if calc_type.get() == "Valor Presente":
                    nuevo_valor=round(float(interesCompuestoP(float(valor_entry),float(valor_entry_tasa),int(valor_entry_n))),3)
                    resultado=(f"El valor presente es = {nuevo_valor} en periodos {periodo_tasa}")
                    output_label.config(text= resultado)                
                 else:
                    nuevo_valor=round(float(interesCompuesto(float(valor_entry),float(valor_entry_tasa),int(valor_entry_n))),3)
                    resultado=(f"El valor futuro es = {nuevo_valor} en periodos {periodo_tasa}")
                    output_label.config(text=resultado)
                 
def Calcular_Tiempo_Compuesto(valor_presente,valor_futuro,valor_entry_tasa,tipo_tasa,periodo_tasa,output_label):
     
     if not valor_presente.get() or not valor_futuro.get() or not valor_entry_tasa.get() or not tipo_tasa.get() or not periodo_tasa.get():
            output_label.config(text="Todos los valores deben ser ingresados")
     else:
            if tipo_tasa.get() =='Nominal':
                if periodo_tasa.get() == "M":
                    valor_entry_tasa = convertirJI(0,float(valor_entry_tasa.get()),2,12)
                elif periodo_tasa.get() == "B":
                    valor_entry_tasa = convertirJI(0,float(valor_entry_tasa.get()),2,6)             
                elif periodo_tasa.get() == "T":
                   valor_entry_tasa = convertirJI(0,float(valor_entry_tasa.get()),2,4)          
                elif periodo_tasa.get() == "C":
                    valor_entry_tasa = convertirJI(0,float(valor_entry_tasa.get()),2,3)              
                elif periodo_tasa.get() == "S":
                    valor_entry_tasa = convertirJI(0,float(valor_entry_tasa.get()),2,2)            
                elif periodo_tasa.get() == "A":
                    valor_entry_tasa = convertirJI(0,float(valor_entry_tasa.get()),2,1)

                valor_respuesta=round(interesCompuestoN(float(valor_futuro.get()),float(valor_presente.get()),float(valor_entry_tasa)))
                respuesta = (f'El valor de n es = {valor_respuesta} en periodos de {periodo_tasa.get()}')
                output_label.config(text=respuesta)
            else:
                valor_respuesta=round(interesCompuestoN(float(valor_futuro.get()),float(valor_presente.get()),float(valor_entry_tasa)))
                respuesta = (f'El valor de n es = {valor_respuesta} en periodos de {periodo_tasa.get()}')
                output_label.config(text=respuesta)
            
def Calcular_Tasa_Compuesto(valor_entry_p, valor_entry_f,valor_entry_n, periodo_n, output_label):
     
    if not valor_entry_p.get() or not valor_entry_f.get() or not valor_entry_n.get() or not periodo_n.get():
                output_label.config(text="Todos los valores deben ser ingresados")
    else:
         
         nueva_tasa=round(interesCompuestoI(float(valor_entry_f.get()),float(valor_entry_p.get()),int(valor_entry_n.get())),2)
         respuesta = (f'El valor de la tasa es de {nueva_tasa} % en periodos {periodo_n.get()}')
         output_label.config(text=respuesta) 




############################################## EQUIVALENCIA DE TASAS #######################################################################

def Conversión_Tasas():
        global ventanaEConversionTasas
        ventanaEConversionTasas = tk.Tk()
        ventanaEConversionTasas.title("Conversión de Tasas de interés")
        ventanaEConversionTasas.geometry("500x400")
        
        fondo_imagen = tk.PhotoImage(file=resource_path("fondo.png"))
        fondo_label = tk.Label(ventanaEConversionTasas, image=fondo_imagen)
        fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

        
        validacion_cantidad=ventanaEConversionTasas.register(es_numero)
        validacion_fraccion=ventanaEConversionTasas.register(es_decimal)

        #Tasa 1
        valor_label_tasa_1 = ttk.Label(ventanaEConversionTasas, text="Tasa 1 en decimal ej:0.10->10%",font=Title_font,background='White')
        valor_label_tasa_1.pack(pady=5)
        valor_entry_tasa_1 = ttk.Entry(ventanaEConversionTasas, width=30, validate='key', validatecommand=(validacion_fraccion, "%P"))
        valor_entry_tasa_1.pack(pady=5)
        #Tipo de tasa 1
        tipo_tasa_1 = ttk.Combobox(ventanaEConversionTasas, values=["Efectiva", "Nominal","Efectiva Anticipada","Nominal Anticipada"], state="readonly", width=10)
        tipo_tasa_1.pack()
        #Periodo de tasa 1
        periodo_tasa_1 = ttk.Combobox(ventanaEConversionTasas, values=["M", "B", "T", "C", "S", "A"], state="readonly", width=5)
        periodo_tasa_1.pack()

        labela = ttk.Label(ventanaEConversionTasas, text="Convertir a: ",font=Title_font,background='White')
        labela.pack(pady=5)

        #Tasa 2
        #Tipo de tasa 2
        tipo_tasa_2 = ttk.Combobox(ventanaEConversionTasas, values=["Efectiva", "Nominal","Efectiva Anticipada","Nominal Anticipada"], state="readonly", width=10)
        tipo_tasa_2.pack()
        #Periodo de tasa 2
        periodo_tasa_2 = ttk.Combobox(ventanaEConversionTasas, values=["M", "B", "T", "C", "S", "A"], state="readonly", width=5)
        periodo_tasa_2.pack()

        output_label = ttk.Label(ventanaEConversionTasas, text="", background='white')
        output_label.pack(pady=10)

        #Botón continuar 
        continue_button = ttk.Button(ventanaEConversionTasas, text="Calcular", 
                                    command=lambda:Calcular_conversion_tasa(valor_entry_tasa_1,tipo_tasa_1,periodo_tasa_1, tipo_tasa_2,periodo_tasa_2,output_label))
      
        continue_button.pack(pady=10)

        #Botón de volver al menu principal
        back_menu_principal = ttk.Button(ventanaEConversionTasas, text="Volver al menu principal", command=lambda:(ventanaEConversionTasas.withdraw(), ventanaEConversionTasas.destroy(), menu_principal()))
        back_menu_principal.pack(pady=10)

        ventanaEConversionTasas.mainloop()

def Calcular_conversion_tasa(valor_entry_tasa_1,tipo_tasa_1,periodo_tasa_1, tipo_tasa_2,periodo_tasa_2,output_label):
      conversiones = {
            'M': 12,  # Mensual
            'B': 6,   # Bimestral
            'T': 4,   # Trimestral
            'C': 3,   # Cuatrimestral
            'S': 2,   # Semestral
            'A': 1    # Anual
        }
      if not valor_entry_tasa_1.get() or not tipo_tasa_1.get() or not periodo_tasa_1.get() or not tipo_tasa_2.get() or not periodo_tasa_2.get():
            output_label.config(text="Todas las entradas deben indicarse")
      else:
           if tipo_tasa_1.get() == 'Nominal Anticipada':
                tasa = convertirJI(0,float(valor_entry_tasa_1.get()),2,conversiones[periodo_tasa_1.get()])
                tasa = convertirIA(0,tasa,2)
                tasaO = equivalenciaTasas(tasa,conversiones[periodo_tasa_1.get()],conversiones[periodo_tasa_2.get()])
                if tipo_tasa_2.get()== 'Nominal Anticipada':
                    tasaO = convertirIA(tasaO,0,1)
                    tasaO = convertirJI(tasaO,0,1,conversiones[periodo_tasa_2.get()])
                elif tipo_tasa_2.get() == 'Nominal':
                    tasaO = convertirJI(tasaO,0,1,conversiones[periodo_tasa_2.get()])
                elif tipo_tasa_2.get() == 'Efectiva Anticipada':
                    tasaO = convertirIA(tasaO,0,1)                    
                output_label.config(text=f"La equivalencia de la tasa {float(valor_entry_tasa_1.get())*100} % {tipo_tasa_1.get()} {periodo_tasa_1.get()} es {round(tasaO*100,2)} % {tipo_tasa_2.get()} {periodo_tasa_2.get()}")
           


           elif tipo_tasa_1.get() == 'Nominal':                
                tasa = convertirJI(0,float(valor_entry_tasa_1.get()),2,conversiones[periodo_tasa_1.get()])
                tasaO = equivalenciaTasas(tasa,conversiones[periodo_tasa_1.get()],conversiones[periodo_tasa_2.get()])
                if tipo_tasa_2.get() == "Nominal":
                    tasaO = convertirJI(tasaO,0,1,conversiones[periodo_tasa_2.get()])
                elif tipo_tasa_2.get() == 'Efectiva Anticipada':
                    tasaO = convertirIA(tasaO,0,1)
                elif tipo_tasa_2.get()== 'Nominal Anticipada':
                    tasaO = convertirIA(tasaO,0,1)
                    tasaO = convertirJI(tasaO,0,1,conversiones[periodo_tasa_2.get()])
                output_label.config(text=f"La equivalencia de la tasa {float(valor_entry_tasa_1.get())*100} % {tipo_tasa_1.get()} {periodo_tasa_1.get()} es {round(tasaO*100,2)} % {tipo_tasa_2.get()} {periodo_tasa_2.get()}")
           

           elif tipo_tasa_1.get() == 'Efectiva Anticipada':
                tasa = convertirIA(0,float(valor_entry_tasa_1.get()),2)
                tasaO = equivalenciaTasas(tasa,conversiones[periodo_tasa_1.get()],conversiones[periodo_tasa_2.get()])
                if tipo_tasa_2.get() == "Nominal":
                    tasaO = convertirJI(tasaO,0,1,conversiones[periodo_tasa_2.get()])
                elif tipo_tasa_2.get() == 'Efectiva Anticipada':
                    tasaO = convertirIA(tasaO,0,1)
                elif tipo_tasa_2.get() == 'Nominal Anticipada':
                    tasaO = convertirIA(tasaO,0,1)
                    tasaO = convertirJI(tasaO,0,1,conversiones[periodo_tasa_2.get()])
                output_label.config(text=f"La equivalencia de la tasa {float(valor_entry_tasa_1.get())*100} % {tipo_tasa_1.get()} {periodo_tasa_1.get()} es {round(tasaO*100,2)} % {tipo_tasa_2.get()} {periodo_tasa_2.get()}")
           
           else:
                tasaO = equivalenciaTasas(float(valor_entry_tasa_1.get()),conversiones[periodo_tasa_1.get()],conversiones[periodo_tasa_2.get()])
                if tipo_tasa_2.get() == "Nominal":
                    tasaO = convertirJI(tasaO,0,1,conversiones[periodo_tasa_2.get()])
                elif tipo_tasa_2.get() == 'Efectiva Anticipada':
                    tasaO = convertirIA(tasaO,0,1)
                elif tipo_tasa_2.get() == 'Nominal Anticipada':
                    tasaO = convertirIA(tasaO,0,1)
                    tasaO = convertirJI(tasaO,0,1,conversiones[periodo_tasa_2.get()])
                output_label.config(text=f"La equivalencia de la tasa {float(valor_entry_tasa_1.get())*100} % {tipo_tasa_1.get()} {periodo_tasa_1.get()} es {round(tasaO*100,2)} % {tipo_tasa_2.get()} {periodo_tasa_2.get()}")
           


menu_principal()
