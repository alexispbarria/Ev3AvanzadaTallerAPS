import tkinter as tk
from tkinter.font import BOLD
from tkinter import ttk, messagebox
import conexion
import util.generic as utl
from ..trabajador import form_trabajador as ft
from ..trabajador import pasajeros as p
from ..trabajador import pasajesaereo as pa


################################################################################################################################################################################
#ITINERARIOS
class iti:
    def menuItinerarios(self):
        #Configuración básica de la ventana
        self.ventana = tk.Tk()                             
        self.ventana.title('Visualizar Itinerarios')
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
        title = tk.Label(frame_form_top, text= "Visualizar Itinerarios", font=('Times', 30, BOLD), fg='#fcfcfc', bg="#3a7ff6", pady=50)
        title.pack(expand=tk.NO, fill=tk.BOTH)

        #Botones de acceso.
        frame_form_access = tk.Frame(frame_form, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_access.pack(side="bottom", expand=tk.YES, fill=tk.Y)


        logo = utl.leer_imagen("./imagenes/logo.png", (200, 200))
        labelLogo = tk.Label(frame_form_access, image=logo, bg='#fcfcfc')
        labelLogo.pack(fill=tk.X, padx=20, pady=10)


         #Visualizar Itinerarios totales
        
        totalItinerarios = tk.Button(frame_form_access, text="Visualizar total de Itinerarios", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirAllItinerarios)
        totalItinerarios.pack(fill=tk.X, padx=20, pady=20)
        totalItinerarios.bind("<Return>", (lambda event: self.abrirAllItinerarios()))

        #Buscar por código
        
        verCodItinerario = tk.Button(frame_form_access, text="Buscar Itinerario por código", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirBuscarItinCodigo)
        verCodItinerario.pack(fill=tk.X, padx=20, pady=20)
        verCodItinerario.bind("<Return>", (lambda event: self.abrirBuscarItinCodigo()))

        #Buscar por fecha
        
        verFechaItinerario = tk.Button(frame_form_access, text="Buscar itinerario por fecha", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirBuscarItinFecha)
        verFechaItinerario.pack(fill=tk.X, padx=20, pady=20)
        verFechaItinerario.bind("<Return>", (lambda event: self.abrirBuscarItinFecha()))

        #Volver al menú anterior
        menuAnterior = tk.Button(frame_form_access, text="Volver al Menú Anterior", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.menuAnterior)
        menuAnterior.pack(fill=tk.X, padx=20, pady=20)
        menuAnterior.bind("<Return>", (lambda event: self.menuAnterior()))

        self.ventana.mainloop()


    def allItinerarios(self):
        db = conexion.get_db()

        #Configuración básica de la ventana
        self.ventana = tk.Tk()                             
        self.ventana.title('Total de Itinerarios')
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
        title = tk.Label(frame_form_top, text= "Total de Itinerarios", font=('Times', 30, BOLD), fg='#fcfcfc', bg="#3a7ff6", pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        #Botones de acceso.
        frame_form_access = tk.Frame(frame_form, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_access.pack(side="bottom", expand=tk.YES, fill=tk.NONE)

        logo = utl.leer_imagen("./imagenes/logo.png", (200, 200))
        labelLogo = tk.Label(frame_form_access, image=logo, bg='#fcfcfc')
        labelLogo.pack(fill=tk.X, padx=20, pady=10)


        listado = ttk.Treeview(frame_form_access, columns=('#0', '#1', '#2', '#3', '#4', '#5', '#6'))
        listado.pack(fill=tk.X, padx=20, pady=5)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", font=('Times', 14))
        style.configure("Treeview.Heading", font=('Times', 15))

        
        #Nombre de las columnas 
        listado.heading('#0', text="Código de Vuelo")
        listado.heading('#1', text="Origen")
        listado.heading('#2', text="Destino")
        listado.heading('#3', text="Fecha de Ida")
        listado.heading('#4', text="Duración")
        listado.heading('#5', text="Hora de Vuelo")
        listado.heading('#6', text="Valor del Pasaje")
        listado.heading('#7', text="Asientos Disponibles")

    

        #Volver al menú anterior
        menuAnterior = tk.Button(frame_form_access, text="Volver al Menú Anterior", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirMenuItinerarios)
        menuAnterior.pack(fill=tk.X, padx=20, pady=20)
        menuAnterior.bind("<Return>", (lambda event: self.abrirMenuItinerarios()))

        itinerarios = db.itinerarios.find({})
        for itinerario in itinerarios:
            listado.insert( "", 
                            tk.END,
                            text=itinerario["_id"],
                            values = (itinerario["origen"], itinerario["destino"], itinerario["fechaIda"], itinerario["duracion"], itinerario["horaIda"], itinerario["valorTramo"], itinerario["disponibilidad"])
                            
                            )
            

        self.ventana.mainloop()

    def itinerarioPorCodigo(self):
        #Configuración básica de la ventana
        self.ventana = tk.Tk()                             
        self.ventana.title('Filtrar Itinerarios por Código')
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
        title = tk.Label(frame_form_top, text= "Itinerario según código", font=('Times', 30, BOLD), fg='#fcfcfc', bg="#3a7ff6", pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        #Botones de acceso.
        frame_form_access = tk.Frame(frame_form, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_access.pack(side="bottom", expand=tk.YES, fill=tk.NONE)

        logo = utl.leer_imagen("./imagenes/logo.png", (200, 200))
        labelLogo = tk.Label(frame_form_access, image=logo, bg='#fcfcfc')
        labelLogo.pack(fill=tk.X, padx=20, pady=10)

        #SOLICITUD DEl codigo del vuelo a consultar
        etiqueta_codigoVuelo = tk.Label(frame_form_access, text="Inserte el código del vuelo a buscar", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_codigoVuelo.pack(fill=tk.X, padx=20, pady=5)
        self.codVueloBuscar = ttk.Entry(frame_form_access, font=('Times', 14))
        self.codVueloBuscar.pack(fill=tk.BOTH, padx=20, pady=10)

        buscarCodigoVuelo =  tk.Button(frame_form_access, text="Buscar Vuelo", font=('Times', 14, BOLD), bg='#3a7ff6', bd=0, fg="#fff", command=self.botonBuscarCodigoVuelo)
        buscarCodigoVuelo.pack(fill=tk.X, padx=20, pady=20)
        buscarCodigoVuelo.bind("<Return>", (lambda event: self.botonBuscarCodigoVuelo()))

        self.listadoCod = ttk.Treeview(frame_form_access, columns=('#0', '#1', '#2', '#3', '#4', '#5', '#6'))
        self.listadoCod.pack(fill=tk.X, padx=20, pady=5)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", font=('Times', 14))
        style.configure("Treeview.Heading", font=('Times', 15))

        
        #Nombre de las columnas 
        self.listadoCod.heading('#0', text="Código de Vuelo")
        self.listadoCod.heading('#1', text="Origen")
        self.listadoCod.heading('#2', text="Destino")
        self.listadoCod.heading('#3', text="Fecha de Ida")
        self.listadoCod.heading('#4', text="Duración")
        self.listadoCod.heading('#5', text="Hora de Vuelo")
        self.listadoCod.heading('#6', text="Valor del Pasaje")
        self.listadoCod.heading('#7', text="Asientos Disponibles")       

        #Volver al menú anterior
        menuAnterior = tk.Button(frame_form_access, text="Volver al Menú Anterior", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirMenuItinerarios)
        menuAnterior.pack(fill=tk.X, padx=20, pady=20)
        menuAnterior.bind("<Return>", (lambda event: self.abrirMenuItinerarioss()))

        self.ventana.mainloop()

    def itinerarioPorFecha(self):
        #Configuración básica de la ventana
        self.ventana = tk.Tk()                             
        self.ventana.title('Filtrar Itinerarios por Fecha')
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
        title = tk.Label(frame_form_top, text= "Itinerario según Fecha", font=('Times', 30, BOLD), fg='#fcfcfc', bg="#3a7ff6", pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        #Botones de acceso.
        frame_form_access = tk.Frame(frame_form, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_access.pack(side="bottom", expand=tk.YES, fill=tk.NONE)

        logo = utl.leer_imagen("./imagenes/logo.png", (200, 200))
        labelLogo = tk.Label(frame_form_access, image=logo, bg='#fcfcfc')
        labelLogo.pack(fill=tk.X, padx=20, pady=10)

        #SOLICITUD DEl codigo del vuelo a consultar
        etiqueta_fechaVuelo = tk.Label(frame_form_access, text="Inserte la fecha del vuelo a buscar", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_fechaVuelo.pack(fill=tk.X, padx=20, pady=5)
        self.fechaVueloBuscar = ttk.Entry(frame_form_access, font=('Times', 14))
        self.fechaVueloBuscar.pack(fill=tk.BOTH, padx=20, pady=10)

        buscarFechaVuelo =  tk.Button(frame_form_access, text="Buscar Vuelo", font=('Times', 14, BOLD), bg='#3a7ff6', bd=0, fg="#fff", command=self.botonBuscarFechaVuelo)
        buscarFechaVuelo.pack(fill=tk.X, padx=20, pady=20)
        buscarFechaVuelo.bind("<Return>", (lambda event: self.botonBuscarFechaVuelo()))

        self.listadoFecha = ttk.Treeview(frame_form_access, columns=('#0', '#1', '#2', '#3', '#4', '#5', '#6'))
        self.listadoFecha.pack(fill=tk.X, padx=20, pady=5)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", font=('Times', 14))
        style.configure("Treeview.Heading", font=('Times', 15))

        
        #Nombre de las columnas 
        self.listadoFecha.heading('#0', text="Código de Vuelo")
        self.listadoFecha.heading('#1', text="Origen")
        self.listadoFecha.heading('#2', text="Destino")
        self.listadoFecha.heading('#3', text="Fecha de Ida")
        self.listadoFecha.heading('#4', text="Duración")
        self.listadoFecha.heading('#5', text="Hora de Vuelo")
        self.listadoFecha.heading('#6', text="Valor del Pasaje")
        self.listadoFecha.heading('#7', text="Asientos Disponibles")       

        #Volver al menú anterior
        menuAnterior = tk.Button(frame_form_access, text="Volver al Menú Anterior", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirMenuItinerarios)
        menuAnterior.pack(fill=tk.X, padx=20, pady=20)
        menuAnterior.bind("<Return>", (lambda event: self.abrirMenuItinerarios()))

        self.ventana.mainloop()

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
        pa.pasajes().verificarDisponibilidadPasaje()

    def abrirVisualizarPasajes(self):
        self.ventana.destroy()
        pa.pasajes().visualizarPasajes()

    def abrirVisualizarTotalPasajes(self):
        self.ventana.destroy()
        pa.pasajes().visualizarTotalPasajes()

    def abrirVisualizarPasajePorCodigoVuelo(self):
        self.ventana.destroy()
        pa.pasajes().visualizarPasajePorCodVuelo()

    def abrirVisualizarPasajePorDocumento(self):
        self.ventana.destroy()
        pa.pasajes().visualizarPasajePorDocumento()

    def abrirVisualizarPasajePorFecha(self):
        self.ventana.destroy()
        pa.pasajes().visualizarPasajePorFecha()

    def abrirVisualizarPasajePorVenta(self):
        self.ventana.destroy()
        pa.pasajes().visualizarPasajePorVenta()

    def abrirAnularVentaPasaje(self):
        self.ventana.destroy()
        pa.pasajes().anularVenta()

    def abrirMenuItinerarios(self):
        self.ventana.destroy()
        self.menuItinerarios()

    def abrirAllItinerarios(self):
        self.ventana.destroy()
        self.allItinerarios()

    def abrirBuscarItinCodigo(self):
        self.ventana.destroy()
        self.itinerarioPorCodigo()

    def abrirBuscarItinFecha(self):
        self.ventana.destroy()
        self.itinerarioPorFecha()

    def botonBuscarCodigoVuelo(self):
        db = conexion.get_db()
        codVuelo = self.codVueloBuscar.get()

        itinerarios = db.itinerarios.find({"_id": codVuelo})
        for itin in itinerarios:
            itincod = (str.format(itin["_id"]))
            if codVuelo == itincod:
                
                self.listadoCod.insert( "", 
                            tk.END,
                            text=itin["_id"],
                            values = (itin["origen"], itin["destino"], itin["fechaIda"], itin["duracion"], itin["horaIda"], itin["valorTramo"], itin["disponibilidad"])
                                
                            )
                return itinerarios
        else:   
            messagebox.showerror(message="El código ingresado no existe.", title="Error")   

    def botonBuscarFechaVuelo(self):
        db = conexion.get_db()
        fechaVuelo = self.fechaVueloBuscar.get()

        itinerarios = db.itinerarios.find({"fechaIda": fechaVuelo})
        for itin in itinerarios:
            itinfecha = (str.format(itin["fechaIda"]))
            if fechaVuelo == itinfecha:
                
                self.listadoFecha.insert( "", 
                            tk.END,
                            text=itin["_id"],
                            values = (itin["origen"], itin["destino"], itin["fechaIda"], itin["duracion"], itin["horaIda"], itin["valorTramo"], itin["disponibilidad"])
                                
                            )
        else:
            messagebox.showerror(message="la fecha ingresada no cuenta con vuelos programados.", title="Error")
        