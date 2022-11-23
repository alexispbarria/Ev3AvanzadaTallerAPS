import tkinter as tk
from tkinter.font import BOLD
import util.generic as utl
from ..trabajador import pasajeros as p
from forms import form_login as fl
from ..trabajador import pasajesaereo as pa
from ..trabajador import iti as i


class TrabajadorMenus:

    def menuTrabajador(self):

        #Configuración básica de la ventana
        self.ventana = tk.Tk()                             
        self.ventana.title('Menú Trabajador')
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
        title = tk.Label(frame_form_top, text= "Menú Trabajador", font=('Times', 30, BOLD), fg='#fcfcfc', bg="#3a7ff6", pady=50)
        title.pack(expand=tk.NO, fill=tk.BOTH)

        #Botones de acceso.
        frame_form_access = tk.Frame(frame_form, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_access.pack(side="bottom", expand=tk.YES, fill=tk.Y)

        logo = utl.leer_imagen("./imagenes/logo.png", (200, 200))
        labelLogo = tk.Label(frame_form_access, image=logo, bg='#fcfcfc')
        labelLogo.pack(fill=tk.X, padx=20, pady=10)

         #Gestión de Pasajeros
        
        gestionPasajeros = tk.Button(frame_form_access, text="Gestionar Pasajeros", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirGestionPasajeros)
        gestionPasajeros.pack(fill=tk.X, padx=20, pady=20)
        gestionPasajeros.bind("<Return>", (lambda event: self.abrirGestionPasajeros()))

        #Gestión de Pasajes Aéreos
        
        gestionPasajesAereos = tk.Button(frame_form_access, text="Gestionar Pasajes Aéreos", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirGestionPasajesAereos)
        gestionPasajesAereos.pack(fill=tk.X, padx=20, pady=20)
        gestionPasajesAereos.bind("<Return>", (lambda event: self.abrirGestionPasajesAereos()))

        #Visualizar Itinerarios de Vuelo
        
        itinVuelo = tk.Button(frame_form_access, text="Visualizar Itinerarios de Vuelo", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirMenuItinerarios)
        itinVuelo.pack(fill=tk.X, padx=20, pady=20)
        itinVuelo.bind("<Return>", (lambda event: self.abrirMenuItinerarios()))

        #Cerrar sesión
        cerrarSesion = tk.Button(frame_form_access, text="Cerrar sesión", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abririniciosesion)
        cerrarSesion.pack(fill=tk.X, padx=20, pady=20)
        gestionPasajesAereos.bind("<Return>", (lambda event: self.abririniciosesion()))

        self.ventana.mainloop()



    #PASAJEROS BLOQUE
    def menuPasajeros(self):
        #Configuración básica de la ventana
        self.ventana = tk.Tk()                             
        self.ventana.title('Gestión de Pasajeros')
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
        title = tk.Label(frame_form_top, text= "Gestión de Pasajeros", font=('Times', 30, BOLD), fg='#fcfcfc', bg="#3a7ff6", pady=50)
        title.pack(expand=tk.NO, fill=tk.BOTH)

        #Botones de acceso.
        frame_form_access = tk.Frame(frame_form, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_access.pack(side="bottom", expand=tk.YES, fill=tk.Y)

        #Imágen
        logo = utl.leer_imagen("./imagenes/logo.png", (200, 200))
        labelLogo = tk.Label(frame_form_access, image=logo, bg='#fcfcfc')
        labelLogo.pack(fill=tk.X, padx=20, pady=10)

        #Ver Pasajeros
        verPasajeros = tk.Button(frame_form_access, text="Visualizar Pasajeros", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirVisualizarPasajeros)
        verPasajeros.pack(fill=tk.X, padx=20, pady=20)
        verPasajeros.bind("<Return>", (lambda event: p.trabajador.abrirVisualizarPasajeros()))

        #Modificar Pasajero
        
        modificarPasajero = tk.Button(frame_form_access, text="Modificar Pasajero", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirModificarPasajero)
        modificarPasajero.pack(fill=tk.X, padx=20, pady=20)
        modificarPasajero.bind("<Return>", (lambda event: p.trabajador.abrirModificarPasajero()))

        #Eliminar Pasajero
        
        eliminarPasajero = tk.Button(frame_form_access, text="Eliminar Pasajero", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirEliminarPasajero)
        eliminarPasajero.pack(fill=tk.X, padx=20, pady=20)
        eliminarPasajero.bind("<Return>", (lambda event: p.trabajador.abrirEliminarPasajero()))

        #Volver al menú anterior
        menuAnterior = tk.Button(frame_form_access, text="Volver al Menú Anterior", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.menuAnterior)
        menuAnterior.pack(fill=tk.X, padx=20, pady=20)
        menuAnterior.bind("<Return>", (lambda event: self.menuAnterior()))

        self.ventana.mainloop()


    def menuPasajesAereos(self):
        #Configuración básica de la ventana
        self.ventana = tk.Tk()                             
        self.ventana.title('Gestionar Pasajes Aereos')
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
        title = tk.Label(frame_form_top, text= "Gestionar Pasajes Aereos", font=('Times', 30, BOLD), fg='#fcfcfc', bg="#3a7ff6", pady=50)
        title.pack(expand=tk.NO, fill=tk.BOTH)

        #Botones de acceso.
        frame_form_access = tk.Frame(frame_form, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_access.pack(side="bottom", expand=tk.YES, fill=tk.Y)

        #Imágen
        logo = utl.leer_imagen("./imagenes/logo.png", (200, 200))
        labelLogo = tk.Label(frame_form_access, image=logo, bg='#fcfcfc')
        labelLogo.pack(fill=tk.X, padx=20, pady=10)

        #Realizar venta de pasajes
        
        ventaPasaje = tk.Button(frame_form_access, text="Realizar Venta de Pasaje", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirVerificarDisponibilidad)
        ventaPasaje.pack(fill=tk.X, padx=20, pady=20)
        ventaPasaje.bind("<Return>", (lambda event: self.abrirVerificarDisponibilidad()))

        #Visualizar pasajes vendidos
        
        visualizarPasajeVendido = tk.Button(frame_form_access, text="Visualizar Pasajes Vendidos", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirVisualizarPasajes)
        visualizarPasajeVendido.pack(fill=tk.X, padx=20, pady=20)
        visualizarPasajeVendido.bind("<Return>", (lambda event: self.abrirVisualizarPasajes()))

        anularVentaPasaje = tk.Button(frame_form_access, text="Anular Venta", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirAnularVentaPasaje)
        anularVentaPasaje.pack(fill=tk.X, padx=20, pady=20)
        anularVentaPasaje.bind("<Return>", (lambda event: self.abrirAnularVentaPasaje()))

        #Volver al menú anterior
        menuAnterior = tk.Button(frame_form_access, text="Volver al Menú Anterior", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.menuAnterior)
        menuAnterior.pack(fill=tk.X, padx=20, pady=20)
        menuAnterior.bind("<Return>", (lambda event: self.menuAnterior()))
    
        self.ventana.mainloop()
        

    #BOTONES DE APERTURA DE MENUS FUNCIONES
    def abrirGestionPasajeros(self):
        self.ventana.destroy()
        self.menuPasajeros()

    def menuAnterior(self):
        self.ventana.destroy()
        self.menuTrabajador()

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

    def abririniciosesion(self):
        self.ventana.destroy()
        fl.App()

    def abrirGestionPasajesAereos(self):
        self.ventana.destroy()
        self.menuPasajesAereos()

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
