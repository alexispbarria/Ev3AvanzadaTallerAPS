import tkinter as tk
from tkinter.font import BOLD
from tkinter import ttk, messagebox
from pytz import common_timezones
import conexion
import util.generic as utl
from ..trabajador import form_trabajador as ft
from ..trabajador import pasajeros as p
from ..trabajador import iti as i
import yang.correoenvio as correo


class pasajes:

    def verificarDisponibilidadPasaje(self):
        #Configuración básica de la ventana
        self.ventana = tk.Tk()                             
        self.ventana.title('Gestionar Pasajes Aereos')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)

        wrapper1 = tk.LabelFrame(self.ventana)

        mycanvas = tk.Canvas(wrapper1, background="#fcfcfc")
        mycanvas.pack(side=tk.LEFT, fill='both', expand=tk.YES)

        yscrollbar = ttk.Scrollbar(wrapper1, orient="vertical", command=mycanvas.yview)
        yscrollbar.pack(side=tk.RIGHT, fill="y")

        mycanvas.configure(yscrollcommand=yscrollbar.set)

        mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion= mycanvas.bbox('all')))

        #FRAME PRINCIPAL
        myframe = tk.Frame(mycanvas, bg="#fcfcfc")
        mycanvas.create_window((0, 0), window=myframe, width=w)

        wrapper1.pack(fill="both", expand="yes", padx=10, pady=10)

        #titulo de la pagina
        title = tk.Label(myframe, text= "Realizar Venta de Pasajes Aereos", font=('Times', 30, BOLD), fg='#fcfcfc', bg="#3a7ff6", pady=50)
        title.pack(expand=tk.NO, fill=tk.BOTH)

        #logo bajo el titulo
        logo = utl.leer_imagen("./imagenes/logo.png", (200, 200))
        labelLogo = tk.Label(myframe, image=logo, bg='#fcfcfc')
        labelLogo.pack(fill=tk.X, padx=20, pady=10)

         
        frame_form_access = tk.Frame(myframe, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_access.pack(side="top", expand=tk.NO, fill=tk.NONE)

        self.etiqueta_fecha = tk.Label(frame_form_access, text="Inserte la fecha del vuelo deseado", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        self.etiqueta_fecha.pack(fill=tk.X, padx=20, pady=5)
        self.fechaBuscar = ttk.Entry(frame_form_access, font=('Times', 14))
        self.fechaBuscar.insert(0, "  -  -    ")
        self.fechaBuscar.pack(fill=tk.BOTH, padx=20, pady=10)

        self.etiqueta_tramo = tk.Label(frame_form_access, text="Inserte el origen del tramo", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        self.etiqueta_tramo.pack(fill=tk.X, padx=20, pady=5)
        self.buscarTramo = ttk.Entry(frame_form_access, font=('Times', 14))
        self.buscarTramo.pack(fill=tk.BOTH, padx=20, pady=10)

        #boton verificar
        self.verificarVuelo =  tk.Button(frame_form_access, text="Verificar Disponibilidad", font=('Times', 14, BOLD), bg='#3a7ff6', bd=0, fg="#fff", command=self.botonVerificarDisponibilidad)
        self.verificarVuelo.pack(fill=tk.X, padx=20, pady=20)
        self.verificarVuelo.bind("<Return>", (lambda event: self.botonVerificarDisponibilidad()))

        #Label y Entry ocultos, aparecen solo cuando existe disponibilidad de vuelo.
        self.etiqueta_documento = tk.Label(frame_form_access, text="Inserte el Documento del Pasajero", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        self.etiqueta_documento.pack_forget()
        self.buscarDocumento = ttk.Entry(frame_form_access, font=('Times', 14))
        self.buscarDocumento.insert(8, "-")
        self.buscarDocumento.pack_forget()

        self.verificarRegistroPasajero =  tk.Button(frame_form_access, text="Verificar registro del pasajero", font=('Times', 14, BOLD), bg='#3a7ff6', bd=0, fg="#fff", command=self.botonVerificarRegistroPasajero)
        self.verificarRegistroPasajero.pack_forget()
        self.verificarRegistroPasajero.bind("<Return>", (lambda event: self.botonVerificarRegistroPasajero()))

        #Label y Entry ocultos, aparecen solo cuando existe disponibilidad de vuelo.
        self.etiqueta_numeroVenta = tk.Label(frame_form_access, text="Inserte el número de venta", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        self.etiqueta_numeroVenta.pack_forget()
        self.nroVenta = ttk.Entry(frame_form_access, font=('Times', 14))
        self.nroVenta.pack_forget()

        #NUEVO NOMBRE
        self.etiqueta_nuevoNombrePax = tk.Label(frame_form_access, text="Inserte nombre del pasajero", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        self.etiqueta_nuevoNombrePax.pack_forget()
        self.nuevoNombrePax = ttk.Entry(frame_form_access, font=('Times', 14))
        self.nuevoNombrePax.pack_forget()

        #NUEVO APELLIDO
        self.etiqueta_nuevoApellidoPax = tk.Label(frame_form_access, text="Inserte apellido del pasajero", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        self.etiqueta_nuevoApellidoPax.pack_forget()
        self.nuevoApellidoPax = ttk.Entry(frame_form_access, font=('Times', 14))
        self.nuevoApellidoPax.pack_forget()

        #nueva nacionalidad
        self.etiqueta_nuevaNacionalidadPax = tk.Label(frame_form_access, text="Inserte nacionalidad del pasajero", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        self.etiqueta_nuevaNacionalidadPax.pack_forget()
        self.nuevaNacionalidadPax = ttk.Entry(frame_form_access, font=('Times', 14))
        self.nuevaNacionalidadPax.pack_forget()

        #nueva fecha de nacimiento
        fechaNuevaEntry = tk.StringVar()
        fechaNuevaEntry.set("formato dd-mm-aaaa")
        self.etiqueta_nuevaFechaNace = tk.Label(frame_form_access, text="Inserte fecha de nacimiento del pasajero", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        self.etiqueta_nuevaFechaNace.pack_forget()
        self.nuevaFechaNacePax = ttk.Entry(frame_form_access, font=('Times', 14), textvariable=fechaNuevaEntry)
        self.nuevaFechaNacePax.pack_forget()

        #nuevo genero
        self.etiqueta_nuevoGenero = tk.Label(frame_form_access, text="Inserte genero del pasajero", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        self.etiqueta_nuevoGenero.pack_forget()
        self.nuevoGeneroPax = ttk.Entry(frame_form_access, font=('Times', 14))
        self.nuevoGeneroPax.pack_forget()

        #nuevo mail
        self.etiqueta_nuevoEmail = tk.Label(frame_form_access, text="Inserte email del pasajero", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        self.etiqueta_nuevoEmail.pack_forget()
        self.nuevoEmailPax = ttk.Entry(frame_form_access, font=('Times', 14))
        self.nuevoEmailPax.pack_forget()

        #nuevo fono
        self.etiqueta_nuevoFono = tk.Label(frame_form_access, text="Inserte teléfono del pasajero", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        self.etiqueta_nuevoFono.pack_forget()
        self.nuevoFonoPax = ttk.Entry(frame_form_access, font=('Times', 14))
        self.nuevoFonoPax.pack_forget()

        self.agregarVenta =  tk.Button(frame_form_access, text="Realizar Venta", font=('Times', 14, BOLD), bg='#3a7ff6', bd=0, fg="#fff", command=self.botonRealizarVenta)
        self.agregarVenta.pack_forget()
        self.agregarVenta.bind("<Return>", (lambda event: self.botonRealizarVenta()))

        #Volver al menú anterior
        self.volver = tk.Button(frame_form_access, text="Volver al Menú Anterior", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirGestionPasajesAereos)
        self.volver.pack(fill=tk.X, padx=20, pady=20)
        self.volver.bind("<Return>", (lambda event: self.abrirGestionPasajesAereos()))

        #SEPARADOR
        for i in range (25):
            tk.Label(myframe, text="", bg="#fcfcfc").pack()



        self.ventana.mainloop()


    def visualizarPasajes(self):
        #Configuración básica de la ventana
        self.ventana = tk.Tk()                             
        self.ventana.title('Visualizar Pasajes')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        #frame para el título.
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_form.pack(expand=tk.YES, fill=tk.BOTH)

        #Frame superior, ocupado por el texto Menú administrador.
        frame_form_top = tk.Frame(frame_form, height=20, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack (side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text= "Visualizar Pasajes", font=('Times', 30, BOLD), fg='#fcfcfc', bg="#3a7ff6", pady=50)
        title.pack(expand=tk.NO, fill=tk.BOTH)

        #Botones de acceso.
        frame_form_access = tk.Frame(frame_form, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_access.pack(side="bottom", expand=tk.YES, fill=tk.Y)

        #Imágen
        logo = utl.leer_imagen("./imagenes/logo.png", (200, 200))
        labelLogo = tk.Label(frame_form_access, image=logo, bg='#fcfcfc')
        labelLogo.pack(fill=tk.X, padx=20, pady=10)

        totalPasajes = tk.Button(frame_form_access, text="Visualizar total de pasajes vendidos", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirVisualizarTotalPasajes)
        totalPasajes.pack(fill=tk.X, padx=20, pady=20)
        totalPasajes.bind("<Return>", (lambda event: self.abrirVisualizarTotalPasajes()))

        pasajePorCodigo = tk.Button(frame_form_access, text="Visualizar pasaje según código de Vuelo", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirVisualizarPasajePorCodigoVuelo)
        pasajePorCodigo.pack(fill=tk.X, padx=20, pady=20)
        pasajePorCodigo.bind("<Return>", (lambda event: self.abrirVisualizarPasajePorCodigoVuelo()))

        pasajePorDocumento = tk.Button(frame_form_access, text="Visualizar pasaje según documento del pasajero.", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirVisualizarPasajePorDocumento)
        pasajePorDocumento.pack(fill=tk.X, padx=20, pady=20)
        pasajePorDocumento.bind("<Return>", (lambda event: self.abrirVisualizarPasajePorDocumento()))

        pasajePorFecha = tk.Button(frame_form_access, text="Visualizar pasaje según fecha de Vuelo", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirVisualizarPasajePorFecha)
        pasajePorFecha.pack(fill=tk.X, padx=20, pady=20)
        pasajePorFecha.bind("<Return>", (lambda event: self.abrirVisualizarPasajePorFecha()))

        pasajePorVenta = tk.Button(frame_form_access, text="Visualizar pasaje según código de venta", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirVisualizarPasajePorVenta)
        pasajePorVenta.pack(fill=tk.X, padx=20, pady=20)
        pasajePorVenta.bind("<Return>", (lambda event: self.abrirVisualizarPasajePorVenta()))

        #Volver al menú anterior
        self.volver = tk.Button(frame_form_access, text="Volver al Menú Anterior", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirGestionPasajesAereos)
        self.volver.pack(fill=tk.X, padx=20, pady=20)
        self.volver.bind("<Return>", (lambda event: self.abrirGestionPasajesAereos()))


        self.ventana.mainloop()


    def visualizarTotalPasajes(self):
        db = conexion.get_db()

        #Configuración básica de la ventana
        self.ventana = tk.Tk()                             
        self.ventana.title('Total de Pasajes Aereos')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        #frame para el título.
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_form.pack(expand=tk.NO, fill=tk.BOTH)

        #Frame superior, ocupado por el texto Menú administrador.
        frame_form_top = tk.Frame(frame_form, height=20, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack (side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text= "Total de Pasajes Vendidos", font=('Times', 30, BOLD), fg='#fcfcfc', bg="#3a7ff6", pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        #Botones de acceso.
        frame_form_access = tk.Frame(frame_form, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_access.pack(side="bottom", expand=tk.YES, fill=tk.NONE)

        logo = utl.leer_imagen("./imagenes/logo.png", (200, 200))
        labelLogo = tk.Label(frame_form_access, image=logo, bg='#fcfcfc')
        labelLogo.pack(fill=tk.X, padx=20, pady=10)


        listado = ttk.Treeview(frame_form_access, columns=('#0', '#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9'))
        listado.pack(fill=tk.X, padx=20, pady=5)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", font=('Times', 14))
        style.configure("Treeview.Heading", font=('Times', 15))

        
        #Nombre de las columnas 
        listado.heading('#0', text="Cod. Venta")
        listado.heading('#1', text="Nombre")
        listado.heading('#2', text="Apellido")
        listado.heading('#3', text="N° Documento")
        listado.heading('#4', text="Cod. vuelo")
        listado.heading('#5', text="Origen")
        listado.heading('#6', text="Destino")
        listado.heading('#7', text="Fecha de Vuelo")
        listado.heading('#8', text="Hora")
        listado.heading('#9', text="Valor")
        listado.heading('#10', text="Email")
        

    

        #Volver al menú anterior
        menuAnterior = tk.Button(frame_form_access, text="Volver al Menú Anterior", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirVisualizarPasajes)
        menuAnterior.pack(fill=tk.X, padx=20, pady=20)
        menuAnterior.bind("<Return>", (lambda event: self.abrirVisualizarPasajes()))

        pasajes = db.ventaPasajes.find({})
        for pasaje in pasajes:
            listado.insert( "", 
                            tk.END,
                            text=pasaje["_id"],
                            values = (pasaje["nombrePax"], pasaje["apellidoPax"], pasaje["pasajeroId"], pasaje["codVuelo"], pasaje["origen"], pasaje["destino"], pasaje["fechaVuelo"], pasaje["horaVuelo"], pasaje["valorTramo"], pasaje["email"])
                            
                            )
            

        self.ventana.mainloop()

    
    def visualizarPasajePorCodVuelo(self):
        #Configuración básica de la ventana
        self.ventana = tk.Tk()                             
        self.ventana.title('Filtrar pasajes por Código')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        #frame para el título.
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_form.pack(expand=tk.NO, fill=tk.BOTH)

        #Frame superior, ocupado por el texto Menú administrador.
        frame_form_top = tk.Frame(frame_form, height=20, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack (side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text= "Pasaje Aereo según código de vuelo", font=('Times', 30, BOLD), fg='#fcfcfc', bg="#3a7ff6", pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        #Botones de acceso.
        frame_form_access = tk.Frame(frame_form, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_access.pack(side="bottom", expand=tk.YES, fill=tk.NONE)

        logo = utl.leer_imagen("./imagenes/logo.png", (200, 200))
        labelLogo = tk.Label(frame_form_access, image=logo, bg='#fcfcfc')
        labelLogo.pack(fill=tk.X, padx=20, pady=10)

        #SOLICITUD DEl codigo del vuelo a consultar
        etiqueta_codigoVuelo = tk.Label(frame_form_access, text="Inserte el código del vuelo del pasaje a buscar", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_codigoVuelo.pack(fill=tk.X, padx=20, pady=5)
        self.pasajeCodVuelo = ttk.Entry(frame_form_access, font=('Times', 14))
        self.pasajeCodVuelo.pack(fill=tk.BOTH, padx=20, pady=10)

        buscarPasajeCod =  tk.Button(frame_form_access, text="Buscar Pasaje", font=('Times', 14, BOLD), bg='#3a7ff6', bd=0, fg="#fff", command=self.botonVisualizarPasajePorCodVuelo)
        buscarPasajeCod.pack(fill=tk.X, padx=20, pady=20)
        buscarPasajeCod.bind("<Return>", (lambda event: self.botonVisualizarPasajePorCodVuelo()))

        self.listado = ttk.Treeview(frame_form_access, columns=('#0', '#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9'))
        self.listado.pack(fill=tk.X, padx=20, pady=5)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", font=('Times', 14))
        style.configure("Treeview.Heading", font=('Times', 15))

        
        #Nombre de las columnas 
        self.listado.heading('#0', text="Cod. Venta")
        self.listado.heading('#1', text="Nombre")
        self.listado.heading('#2', text="Apellido")
        self.listado.heading('#3', text="N° Documento")
        self.listado.heading('#4', text="Cod. vuelo")
        self.listado.heading('#5', text="Origen")
        self.listado.heading('#6', text="Destino")
        self.listado.heading('#7', text="Fecha de Vuelo")
        self.listado.heading('#8', text="Hora")
        self.listado.heading('#9', text="Valor")
        self.listado.heading('#10', text="Email")
        

    

        #Volver al menú anterior
        menuAnterior = tk.Button(frame_form_access, text="Volver al Menú Anterior", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirVisualizarPasajes)
        menuAnterior.pack(fill=tk.X, padx=20, pady=20)
        menuAnterior.bind("<Return>", (lambda event: self.abrirVisualizarPasajes()))

        self.ventana.mainloop()

    def visualizarPasajePorDocumento(self):
        #Configuración básica de la ventana
        self.ventana = tk.Tk()                             
        self.ventana.title('Filtrar pasajes por documento')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        #frame para el título.
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_form.pack(expand=tk.NO, fill=tk.BOTH)

        #Frame superior, ocupado por el texto Menú administrador.
        frame_form_top = tk.Frame(frame_form, height=20, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack (side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text= "Pasaje Aereo según documento del pasajero", font=('Times', 30, BOLD), fg='#fcfcfc', bg="#3a7ff6", pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        #Botones de acceso.
        frame_form_access = tk.Frame(frame_form, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_access.pack(side="bottom", expand=tk.YES, fill=tk.NONE)

        logo = utl.leer_imagen("./imagenes/logo.png", (200, 200))
        labelLogo = tk.Label(frame_form_access, image=logo, bg='#fcfcfc')
        labelLogo.pack(fill=tk.X, padx=20, pady=10)

        
        etiqueta_documentoPax = tk.Label(frame_form_access, text="Inserte el documento o pasaporte del pasajero del pasaje a buscar", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_documentoPax.pack(fill=tk.X, padx=20, pady=5)
        self.pasajeDocumento = ttk.Entry(frame_form_access, font=('Times', 14))
        self.pasajeDocumento.pack(fill=tk.BOTH, padx=20, pady=10)

        buscarPasajeCod =  tk.Button(frame_form_access, text="Buscar Pasaje", font=('Times', 14, BOLD), bg='#3a7ff6', bd=0, fg="#fff", command=self.botonVisualizarPasajePorDocumento)
        buscarPasajeCod.pack(fill=tk.X, padx=20, pady=20)
        buscarPasajeCod.bind("<Return>", (lambda event: self.botonVisualizarPasajePorDocumento()))

        self.listado = ttk.Treeview(frame_form_access, columns=('#0', '#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9'))
        self.listado.pack(fill=tk.X, padx=20, pady=5)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", font=('Times', 14))
        style.configure("Treeview.Heading", font=('Times', 15))

        
        #Nombre de las columnas 
        self.listado.heading('#0', text="Cod. Venta")
        self.listado.heading('#1', text="Nombre")
        self.listado.heading('#2', text="Apellido")
        self.listado.heading('#3', text="N° Documento")
        self.listado.heading('#4', text="Cod. vuelo")
        self.listado.heading('#5', text="Origen")
        self.listado.heading('#6', text="Destino")
        self.listado.heading('#7', text="Fecha de Vuelo")
        self.listado.heading('#8', text="Hora")
        self.listado.heading('#9', text="Valor")
        self.listado.heading('#10', text="Email")
        

    

        #Volver al menú anterior
        menuAnterior = tk.Button(frame_form_access, text="Volver al Menú Anterior", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirVisualizarPasajes)
        menuAnterior.pack(fill=tk.X, padx=20, pady=20)
        menuAnterior.bind("<Return>", (lambda event: self.abrirVisualizarPasajes()))

        self.ventana.mainloop()
    
    def visualizarPasajePorFecha(self):
        #Configuración básica de la ventana
        self.ventana = tk.Tk()                             
        self.ventana.title('Filtrar pasajes por fecha')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        #frame para el título.
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_form.pack(expand=tk.NO, fill=tk.BOTH)

        #Frame superior, ocupado por el texto Menú administrador.
        frame_form_top = tk.Frame(frame_form, height=20, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack (side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text= "Pasaje Aereo según fecha de vuelo", font=('Times', 30, BOLD), fg='#fcfcfc', bg="#3a7ff6", pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        #Botones de acceso.
        frame_form_access = tk.Frame(frame_form, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_access.pack(side="bottom", expand=tk.YES, fill=tk.NONE)

        logo = utl.leer_imagen("./imagenes/logo.png", (200, 200))
        labelLogo = tk.Label(frame_form_access, image=logo, bg='#fcfcfc')
        labelLogo.pack(fill=tk.X, padx=20, pady=10)

        
        etiqueta_fechaPasaje = tk.Label(frame_form_access, text="Inserte la fecha a buscar. Formato dd-mm-aaaa", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_fechaPasaje.pack(fill=tk.X, padx=20, pady=5)
        self.pasajeFecha = ttk.Entry(frame_form_access, font=('Times', 14))
        self.pasajeFecha.pack(fill=tk.BOTH, padx=20, pady=10)

        buscarPasajeCod =  tk.Button(frame_form_access, text="Buscar Pasaje", font=('Times', 14, BOLD), bg='#3a7ff6', bd=0, fg="#fff", command=self.botonVisualizarPasajePorFecha)
        buscarPasajeCod.pack(fill=tk.X, padx=20, pady=20)
        buscarPasajeCod.bind("<Return>", (lambda event: self.botonVisualizarPasajePorFecha()))

        self.listado = ttk.Treeview(frame_form_access, columns=('#0', '#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9'))
        self.listado.pack(fill=tk.X, padx=20, pady=5)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", font=('Times', 14))
        style.configure("Treeview.Heading", font=('Times', 15))

        
        #Nombre de las columnas 
        self.listado.heading('#0', text="Cod. Venta")
        self.listado.heading('#1', text="Nombre")
        self.listado.heading('#2', text="Apellido")
        self.listado.heading('#3', text="N° Documento")
        self.listado.heading('#4', text="Cod. vuelo")
        self.listado.heading('#5', text="Origen")
        self.listado.heading('#6', text="Destino")
        self.listado.heading('#7', text="Fecha de Vuelo")
        self.listado.heading('#8', text="Hora")
        self.listado.heading('#9', text="Valor")
        self.listado.heading('#10', text="Email")
        

    

        #Volver al menú anterior
        menuAnterior = tk.Button(frame_form_access, text="Volver al Menú Anterior", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirVisualizarPasajes)
        menuAnterior.pack(fill=tk.X, padx=20, pady=20)
        menuAnterior.bind("<Return>", (lambda event: self.abrirVisualizarPasajes()))

        self.ventana.mainloop()


    def visualizarPasajePorVenta(self):
        #Configuración básica de la ventana
        self.ventana = tk.Tk()                             
        self.ventana.title('Filtrar pasajes por número de venta')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        #frame para el título.
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_form.pack(expand=tk.NO, fill=tk.BOTH)

        #Frame superior, ocupado por el texto Menú administrador.
        frame_form_top = tk.Frame(frame_form, height=20, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack (side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text= "Pasaje Aereo según número de venta", font=('Times', 30, BOLD), fg='#fcfcfc', bg="#3a7ff6", pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        #Botones de acceso.
        frame_form_access = tk.Frame(frame_form, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_access.pack(side="bottom", expand=tk.YES, fill=tk.NONE)

        logo = utl.leer_imagen("./imagenes/logo.png", (200, 200))
        labelLogo = tk.Label(frame_form_access, image=logo, bg='#fcfcfc')
        labelLogo.pack(fill=tk.X, padx=20, pady=10)

        
        etiqueta_ventaPasaje = tk.Label(frame_form_access, text="Inserte el código de venta", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_ventaPasaje.pack(fill=tk.X, padx=20, pady=5)
        self.pasajeNumVenta = ttk.Entry(frame_form_access, font=('Times', 14))
        self.pasajeNumVenta.pack(fill=tk.BOTH, padx=20, pady=10)

        buscarPasajeCod =  tk.Button(frame_form_access, text="Buscar Pasaje", font=('Times', 14, BOLD), bg='#3a7ff6', bd=0, fg="#fff", command=self.botonVisualizarPasajePorVenta)
        buscarPasajeCod.pack(fill=tk.X, padx=20, pady=20)
        buscarPasajeCod.bind("<Return>", (lambda event: self.botonVisualizarPasajePorVenta()))

        self.listado = ttk.Treeview(frame_form_access, columns=('#0', '#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9'))
        self.listado.pack(fill=tk.X, padx=20, pady=5)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", font=('Times', 14))
        style.configure("Treeview.Heading", font=('Times', 15))

        
        #Nombre de las columnas 
        self.listado.heading('#0', text="Cod. Venta")
        self.listado.heading('#1', text="Nombre")
        self.listado.heading('#2', text="Apellido")
        self.listado.heading('#3', text="N° Documento")
        self.listado.heading('#4', text="Cod. vuelo")
        self.listado.heading('#5', text="Origen")
        self.listado.heading('#6', text="Destino")
        self.listado.heading('#7', text="Fecha de Vuelo")
        self.listado.heading('#8', text="Hora")
        self.listado.heading('#9', text="Valor")
        self.listado.heading('#10', text="Email")
        

    

        #Volver al menú anterior
        menuAnterior = tk.Button(frame_form_access, text="Volver al Menú Anterior", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirVisualizarPasajes)
        menuAnterior.pack(fill=tk.X, padx=20, pady=20)
        menuAnterior.bind("<Return>", (lambda event: self.abrirVisualizarPasajes()))

        self.ventana.mainloop()



######################################################################################################################################################################

    def anularVenta(self):
        db = conexion.get_db()
        #Configuración básica de la ventana
        self.ventana = tk.Tk()                             
        self.ventana.title('Anular Pasaje')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        #frame para el título.
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_form.pack(expand=tk.NO, fill=tk.BOTH)

        #Frame superior, ocupado por el texto de título
        frame_form_top = tk.Frame(frame_form, height=20, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack (side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text= "Anular Venta", font=('Times', 30, BOLD), fg='#fcfcfc', bg="#3a7ff6", pady=50)
        title.pack(expand=tk.NO, fill=tk.BOTH)

        #Botones de acceso.
        frame_form_access = tk.Frame(frame_form, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_access.pack(side="top", expand=tk.YES, fill=tk.NONE)

        logo = utl.leer_imagen("./imagenes/logo.png", (200, 200))
        labelLogo = tk.Label(frame_form_access, image=logo, bg='#fcfcfc')
        labelLogo.pack(fill=tk.X, padx=20, pady=10)

        #SOLICITUD DE LA ID DEL USUARIO A MODIFICAR
        etiqueta_numVenta = tk.Label(frame_form_access, text="Inserte código de venta del pasaje a eliminar", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_numVenta.pack(fill=tk.X, padx=20, pady=5)
        self.anularVentaPasaje = ttk.Entry(frame_form_access, font=('Times', 14))
        self.anularVentaPasaje.pack(fill=tk.BOTH, padx=20, pady=10)

        deleteVenta =  tk.Button(frame_form_access, text="Anular venta", font=('Times', 14, BOLD), bg='#3a7ff6', bd=0, fg="#fff", command=self.botonAnularVenta)
        deleteVenta.pack(fill=tk.X, padx=20, pady=20)
        deleteVenta.bind("<Return>", (lambda event: self.botonAnularVenta()))

        listado = ttk.Treeview(frame_form_access, columns=('#0', '#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9'))
        listado.pack(fill=tk.X, padx=20, pady=5)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", font=('Times', 14))
        style.configure("Treeview.Heading", font=('Times', 15))

        
        #Nombre de las columnas 
        listado.heading('#0', text="Cod. Venta")
        listado.heading('#1', text="Nombre")
        listado.heading('#2', text="Apellido")
        listado.heading('#3', text="N° Documento")
        listado.heading('#4', text="Cod. vuelo")
        listado.heading('#5', text="Origen")
        listado.heading('#6', text="Destino")
        listado.heading('#7', text="Fecha de Vuelo")
        listado.heading('#8', text="Hora")
        listado.heading('#9', text="Valor")
        listado.heading('#10', text="Email")
        

    

        #Volver al menú anterior
        menuAnterior = tk.Button(frame_form_access, text="Volver al Menú Anterior", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirGestionPasajesAereos)
        menuAnterior.pack(fill=tk.X, padx=20, pady=20)
        menuAnterior.bind("<Return>", (lambda event: self.abrirGestionPasajesAereos()))

        pasajes = db.ventaPasajes.find({})
        for pasaje in pasajes:
            listado.insert( "", 
                            tk.END,
                            text=pasaje["_id"],
                            values = (pasaje["nombrePax"], pasaje["apellidoPax"], pasaje["pasajeroId"], pasaje["codVuelo"], pasaje["origen"], pasaje["destino"], pasaje["fechaVuelo"], pasaje["horaVuelo"], pasaje["valorTramo"], pasaje["email"])
                            
                            )
            

        self.ventana.mainloop()


    #BOTONES DE APERTURA DE MENUS FUNCIONES
    def abrirGestionPasajeros(self):
        self.ventana.destroy()
        ft.TrabajadorMenus().menuPasajeros()

    def menuAnterior(self):
        self.ventana.destroy()
        ft.TrabajadorMenus().menuTrabajador()

    def abrirVisualizarPasajeros(self):
        self.ventana.destroy()
        p.trabajador().visualizarPasajeros()

    def abrirVisualizarAllPasajeros(self):
        self.ventana.destroy()
        p.trabajador().visualizarAllPasajeros()

    def abrirVisualizarPasajeroPorDocumento(self):
        self.ventana.destroy()
        p.trabajador().visualizarPasajeroPorDocumento()

    def abrirModificarPasajero(self):
        self.ventana.destroy()
        p.trabajador().modificarPasajero()

    def abrirEliminarPasajero(self):
        self.ventana.destroy()
        p.trabajador().eliminarPasajero()

    def abrirGestionPasajesAereos(self):
        self.ventana.destroy()
        ft.TrabajadorMenus().menuPasajesAereos()

    def abrirVerificarDisponibilidad(self):
        self.ventana.destroy()
        self.verificarDisponibilidadPasaje()

    def abrirVisualizarPasajes(self):
        self.ventana.destroy()
        self.visualizarPasajes()

    def abrirVisualizarTotalPasajes(self):
        self.ventana.destroy()
        self.visualizarTotalPasajes()

    def abrirVisualizarPasajePorCodigoVuelo(self):
        self.ventana.destroy()
        self.visualizarPasajePorCodVuelo()

    def abrirVisualizarPasajePorDocumento(self):
        self.ventana.destroy()
        self.visualizarPasajePorDocumento()

    def abrirVisualizarPasajePorFecha(self):
        self.ventana.destroy()
        self.visualizarPasajePorFecha()

    def abrirVisualizarPasajePorVenta(self):
        self.ventana.destroy()
        self.visualizarPasajePorVenta()

    def abrirAnularVentaPasaje(self):
        self.ventana.destroy()
        self.anularVenta()

    def abrirMenuItinerarios(self):
        self.ventana.destroy()
        i.iti().menuItinerarios()

    def abrirAllItinerarios(self):
        self.ventana.destroy()
        i.iti().allItinerarios()

    def abrirBuscarItinCodigo(self):
        self.ventana.destroy()
        i.iti().itinerarioPorCodigo()

    def abrirBuscarItinFecha(self):
        self.ventana.destroy()
        i.iti().itinerarioPorFecha()

    def botonVerificarDisponibilidad(self):
        db = conexion.get_db()

        fechaVuelo = self.fechaBuscar.get()
        tramo = self.buscarTramo.get()

        #Verificación de la disponibilidad en la base de datos
        verificar = db.itinerarios.find({"fechaIda": fechaVuelo, "origen": {"$regex": tramo, "$options": "i"}})

        if fechaVuelo == "" or tramo == "":
            messagebox.showerror(message="Ingrese una fecha y origen de vuelo")
        else:
            for x in verificar:

                if x["disponibilidad"] <=0:
                    messagebox.showerror(message="Sin disponibilidad para dicha fecha y tramo.", title="Error")
                    return verificar
                else:
                    messagebox.showinfo(message=f"En el tramo {x['origen']}-{x['destino']} existe un total de {x['disponibilidad']} asientos disponibles.\nSu valor es de ${x['valorTramo']}", title="Felicidades")
                    self.etiqueta_documento.pack(fill=tk.X, padx=20, pady=5)
                    self.buscarDocumento.pack(fill=tk.BOTH, padx=20, pady=10)
                    self.verificarRegistroPasajero.pack(fill=tk.X, padx=20, pady=20)

                    #ocultar y mostrar botón de volver atrás
                    self.volver.pack_forget()
                    self.volver.pack(fill=tk.X, padx=20, pady=20)



    def botonVerificarRegistroPasajero(self):
        db = conexion.get_db()

        documento = self.buscarDocumento.get()
        pax = db.pasajeros.find({"_id": documento}, {"_id": 1, "nombre": 1, "apellido": 1, "email": 1})
        if documento == "":
            messagebox.showerror(message="Ingrese un número de documento", title="Error")
            return pax
        else:
            for p in pax:
                if documento == p["_id"]:
                    messagebox.showinfo(message="El pasajero se encuentra registrado en el sistema", title="Felicitaciones")
                    self.etiqueta_numeroVenta.pack(fill=tk.X, padx=20, pady=5)
                    self.nroVenta.pack(fill=tk.BOTH, padx=20, pady=10)  
                    self.agregarVenta.pack(fill=tk.X, padx=20, pady=20)

                    #ocultar y mostrar botón de volver atrás
                    self.volver.pack_forget()
                    self.volver.pack(fill=tk.X, padx=20, pady=20)
                    return pax
                
        # SOLUCIONAR ESTA VERIFICACIÓN #
        messagebox.showerror(message="El pasajero no se encuentra en el sistema", title="Venta")
            
        self.etiqueta_numeroVenta.pack(fill=tk.X, padx=20, pady=5)
        self.nroVenta.pack(fill=tk.BOTH, padx=20, pady=10)

        self.etiqueta_nuevoNombrePax.pack(fill=tk.X, padx=20, pady=5)               
        self.nuevoNombrePax.pack(fill=tk.BOTH, padx=20, pady=10)

        #NUEVO APELLIDO
            
        self.etiqueta_nuevoApellidoPax.pack(fill=tk.X, padx=20, pady=5)
        self.nuevoApellidoPax.pack(fill=tk.BOTH, padx=20, pady=10)

        #nueva nacionalidad
        self.etiqueta_nuevaNacionalidadPax.pack(fill=tk.X, padx=20, pady=5)
        self.nuevaNacionalidadPax.pack(fill=tk.BOTH, padx=20, pady=10)

        #nueva fecha de nacimiento
        self.etiqueta_nuevaFechaNace.pack(fill=tk.X, padx=20, pady=5)
        self.nuevaFechaNacePax.pack(fill=tk.BOTH, padx=20, pady=10)

        #nuevo genero
        self.etiqueta_nuevoGenero.pack(fill=tk.X, padx=20, pady=5)
        self.nuevoGeneroPax.pack(fill=tk.BOTH, padx=20, pady=10)

        #nuevo mail
        self.etiqueta_nuevoEmail.pack(fill=tk.X, padx=20, pady=5)
        self.nuevoEmailPax.pack(fill=tk.BOTH, padx=20, pady=10)

        #nuevo fono
        self.etiqueta_nuevoFono.pack(fill=tk.X, padx=20, pady=5)
        self.nuevoFonoPax.pack(fill=tk.BOTH, padx=20, pady=10)

        #boton agregar venta
        self.agregarVenta.pack(fill=tk.X, padx=20, pady=20)

        #ocultar y mostrar botón de volver atrás
        self.volver.pack_forget()
        self.volver.pack(fill=tk.X, padx=20, pady=20)
        return pax
                


    def botonRealizarVenta(self):
        db = conexion.get_db()

        fechaVuelo = self.fechaBuscar.get()
        tramo = self.buscarTramo.get()
        documento = self.buscarDocumento.get()
        nroVenta = self.nroVenta.get()

        #Verificación de la disponibilidad en la base de datos
        itin = db.itinerarios.find({"fechaIda": fechaVuelo, "origen": {"$regex": tramo, "$options": "i"}})

        pax = db.pasajeros.find({"_id": documento}, {"_id": 1, "nombre": 1, "apellido": 1, "email": 1})

        if fechaVuelo == "" or tramo == "" or documento == "" or nroVenta == "":
            messagebox.showerror(message="No se pueden insertar valores vacíos", title="Error")
        else:
            for x in itin:
                if x["disponibilidad"] <= 0:
                    messagebox.showerror(message="Sin disponibilidad para dicha fecha y tramo.", title="Error")
                    return itin
                else:
                    for p in pax:
                        if documento == p["_id"]:
                            venta = db.ventaPasajes.insert_one({
                                "_id": nroVenta,
                                "nombrePax": p["nombre"],
                                "apellidoPax": p["apellido"],
                                "pasajeroId": p["_id"],
                                "codVuelo": x["_id"],
                                "origen": x["origen"],
                                "destino": x["destino"],
                                "fechaVuelo": x["fechaIda"],
                                "horaVuelo": x["horaIda"],
                                "valorTramo": x["valorTramo"],
                                "email": p["email"]   
                            })

                            #Función para modificar la disponibilidad de los vuelos, cuando haya una venta de pasajes.
                            disp = db.itinerarios.update_one(
                                {"_id": x["_id"]},
                                {
                                    "$inc": {"disponibilidad": -1}
                                }
                            )

                            messagebox.showinfo(message=f"Venta agregada correctamente, verificar en pasajes vendidos\nLos datos han sido enviados a {p['email']}.", title="Venta Correcta")
                            correo.correollamar(nroVenta, p["nombre"], p["apellido"], p["_id"], x["_id"], x["origen"], x["destino"], x["fechaIda"], x["horaIda"], x["valorTramo"], p["email"])

                            self.etiqueta_documento.pack_forget()
                            self.buscarDocumento.pack_forget()
                            self.verificarRegistroPasajero.pack_forget()
                            self.etiqueta_numeroVenta.pack_forget()
                            self.nroVenta.pack_forget()
                            self.agregarVenta.pack_forget()

                            #ocultar y mostrar botón de volver atrás
                            self.volver.pack_forget()
                            self.volver.pack(fill=tk.X, padx=20, pady=20)
                            self.abrirVisualizarTotalPasajes()
                            return venta, disp  
                    else:               
                        nombrePax = self.nuevoNombrePax.get()
                        #NUEVO APELLIDO                     
                        apellidoPax= self.nuevoApellidoPax.get()
                        #nueva nacionalidad                        
                        nacionalidad = self.nuevaNacionalidadPax.get()
                        #nueva fecha de nacimiento                        
                        fechaNace = self.nuevaFechaNacePax.get()
                        #nuevo genero                     
                        genero = self.nuevoGeneroPax.get()
                        #nuevo mail
                        email = self.nuevoEmailPax.get()
                        #nuevo fono
                        telefono = self.nuevoFonoPax.get()            

                        pasajero = db.pasajeros.insert_one({
                        "_id": documento,
                        "nombre": nombrePax,
                        "apellido": apellidoPax,
                        "nacionalidad": nacionalidad,
                        "fechaNacimiento": fechaNace,
                        "genero": genero,
                        "email": email,
                        "telefono": telefono,                                
                        })

                        venta = db.ventaPasajes.insert_one({
                        "_id": nroVenta,
                        "nombrePax": nombrePax,
                        "apellidoPax": apellidoPax,
                        "pasajeroId": documento,
                        "codVuelo": x["_id"],
                        "origen": x["origen"],
                        "destino": x["destino"],
                        "fechaVuelo": x["fechaIda"],
                        "horaVuelo": x["horaIda"],
                        "valorTramo": x["valorTramo"],
                        "email": email  
                        })
                        disp = db.itinerarios.update_one({
                            "_id": x["_id"]},
                        {
                            "$inc": {"disponibilidad": -1}
                        })
                        messagebox.showinfo(message=f"Venta agregada correctamente, verificar en pasajes vendidos.\nLos datos han sido enviados a {email}", title="Venta Correcta")
                        correo.correollamar(nroVenta, nombrePax, apellidoPax, documento, x["_id"], x["origen"], x["destino"], x["fechaIda"], x["horaIda"], x["valorTramo"], email)
                        
                        self.etiqueta_documento.pack_forget()
                        self.buscarDocumento.pack_forget()
                        self.verificarRegistroPasajero.pack_forget()
                        self.etiqueta_numeroVenta.pack_forget()
                        self.nroVenta.pack_forget()
                        self.agregarVenta.pack_forget()
                        self.etiqueta_nuevoNombrePax.pack_forget()               
                        self.nuevoNombrePax.pack_forget()
                        self.etiqueta_nuevoApellidoPax.pack_forget()
                        self.nuevoApellidoPax.pack_forget()
                        self.etiqueta_nuevaNacionalidadPax.pack_forget()
                        self.nuevaNacionalidadPax.pack_forget()
                        self.etiqueta_nuevaFechaNace.pack_forget()
                        self.nuevaFechaNacePax.pack_forget()
                        self.etiqueta_nuevoGenero.pack_forget()
                        self.nuevoGeneroPax.pack_forget()
                        self.etiqueta_nuevoEmail.pack_forget()
                        self.nuevoEmailPax.pack_forget()
                        self.etiqueta_nuevoFono.pack_forget()
                        self.nuevoFonoPax.pack_forget()
                        #ocultar y mostrar botón de volver atrás
                        self.volver.pack_forget()
                        self.volver.pack(fill=tk.X, padx=20, pady=20)
                        self.abrirVisualizarTotalPasajes()
                        return pasajero, venta, disp

    # SOLUCIONAR VERIFICACIÓN DE MAYUSCULAS
    def botonVisualizarPasajePorCodVuelo(self):
        db = conexion.get_db()
        codVuelo = self.pasajeCodVuelo.get()

        pasajes = db.ventaPasajes.find({"codVuelo": {"$regex": f"^{codVuelo}$", "$options": "$i"}})
        for pasaje in pasajes:
            
            if codVuelo == pasaje["codVuelo"]:
                
                self.listado.insert( "", 
                            tk.END,
                            text=pasaje["_id"],
                            values = (pasaje["nombrePax"], pasaje["apellidoPax"], pasaje["pasajeroId"], pasaje["codVuelo"], pasaje["origen"], pasaje["destino"], pasaje["fechaVuelo"], pasaje["horaVuelo"], pasaje["valorTramo"], pasaje["email"])
                            
                            )
                
        else:
            messagebox.showerror(message="El código de vuelo ingresado no está a asociado a ningún pasaje vendido.", title="Error")

    # SOLUCIONAR VERIFICACIÓN DE MAYUSCULAS
    def botonVisualizarPasajePorDocumento(self):
        db = conexion.get_db()
        documento = self.pasajeDocumento.get()

        pasajes = db.ventaPasajes.find({"pasajeroId": {"$regex": f"^{documento}$", "$options": "$i"}})
        for pasaje in pasajes:
            
            if documento == pasaje["pasajeroId"]:
                
                self.listado.insert( "", 
                            tk.END,
                            text=pasaje["_id"],
                            values = (pasaje["nombrePax"], pasaje["apellidoPax"], pasaje["pasajeroId"], pasaje["codVuelo"], pasaje["origen"], pasaje["destino"], pasaje["fechaVuelo"], pasaje["horaVuelo"], pasaje["valorTramo"], pasaje["email"])
                            
                            )
                
        else:
            messagebox.showerror(message="El documento ingresado no se encuentra asociado a ningún pasaje vendido.", title="Error")

    def botonVisualizarPasajePorFecha(self):
        db = conexion.get_db()
        fecha = self.pasajeFecha.get()

        pasajes = db.ventaPasajes.find({"fechaVuelo": {"$regex": f"^{fecha}$", "$options": "$i"}})
        for pasaje in pasajes:
            
            if fecha == pasaje["fechaVuelo"]:
                
                self.listado.insert( "", 
                            tk.END,
                            text=pasaje["_id"],
                            values = (pasaje["nombrePax"], pasaje["apellidoPax"], pasaje["pasajeroId"], pasaje["codVuelo"], pasaje["origen"], pasaje["destino"], pasaje["fechaVuelo"], pasaje["horaVuelo"], pasaje["valorTramo"], pasaje["email"])
                            
                            )
                
        else:
            messagebox.showerror(message="No existe un pasaje vendido para la fecha solicitada.", title="Error")

    def botonVisualizarPasajePorVenta(self):
        db = conexion.get_db()
        numVenta = self.pasajeNumVenta.get()

        pasajes = db.ventaPasajes.find({"_id": {"$regex": f"^{numVenta}$", "$options": "$i"}})
        for pasaje in pasajes:
            
            if numVenta == pasaje["_id"]:
                
                self.listado.insert( "", 
                            tk.END,
                            text=pasaje["_id"],
                            values = (pasaje["nombrePax"], pasaje["apellidoPax"], pasaje["pasajeroId"], pasaje["codVuelo"], pasaje["origen"], pasaje["destino"], pasaje["fechaVuelo"], pasaje["horaVuelo"], pasaje["valorTramo"], pasaje["email"])
                            
                            )
                
        else:
            messagebox.showerror(message="El código de venta no se encuentra asociado a ningún pasaje.", title="Error")

    
    def botonAnularVenta(self):
        db = conexion.get_db()
        nroVenta = self.anularVentaPasaje.get()

        itin = db.ventaPasajes.find({"_id": nroVenta})
        for x in itin:

            if nroVenta == x["_id"]:
                #Antes de anular la venta del pasaje, el sistema actualizará la disponibilidad del vuelo a anular, en este caso lo aumenta en 1.
                actItin = db.itinerarios.update_one(
                    {"_id": {"$regex": x["codVuelo"], "$options":"i"}},
                    {
                        '$inc': {"disponibilidad": 1}
                    }
                    )
                delpasaje = db.ventaPasajes.delete_one({"_id": nroVenta})
                messagebox.showinfo(message="Venta anulada correctamente", title="Felicitaciones")
                self.abrirAnularVentaPasaje()
                return actItin, delpasaje
        else:
            messagebox.showerror(message="No existe una venta con el código ingresado.", title="Error") 
